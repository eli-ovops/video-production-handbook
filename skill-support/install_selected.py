"""Project-only skill file installation; never runs upstream setup or generation."""
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path('/Volumes/EXTERNAL/ai视频')
DEST = ROOT / '.agents/skills'
SUPPORT = ROOT / 'skill-support'
HELPER = Path('/Users/USER/.codex/skills/.system/skill-installer/scripts')
sys.path.insert(0, str(HELPER))
spec = importlib.util.spec_from_file_location('codex_skill_installer', HELPER / 'install-skill-from-github.py')
installer = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = installer
spec.loader.exec_module(installer)

def request_public(url):
    return subprocess.run(['curl', '--fail', '--silent', '--show-error', '--location',
                           '--connect-timeout', '10', '--max-time', '120', url],
                          check=True, stdout=subprocess.PIPE).stdout

installer._request = request_public
FILM = ['director-agent', 'ai-storyboard-director', 'character-asset', 'scene-asset',
        'prop-asset', 'cyberpunk-design', 'epic-design', 'fantasy-design',
        'horror-design', 'noir-design', 'romance-design', 'war-design', 'wuxia-design']
REMOTE = [
    ('62656456/ai-film-skills', '678edc06d3318c1516f6eb73503f740427fdd831',
     [('skills/' + name, name) for name in FILM]),
    ('seaartpublic/skills', 'a3edc17605d525b54b2a5f61a4800f2dd8dd8b30',
     [('storyboard-prompt-assistant', 'storyboard-prompt-assistant')]),
    ('alchaincyf/seedance-skill', 'f14d8fa19b57c83f674c70e5730a19df4ef4accd',
     [('.', 'seedance-whitebox')]),
    ('remotion-dev/skills', '11986e44eeb672b083354e68967f2b194df73b7c',
     [('skills/remotion-best-practices', 'remotion-best-practices')]),
    ('Ashad001/remotion-transitions', '2bf15881f1f9d74e4b76979cd0846aefffc9962c',
     [('.', 'remotion-transitions')]),
]
LOCAL = ['prompt-videos', 'seedance-prompt', 'seedance-prompt-en', 'video-understand',
         'hyperframes-creative', 'hyperframes-animation', 'media-use', 'video-edit']

def tree_hashes(directory):
    return {str(p.relative_to(directory)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(directory.rglob('*')) if p.is_file()}

def main():
    DEST.mkdir(parents=True, exist_ok=True)
    records = []
    for repo, ref, paths in REMOTE:
        missing = [(p, name) for p, name in paths if not (DEST / name).exists()]
        if missing:
            args = ['--repo', repo, '--ref', ref, '--dest', str(DEST), '--method', 'download',
                    '--path', *[p for p, _ in missing]]
            if len(missing) == 1:
                args.extend(['--name', missing[0][1]])
            if installer.main(args) != 0:
                raise RuntimeError('Installer failed for ' + repo)
        for path, name in paths:
            assert (DEST / name / 'SKILL.md').is_file(), name
            records.append({'name': name, 'source': repo, 'ref': ref, 'source_path': path,
                            'kind': 'github-pinned', 'hashes': tree_hashes(DEST / name)})
    for name in LOCAL:
        source = Path('/Users/USER/.agents/skills') / name
        target = DEST / name
        assert (source / 'SKILL.md').is_file(), source
        if not target.exists():
            shutil.copytree(source, target)
        assert tree_hashes(source) == tree_hashes(target), 'Local copy mismatch: ' + name
        records.append({'name': name, 'source': str(source), 'kind': 'local-snapshot',
                        'hashes': tree_hashes(target)})
    manifest = SUPPORT / 'installed-manifest.json'
    if manifest.exists():
        raise RuntimeError('Preserving existing manifest: ' + str(manifest))
    manifest.write_text(json.dumps({'schema': 1, 'root': str(ROOT), 'skills': records,
                                   'runtime_tested': False, 'video_generation_authorized': False},
                                  ensure_ascii=False, indent=2) + '\n')
    print('VERIFIED_SKILL_PACKAGES=' + str(len(records)), flush=True)
    print('MANIFEST=' + str(manifest), flush=True)

if __name__ == '__main__':
    main()
