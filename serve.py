#!/usr/bin/env python3
"""Local preview server for the static site: python3 serve.py [port]"""
import http.server
import os
import socketserver
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 4173
os.chdir(os.path.dirname(os.path.abspath(__file__)))
socketserver.TCPServer.allow_reuse_address = True
print(f"Serving Runout Rank site on http://127.0.0.1:{PORT}")
socketserver.TCPServer(("127.0.0.1", PORT), http.server.SimpleHTTPRequestHandler).serve_forever()
