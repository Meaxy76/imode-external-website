# Version 1.0 
# It will be changed and improved
# I havent tested further yet
#!/usr/bin/env python3

import os
import sys

APP_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_FILE = os.path.join(APP_DIR, "index.htm")

try:
    with open(INDEX_FILE, "rb") as page_file:
        page = page_file.read()
except OSError:
    page = b"index.htm not found\r\n"
    status = b"Status: 500 Internal Server Error\r\n"
    content_type = b"Content-Type: text/plain; charset=US-ASCII\r\n"
else:
    status = b"Status: 200 OK\r\n"
    content_type = b"Content-Type: text/html; charset=Shift_JIS\r\n"

headers = (
    status
    + content_type
    + b"Cache-Control: no-cache\r\n"
    + b"Content-Length: " + str(len(page)).encode("ascii") + b"\r\n"
    + b"\r\n"
)

sys.stdout.buffer.write(headers)
sys.stdout.buffer.write(page)
