"""Run interactively to save an AutoDL ComfyUI token for this macOS user."""
import getpass
import os
from pathlib import Path
import sys

if not sys.stdin.isatty():
    sys.exit('Run this in your own interactive terminal; do not paste credentials into chat.')
p = Path.home() / '.config/pocket-rove/autodl-comfyui.token'
if p.exists() or p.is_symlink():
    sys.exit('A credential already exists; nothing changed.')
print('The token will be saved locally with owner-only permissions at: ' + str(p))
print('Other tasks running as this macOS user can use it. It will not be stored in the project.')
token = getpass.getpass('Paste the ComfyUI token (hidden): ').strip()
if not token or '\n' in token or '\r' in token:
    sys.exit('Invalid empty or multiline token; nothing saved.')
p.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
fd = os.open(p, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
with os.fdopen(fd, 'w') as out:
    out.write(token)
print('Credential saved. No API request was sent.')
