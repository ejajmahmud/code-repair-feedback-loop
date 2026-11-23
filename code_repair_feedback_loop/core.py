"""Core Code Repair Feedback Loop implementation."""
import re
from typing import Tuple, Optional

class RepairAction:
    def __init__(self, repair_type: str, line_num: int, suggested_fix: str):
        self.repair_type = repair_type
        self.line_num = line_num
        self.suggested_fix = suggested_fix

class CodeRepairLoop:
    @staticmethod
    def diagnose_traceback(tb_text: str) -> Optional[RepairAction]:
        # NameError: name 'xyz' is not defined
        name_err = re.search(r"NameError:\s+name\s+'(\w+)'\s+is\s+not\s+defined", tb_text)
        if name_err:
            missing_sym = name_err.group(1)
            common_modules = {"json", "os", "sys", "time", "math", "re", "hashlib"}
            if missing_sym in common_modules:
                return RepairAction("missing_import", 1, f"import {missing_sym}")

        # IndentationError
        indent_err = re.search(r"IndentationError:.+?line\s+(\d+)", tb_text)
        if indent_err:
            return RepairAction("indentation", int(indent_err.group(1)), "Fix indentation to 4 spaces")

        return None
