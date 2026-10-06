# Information Gathering Tool 🔍

A simple, menu-driven Python script that automates four common **reconnaissance (OSINT / footprinting)** tasks against a single target domain or IP. It's the first phase of any penetration test.

> ⚠️ **Disclaimer:** For educational and authorised security testing only. Run it only against systems you own or have written permission to test. Unauthorised scanning or data collection may violate the Information Technology Act, 2000 (India) and computer-misuse laws in other countries. The author accepts no liability for misuse.

## Features

| Option | Module | How it works |
|---|---|---|
| 1 | **IP resolution** | Resolves the domain to its IPv4 address using `socket.gethostbyname()` |
| 2 | **Google dorking** | Opens a `site:<target> inurl:admin` search to find exposed admin pages |
| 3 | **DNS details** | Runs `nslookup` on the target to show its DNS records |
| 4 | **Emails & employees** | Builds `intext:@<target>` and `site:linkedin.com <target>` searches |
| 5 | **Exit** | Closes the tool |

## Requirements

- Python 3.8+
- `nslookup` available in your terminal (built into Windows, macOS and most Linux distros)
- A default web browser

Uses only the Python standard library (`socket`, `os`, `webbrowser`). **No `pip install` needed.**

## Usage

```bash
git clone https://github.com/nehanshughosh12345/Information-Gathering-Tool.git
cd Information-Gathering-Tool
python Information_Gathering_Tool.py
```

Example run against a public practice site:

```
Enter the domain or IP: testfire.net

1. Find IP of domain
2. Google dorking
3. DNS details
4. Emails and employee details
5. Exit
Enter your choice: 1
IP address: 65.61.137.117
```

## How it works

1. The target is entered **once** and reused by every option.
2. The menu runs inside a `while True` loop, so you can run several modules one after another.
3. Option 5 (`break`) is the only way out. Any invalid input reprints the menu.

## Limitations

- No error handling yet. An invalid domain raises an exception.
- `gethostbyname` returns only one IPv4 address.
- `nslookup` output is printed but not parsed or saved.

## Roadmap

- [ ] `try/except` error handling
- [ ] WHOIS lookup, subdomain enumeration and reverse DNS
- [ ] Replace `os.system` with `subprocess` and parse the records
- [ ] Export results to CSV / JSON / HTML report

## References

- [Python `socket` docs](https://docs.python.org/3/library/socket.html)
- [Python `webbrowser` docs](https://docs.python.org/3/library/webbrowser.html)
- [Google Hacking Database (GHDB)](https://www.exploit-db.com/google-hacking-database)
- [OWASP Web Security Testing Guide: Information Gathering](https://owasp.org/www-project-web-security-testing-guide/)

## Author

**Nehanshu B. Ghosh** · [LinkedIn](https://www.linkedin.com/in/nehanshughosh)
