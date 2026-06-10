import unittest

# Entry point for the BrowserStack SDK generic-Python runner:
#   browserstack-sdk python bstack_runner.py
# The SDK forks one process per platform listed in browserstack.yml and runs
# the discovered unittest suite in each (one BrowserStack App Automate session
# per platform). The app under test (BStackSampleApp.ipa) is injected from the
# `app:` key in browserstack.yml.
if __name__ == "__main__":
    suite = unittest.TestLoader().discover("tests", pattern="bstack_*_test.py")
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if not result.wasSuccessful():
        raise SystemExit(1)
