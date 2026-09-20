"""Dependency-free public integrity gate, not private runtime validation."""
from pathlib import Path
import hashlib, json, re
ROOT = Path(__file__).resolve().parents[1]
def unique(pairs):
    result = {}
    for key, value in pairs:
        assert key not in result, f'duplicate JSON key: {key}'
        result[key] = value
    return result
def check():
    checks = []
    for path in sorted((ROOT / 'docs').rglob('*.json')) + [ROOT / 'lvs-educt.schema.json']:
        json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=unique,
                   parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))
        checks.append('JSON:' + path.relative_to(ROOT).as_posix())
    status = json.loads((ROOT / 'docs/machine/project-status.json').read_text())
    evidence = json.loads((ROOT / 'docs/machine/verification-summary.json').read_text())
    assert status['products']['commercial_runtime'] == 'STAGED_NOT_PUBLIC'
    assert status['public_release_version'] is None
    assert status['token_savings'] is None and evidence['token_savings_percent'] is None
    assert not status['transaction_endpoint_available']
    assert evidence['independent_reproduction'] == 'PENDING'
    assert evidence['local_tests']['passed'] == 46 and not evidence['local_tests']['independent']
    b = evidence['benchmark']
    assert b['final_accepted'] == b['final_total'] == 36
    assert b['all_attempts_accepted'] / b['all_attempts_total'] == b['all_attempt_acceptance_rate'] == 0.6
    checks.append('MATURITY_AND_EVIDENCE_CONSISTENCY')
    # Git checks out CRLF on Windows and LF in Linux CI; normalize only line endings.
    assert hashlib.sha256((ROOT / 'LICENSE').read_bytes().replace(b'\r\n', b'\n')).hexdigest() == 'b3714873c3fb7358463015f40643e103629b4190ff4f440d15647306f67f6666'
    checks.append('LICENSE_CONTENT_UNCHANGED')
    targets = [ROOT / 'README.md', *sorted((ROOT / 'docs').rglob('*.md')), ROOT / 'docs/index.html']
    for path in targets:
        content = path.read_text(encoding='utf-8')
        for html, md in re.findall(r'href="([^"]+)"|\]\(([^)]+)\)', content):
            link = (html or md).split('#')[0]
            if not link or ':' in link or link.startswith('/'):
                continue
            assert (path.parent / link).exists(), f'broken local link in {path.name}: {link}'
        checks.append('LOCAL_LINKS:' + path.relative_to(ROOT).as_posix())
    public = [*targets, *sorted((ROOT / 'docs').rglob('*.json'))]
    deny = [r'C:\\Users\\', r'PRIVATE\.zip', r'BEGIN (?:RSA |OPENSSH )?PRIVATE KEY',
            r'gh[pousr]_[A-Za-z0-9]{30,}', r'sites\.google\.com/d/.+/edit', r'TODO_HASH', r'REPLACE_ME']
    for path in public:
        text = path.read_text(encoding='utf-8')
        for pattern in deny:
            assert not re.search(pattern, text), f'leak/placeholder gate: {path.name}'
    checks.append('SCOPED_PUBLIC_LEAK_AND_PLACEHOLDER_GATE')
    return checks
if __name__ == '__main__':
    checks = check()
    print(json.dumps({'status': 'PASS', 'checks': checks, 'count': len(checks)}, indent=2))
