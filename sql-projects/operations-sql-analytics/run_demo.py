from pathlib import Path
import sqlite3
ROOT=Path(__file__).resolve().parent
conn=sqlite3.connect(':memory:')
conn.executescript((ROOT/'schema.sql').read_text(encoding='utf-8'))
conn.executescript((ROOT/'seed.sql').read_text(encoding='utf-8'))
parts=['# RA Operations SQL Analytics — Verified Demo Results','', 'Synthetic data only. SQLite standard library execution.','']
for p in sorted((ROOT/'queries').glob('*.sql')):
    cur=conn.execute(p.read_text(encoding='utf-8'))
    cols=[d[0] for d in cur.description]
    rows=cur.fetchall()
    parts += [f'## {p.stem}', '', '| '+' | '.join(cols)+' |', '|'+ '|'.join(['---']*len(cols))+'|']
    for row in rows:
        parts.append('| '+' | '.join('' if v is None else str(v) for v in row)+' |')
    parts.append('')
(ROOT/'docs/results.md').write_text('\n'.join(parts)+'\n',encoding='utf-8')
print('\n'.join(parts))
