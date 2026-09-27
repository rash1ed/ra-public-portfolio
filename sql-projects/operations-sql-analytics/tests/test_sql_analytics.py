from pathlib import Path
import sqlite3
import unittest

ROOT=Path(__file__).resolve().parents[1]

class SQLAnalyticsTests(unittest.TestCase):
    def setUp(self):
        self.db=sqlite3.connect(':memory:')
        self.db.executescript((ROOT/'schema.sql').read_text(encoding='utf-8'))
        self.db.executescript((ROOT/'seed.sql').read_text(encoding='utf-8'))

    def tearDown(self): self.db.close()

    def test_seed_counts(self):
        self.assertEqual(self.db.execute('select count(*) from teams').fetchone()[0],3)
        self.assertEqual(self.db.execute('select count(*) from agents').fetchone()[0],6)
        self.assertEqual(self.db.execute('select count(*) from tickets').fetchone()[0],72)

    def test_public_safe_agent_labels(self):
        labels=[r[0] for r in self.db.execute('select agent_code from agents')]
        self.assertEqual(labels,[f'Agent {c}' for c in 'ABCDEF'])

    def test_backlog_is_12(self):
        self.assertEqual(self.db.execute("select count(*) from tickets where status <> 'Resolved'").fetchone()[0],12)

    def test_resolved_have_resolution_time(self):
        bad=self.db.execute("select count(*) from tickets where status='Resolved' and resolved_at is null").fetchone()[0]
        self.assertEqual(bad,0)

    def test_all_queries_execute(self):
        for p in sorted((ROOT/'queries').glob('*.sql')):
            rows=self.db.execute(p.read_text(encoding='utf-8')).fetchall()
            self.assertTrue(rows, p.name)

    def test_executive_kpi_shape(self):
        row=self.db.execute((ROOT/'queries/01_executive_kpis.sql').read_text()).fetchone()
        self.assertEqual(row[0],72)
        self.assertEqual(row[1],60)
        self.assertEqual(row[2],12)
        self.assertGreaterEqual(row[3],0)
        self.assertLessEqual(row[3],100)

    def test_agent_rankings_unique_agents(self):
        rows=self.db.execute((ROOT/'queries/05_agent_rankings.sql').read_text()).fetchall()
        self.assertEqual(len(rows),6)
        self.assertEqual(len({r[0] for r in rows}),6)

    def test_no_sensitive_patterns(self):
        seed=(ROOT/'seed.sql').read_text(encoding='utf-8').lower()
        for token in ['@gmail.com','@outlook.com','password','secret','api_key','token=']:
            self.assertNotIn(token,seed)

if __name__=='__main__': unittest.main()
