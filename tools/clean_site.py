#!/usr/bin/env python3
"""Remove the rendered _site folder with retries.

On Windows, files copied from read-only sources (and freshly written files on
OneDrive-synced folders) can refuse deletion, which makes babelquarto's own
clean-up fail. Only the project's _site output folder is ever touched.
"""
import os
import shutil
import stat
import sys
import time
from pathlib import Path

root = Path(__file__).resolve().parent.parent
site = root / "_site"


def clear_readonly_and_retry(func, path, _exc_info):
    os.chmod(path, stat.S_IWRITE)
    func(path)


if not site.exists():
    print("clean_site: nothing to do")
    sys.exit(0)
for attempt in range(1, 11):
    try:
        shutil.rmtree(site, onerror=clear_readonly_and_retry)
        print(f"clean_site: removed {site} (attempt {attempt})")
        break
    except PermissionError as exc:
        print(f"clean_site: attempt {attempt} failed ({exc}); retrying")
        time.sleep(2)
else:
    print("clean_site: giving up")
    sys.exit(1)
