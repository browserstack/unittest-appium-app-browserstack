# unittest + Appium with BrowserStack App Automate

Run Python `unittest` Appium tests on real mobile devices in the BrowserStack
device cloud, instrumented automatically by the **BrowserStack SDK**. No changes
to your test logic are required — the SDK reads `browserstack.yml`, uploads/uses
the app under test, and creates one App Automate session per platform.

This sample contains two self-contained platform directories:

```
unittest-appium/
├── android/   # WikipediaSample.apk — search flow
│   ├── browserstack.yml
│   ├── bstack_runner.py
│   ├── requirements.txt
│   └── tests/bstack_sample_test.py
└── ios/       # BStackSampleApp.ipa — text-echo flow
    ├── browserstack.yml
    ├── bstack_runner.py
    ├── requirements.txt
    └── tests/bstack_sample_test.py
```

## Prerequisites

- A [BrowserStack App Automate](https://app-automate.browserstack.com/) account.
- Python 3.8+.
- Your `BROWSERSTACK_USERNAME` and `BROWSERSTACK_ACCESS_KEY`
  (from your [account settings](https://www.browserstack.com/accounts/settings)).

## Setup

```bash
git clone <this-repo>
cd unittest-appium-app-browserstack/android        # or cd unittest-appium-app-browserstack/ios

python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

Configure credentials either in `browserstack.yml` (`userName` / `accessKey`)
or as environment variables (recommended):

```bash
export BROWSERSTACK_USERNAME="YOUR_USERNAME"
export BROWSERSTACK_ACCESS_KEY="YOUR_ACCESS_KEY"
```

The app under test is referenced in `browserstack.yml` via the `app:` key as a
pre-uploaded `bs://<hashed-id>`. To use your own build, upload it first:

```bash
curl -u "$BROWSERSTACK_USERNAME:$BROWSERSTACK_ACCESS_KEY" \
  -X POST "https://api-cloud.browserstack.com/app-automate/upload" \
  -F "file=@WikipediaSample.apk"
# then set app: bs://<app_url> in browserstack.yml
```

## Run Sample Test

From inside the platform directory:

```bash
cd android
browserstack-sdk python bstack_runner.py
```

`bstack_runner.py` discovers and runs the `unittest` suite under `tests/`. The
SDK forks one process per platform in `browserstack.yml`, opening one App
Automate session per device.

- **Android** (`WikipediaSample.apk`): taps **Search Wikipedia**, types
  `BrowserStack`, and asserts that search-result `TextView`s are shown.
- **iOS** (`BStackSampleApp.ipa`): taps **Text Button**, types
  `hello@browserstack.com`, and asserts the echoed **Text Output**.

## Notes / Dashboard

- View runs at [app-automate.browserstack.com](https://app-automate.browserstack.com/).
- With `testObservability: true`, builds also appear in
  [Test Observability](https://observability.browserstack.com/).
- Device, OS, and app capabilities all come from `browserstack.yml` — the Appium
  driver is created with an **empty options object**; the SDK injects the rest.
