import logging
from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    # Redirect HTTP(S) request to localhost
    flow.request.host = "localhost"
    logging.info(f"Redirecting request to {flow.request.host}:{flow.request.port}")
