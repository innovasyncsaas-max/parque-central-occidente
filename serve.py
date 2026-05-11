#!/usr/bin/env python3
"""Minimal HTTP server that forces text/html for all files without extension."""
from http.server import HTTPServer, SimpleHTTPRequestHandler
import mimetypes

class HTMLHandler(SimpleHTTPRequestHandler):
    def guess_type(self, path):
        mt, enc = mimetypes.guess_type(path)
        if mt is None:
            return 'text/html; charset=utf-8'
        return mt
    def log_message(self, fmt, *args):
        pass  # silent

if __name__ == '__main__':
    HTTPServer(('', 8081), HTMLHandler).serve_forever()
