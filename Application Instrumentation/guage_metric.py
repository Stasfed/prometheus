import http.server
import time
from prometheus_client import start_http_server, Gauge

REQUEST_IN_PROGRESS = Gauge('reuests_inprogress', "Number of Live Request on Application")

class HandleRequests(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        REQUEST_IN_PROGRESS.inc() 
        time.sleep(5)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>First python Application</title></head><body style='color: #333; margin-top: 30px;'><center><h2>Welcome to our first Python application.</center></h2></body></html>", "utf-8"))
        self.wfile.close
        REQUEST_IN_PROGRESS.dec() 

if __name__ == "__main__":
    start_http_server(5001)
    server = http.server.HTTPServer(('178.62.224.102', 5000), HandleRequests)
    server.serve_forever()