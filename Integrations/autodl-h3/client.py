"""AutoDL ComfyUI client. No automatic POST retries or embedded credentials."""
import argparse
import json
import os
from pathlib import Path
import re
import sys
import urllib.request
import urllib.error

BASE = 'https://autodl.art/api/v1/comfyui/comfyui_workflow'

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None

def identifier(value):
    if not re.fullmatch(r'[A-Za-z0-9_-]+', value):
        raise ValueError('Invalid workflow/task identifier')
    return value

def request(method, suffix, payload=None):
    token = os.environ.get('AUTODL_COMFYUI_TOKEN', '').strip()
    if not token:
        credential = Path.home() / '.config/pocket-rove/autodl-comfyui.token'
        if credential.exists():
            if credential.is_symlink() or credential.stat().st_mode & 0o077:
                raise ValueError('Credential file must be a regular private file (chmod 600)')
            token = credential.read_text().strip()
    if not token:
        raise ValueError('Run setup_token.py locally, or set AUTODL_COMFYUI_TOKEN')
    req = urllib.request.Request(BASE + '/' + suffix,
        data=json.dumps(payload).encode() if payload is not None else None,
        headers={'Authorization': token, 'Content-Type': 'application/json'}, method=method)
    try:
        with urllib.request.build_opener(NoRedirect).open(req, timeout=60) as response:
            return json.load(response)
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f'HTTP {exc.code}; response body suppressed. Do not retry a submission until task logs are checked.') from None
    except (urllib.error.URLError, TimeoutError):
        raise RuntimeError('Network outcome uncertain. Check platform task logs before submitting again.') from None

def main():
    p = argparse.ArgumentParser(description=__doc__)
    s = p.add_subparsers(dest='action', required=True)
    dry = s.add_parser('validate')
    dry.add_argument('payload', type=Path)
    submit = s.add_parser('submit')
    submit.add_argument('workflow')
    submit.add_argument('payload', type=Path)
    submit.add_argument('--approved-charge', action='store_true', help='Use only after the user approves the concrete test and its charge')
    submit.add_argument('--record', type=Path, required=True)
    status = s.add_parser('status')
    status.add_argument('task_id')
    status.add_argument('--record', type=Path, required=True)
    a = p.parse_args()
    if a.action in ('validate', 'submit'):
        payload = json.loads(a.payload.read_text())
        if not isinstance(payload, dict) or not isinstance(payload.get('prompt'), str) or not payload['prompt'].strip():
            raise ValueError('A nonempty prompt is required')
        if not 1 <= len(payload['prompt']) <= 10000:
            raise ValueError('Prompt exceeds documented U24 length')
        if type(payload.get('duration')) is not int or not 1 <= payload['duration'] <= 15:
            raise ValueError('Duration must be an integer from 1 through 15')
        if a.action == 'validate':
            print('Local JSON validation passed; workflow schema/auth/billing not yet verified.')
            return
        if not a.approved_charge:
            raise ValueError('Submission requires approved test and charge; no request sent')
        suffix = identifier(a.workflow)
    else:
        suffix = 'result/' + identifier(a.task_id)
    # Reserve output before any request so an existing record cannot be overwritten.
    with a.record.open('x', encoding='utf-8') as out:
        result = request('POST' if a.action == 'submit' else 'GET', suffix,
                         payload if a.action == 'submit' else None)
        json.dump(result, out, ensure_ascii=False, indent=2)
    data = result.get('data') or {}
    print(json.dumps({'code': result.get('code'), 'task_id': data.get('task_id'),
                      'status': data.get('status'), 'saved_to': str(a.record)}, ensure_ascii=False))

if __name__ == '__main__':
    try:
        main()
    except (ValueError, RuntimeError, OSError) as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
