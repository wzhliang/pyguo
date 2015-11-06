from SimpleHTTPServer import SimpleHTTPRequestHandler
import SocketServer
import qrcode
import sys


class MyHandler(SimpleHTTPRequestHandler):
    def spit(self):
        addr, port = self.request.getsockname()
        qr = qrcode.QRCode()
        qr.add_data("http://{0}{1}{2}".format(addr, port, self.path))
        qr.print_ascii(tty=True)

    def do_GET(self):
        if 'Referer' not in self.headers:
            self.spit()
        return SimpleHTTPRequestHandler.do_GET(self)


port = int(sys.argv[1])
Handler = MyHandler
httpd = SocketServer.TCPServer(("", port), Handler)

print "Serving at port", port
print "Pressing enter on browser location bar will display a QR code"
httpd.serve_forever()
