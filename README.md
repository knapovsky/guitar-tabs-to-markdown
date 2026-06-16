# Guitar Tabs to Markdown

A Selenium-based helper script for downloading favourite tabs from Ultimate Guitar and saving them as Markdown-friendly text.

> Status: personal automation script.
>
> Websites change frequently. The CSS selectors in this script may be outdated.

## What it does

`download_my_favs.py` logs into Ultimate Guitar, opens the user's saved tabs page, collects track links, opens each tab, and attempts to extract the tab text from the page.

The original intent was to turn favourite guitar tabs/chords into Markdown notes for personal use.

## Requirements

- Python 3
- Selenium
- Firefox
- geckodriver available in `PATH` or in the repository root

Install Python dependency:

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install selenium
```

Install geckodriver on macOS:

```bash
brew install geckodriver
```

## Configuration

Edit the placeholder credentials in `download_my_favs.py` before running:

```python
username = 'username'
password = 'password'
```

Do not commit real credentials. Prefer loading them from environment variables if you modernise the script.

## Usage

```bash
python3 download_my_favs.py
```

## Maintenance notes

The script uses old Selenium APIs and page-specific CSS selectors. If it is revived, update it to:

- Selenium 4 APIs
- environment variables for credentials
- explicit waits for dynamic content
- configurable output directory
- robust Markdown file naming
- rate limiting and terms-of-service review

## Legal note

Tabs and lyrics may be copyrighted. Use downloaded material only in ways permitted by the source site and applicable law.

## License

No explicit license is included. Treat the code as all rights reserved unless a license is added by the repository owner.
