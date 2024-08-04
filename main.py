from http.server import SimpleHTTPRequestHandler, HTTPServer

class NoCacheHTTPRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add cache control headers
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

if __name__ == '__main__':
    # Set the server address and port
    server_address = ('', 3000)  # Change port if needed
    httpd = HTTPServer(server_address, NoCacheHTTPRequestHandler)
    print(f"Serving on http://localhost:{server_address[1]}")
    httpd.serve_forever()