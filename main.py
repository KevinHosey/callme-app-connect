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
            print("Received data:", data)

            # Query the CallMe service
            callme_url = 'http://gibson.h4ck.me/echo'
                
            # callback_url = 'http://{}:{}/hello'.format(self.server.server_address[0], self.server.server_address[1])
            # payload = {'url': callback_url}
            # response = requests.post(callme_url, json=payload)

            if response.status_code == 200:
                print("Callback successful.")
            else:
                print("Callback failed. Status code:", response.status_code)
            
            # Send response
           #  self.send_response(200)
           #  self.end_headers()
           #  self.wfile.write(json.dumps({"message": "Received and processed"}).encode('utf-8'))
        # else:
           #  self.send_response(404)
           #  self.end_headers()

def run(server_class=http.server.HTTPServer, handler_class=HelloHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
