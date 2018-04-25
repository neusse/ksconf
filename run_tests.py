#!/usr/bin/env python
# May eventually switch to some other mechanism (possibly nose) but for now this works

# Note:  TestLoader.discover() is new in Python 2.7 (won't work in 2.6, if we care)

import unittest
import os

# Because this script is run from the 'pre-commit' hooks, and some of these
# unittests do git automation, we need to purge all the "GIT_*" variables
for k in os.environ.keys():
    if k.startswith("GIT_"):
        del os.environ[k]

def run_all():
    loader = unittest.TestLoader()
    # Top-level "tests" directory, contains "test_*.py" scripts
    suite = loader.discover("tests")
    runner = unittest.TextTestRunner()
    results = runner.run(suite)
    if results.errors:
        return 2
    elif results.failures:
        return 1

if __name__ == "__main__":
    import sys
    sys.exit(run_all())
