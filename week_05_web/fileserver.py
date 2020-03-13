from http.server import HTTPServer, SimpleHTTPRequestHandler


class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        print('Request from {}:{}'.format(*self.client_address))
        return super().do_GET()


PORT = 8080
HOST = '127.0.0.1'

with HTTPServer((HOST, PORT), Handler) as httpd:
    print(f'Serving at {HOST}:{PORT}')
    httpd.serve_forever()
