"""Tests for CodeRepairLoop."""
import unittest
from code_repair_feedback_loop.core import CodeRepairLoop

class TestCodeRepairLoop(unittest.TestCase):
    def test_missing_import_diagnosis(self):
        tb = "NameError: name 'json' is not defined"
        act = CodeRepairLoop.diagnose_traceback(tb)
        self.assertIsNotNone(act)
        self.assertEqual(act.suggested_fix, "import json")
