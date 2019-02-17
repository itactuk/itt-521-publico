import time
from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = ''
PUERTO = 8000


class MiHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        paths = {
            '/bien': {'status': 200},
            '/movido': {'status': 302},
            '/noencontro': {'status': 404},
            '/errorservidor': {'status': 500}
        }

        if self.path in paths:
            self.responder(paths[self.path])
        else:
            self.responder({'status': 500})

    def handle_http(self, status_code, path):
        self.send_response(status_code)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        content = '''
        <html><head><title>El título va aquí</title></head>
        <body><p>Este es un ejemplo</p>
        <p>Accediste al recurso: {}</p>
        </body></html>
        '''.format(path)
        return bytes(content, 'UTF-8')

    def responder(self, opts):
        status_code = opts['status']
        path = self.path
        self.send_response(status_code)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        content = '''
        <html><head><title>El título va aquí</title></head>
        <body><p>Este es un ejemplo</p>
        <p>Accediste al recurso: {}</p>
        </body></html>
        '''.format(path)
        response = bytes(content, 'UTF-8')
        self.wfile.write(response)

if __name__ == '__main__':
    httpd = HTTPServer((HOST, PUERTO), MiHandler)
    print(time.asctime(), 'El servidor inició en %s:%s' % (HOST, PUERTO))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), 'El servidor se detuvo - %s:%s' % (HOST, PUERTO))
