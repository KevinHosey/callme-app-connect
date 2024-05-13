import http.server
import requests
import json
import sys

from urllib.parse import urlparse, parse_qs

class HelloHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        # print("Received data:", post_data)
        sys.stdout.flush()

        try:
            data = json.loads(post_data.decode('utf-8'))
        except json.JSONDecodeError as e:
            print("Error decoding JSON:", e)
            self.send_response(400)
            self.end_headers()
            return

        if self.path == '/hello':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            print("Received data:", data)

    def query_callme_service():
        callme_url = "http://gibson.h4ck.me/echo"
        payload = {"url": "http://16.171.38.251/hello"}
        response = requests.post(callme_url, json=payload)
        callback_message = response.json()
        print("Callback message from CallMe service:", callback_message)
        return callback_message


def run(server_class=http.server.HTTPServer, handler_class=HelloHandler, port=8000):
    callback_message = HelloHandler.query_callme_service()
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
