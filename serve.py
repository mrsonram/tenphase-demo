#!/usr/bin/env python3
"""Lightweight local HTTP server for the TENPHASE VILLAIN client pitch demo."""

import functools
import http.server
import os
import socketserver
import sys


class QuietNoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Referrer-Policy", "strict-origin-when-cross-origin")
        super().end_headers()

    def log_message(self, fmt, *args):
        sys.stderr.write(f"[tenphase-demo] {fmt % args}\n")


class ReusableThreadingServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True


def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    handler = functools.partial(QuietNoCacheHandler, directory=root_dir)

    server = None
    bound_port = None
    for port in range(4173, 4186):
        try:
            server = ReusableThreadingServer(("127.0.0.1", port), handler)
            bound_port = port
            break
        except OSError:
            continue

    if server is None or bound_port is None:
        print("ERROR: Could not bind any port in range 4173..4185", file=sys.stderr, flush=True)
        sys.exit(1)

    print(f"TENPHASE_DEMO_URL=http://localhost:{bound_port}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
