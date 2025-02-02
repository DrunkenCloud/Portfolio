from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

class NoCacheHTTPRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

if __name__ == '__main__':
    os.chdir('.')
    server_address = ('', 3000)
    httpd = HTTPServer(server_address, NoCacheHTTPRequestHandler)
    print("Serving on port 3000...")
    httpd.serve_forever()
