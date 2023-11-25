# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import sys

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>Este é um exemplo de um servidor web .</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <port>")
        sys.exit(1)

    port = int(sys.argv[1])

    webServer = HTTPServer(("localhost", port), MyServer)
    print(f"Server started http://localhost:{port}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
