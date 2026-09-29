import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from training_pipeline import *

class TrainingPipelineTests(unittest.TestCase):
    def test_valid_module(self):
        m={"id":"T1","topic":"SOP","owner":"Ops","audience":"internal","steps":["draft","review"]}
        self.assertTrue(validate_module(m)["ok"])

    def test_missing_steps_holds(self):
        m={"id":"T1","topic":"SOP","owner":"Ops","audience":"internal"}
        self.assertIn("steps", validate_module(m)["missing"])

    def test_normalize_steps(self):
        self.assertEqual(normalize_steps([" A ","", "B"]), ["A","B"])

    def test_external_requires_review(self):
        self.assertTrue(review_required({"audience":"external"}))

    def test_policy_sensitive_requires_review(self):
        self.assertTrue(review_required({"audience":"internal","policy_sensitive":True}))

    def test_build_ready(self):
        m={"id":"T1","topic":"SOP","owner":"Ops","audience":"internal","steps":["draft"]}
        self.assertEqual(build_module(m)["status"], "READY")

    def test_build_waiting_review(self):
        m={"id":"T1","topic":"Client guide","owner":"Ops","audience":"external","steps":["draft"]}
        self.assertEqual(build_module(m)["status"], "WAITING_REVIEW")

    def test_plan_counts(self):
        mods=[
            {"id":"1","topic":"A","owner":"Ops","audience":"internal","steps":["x"]},
            {"id":"2","topic":"B","owner":"Ops","audience":"external","steps":["x"]},
            {"id":"3","topic":"C","owner":"Ops","audience":"internal"},
        ]
        p=build_plan(mods)
        self.assertEqual((p["ready"],p["waiting_review"],p["hold"]),(1,1,1))

    def test_completion_rate(self):
        self.assertEqual(completion_rate(3,4),75.0)

    def test_zero_total_is_none(self):
        self.assertIsNone(completion_rate(0,0))

if __name__ == "__main__":
    unittest.main()
