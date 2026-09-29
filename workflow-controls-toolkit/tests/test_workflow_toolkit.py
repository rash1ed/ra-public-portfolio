import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from workflow_toolkit import *

RULES = [
    {"category":"reporting","priority":"high","queue":"EXECUTIVE_REPORTING"},
    {"category":"*","priority":"high","queue":"PRIORITY_OPERATIONS"},
    {"category":"*","priority":"*","queue":"STANDARD_OPERATIONS"},
]

class WorkflowToolkitTests(unittest.TestCase):
    def test_validation_passes(self):
        self.assertTrue(validate_item({"id":"1","category":"reporting","priority":"high"})["ok"])

    def test_validation_holds_missing(self):
        self.assertIn("priority", validate_item({"id":"1","category":"reporting"})["missing"])

    def test_specific_route(self):
        self.assertEqual(route_item({"category":"reporting","priority":"high"}, RULES), "EXECUTIVE_REPORTING")

    def test_priority_route(self):
        self.assertEqual(route_item({"category":"service","priority":"high"}, RULES), "PRIORITY_OPERATIONS")

    def test_default_route(self):
        self.assertEqual(route_item({"category":"service","priority":"low"}, RULES), "STANDARD_OPERATIONS")

    def test_fan_out(self):
        self.assertEqual(len(fan_out({"id":"X","actions":["check","report","archive"]})), 3)

    def test_approval_gate(self):
        self.assertTrue(approval_required({"amount":12000}))

    def test_retry_cap(self):
        self.assertEqual(retry_delay_seconds(8), 1800)

    def test_workflow_ready(self):
        self.assertEqual(run_workflow({"id":"1","category":"service","priority":"low"}, RULES)["status"], "READY")

    def test_workflow_waiting_approval(self):
        self.assertEqual(run_workflow({"id":"1","category":"service","priority":"low","high_risk":True}, RULES)["status"], "WAITING_APPROVAL")

if __name__ == "__main__":
    unittest.main()
