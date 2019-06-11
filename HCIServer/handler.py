import json
import http.server
import urllib.parse

from data import get_data
from data import add_data


class HCIRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # API request for data
        print(2)
        if "/index.html" in self.path or "/" == self.path:
            print(1)
        if "/data/" in self.path or "/data?" in self.path:
            parsed_request = urllib.parse.urlparse(self.path)
            data = json.dumps(get_data(dict(urllib.parse.parse_qsl(parsed_request[4]))))
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(data.encode("utf-8"))
            return

        # Requesting a resource (html, js, css)
        if "/shared/" not in self.path:
            if '/' == self.path:
                self.path = "/index.html"

            if "Mobi" in self.headers['user-agent']:
                # Requested by a mobile device
                self.path = '/mobile%s' % self.path
            else:
                self.path = '/desktop%s' % self.path

        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        params = json.loads(body)

        if self.path  == '/register':
            print(123123)
            user_id = add_data(params)
            self.send_response(200)

            self.send_header('Content-type', 'text/html')
            try:
                self.end_headers()
            except:
                print('failed')
            self.wfile.write(bytes('Registration succsess!', "utf8"))
            return
        elif self.path  == '/login':
            user = get_data(params)
            if user == None:
                # Send headers
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                try:
                    self.end_headers()
                except:
                    print('failed')
                self.wfile.write(bytes('False', "utf8"))
                return
            # Send headers
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            try:
                self.end_headers()
            except:
                print('failed')
            self.wfile.write(bytes('loggedin', "utf8"))
            return

        add_data(params)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        try:
            self.end_headers()
        except:
            print('failed')
        self.wfile.write(bytes('added one recipe', "utf8"))
        return