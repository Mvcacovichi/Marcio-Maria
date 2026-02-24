import http.server
import socketserver
import webbrowser
from threading import Timer
import os

PORT = 8000

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def open_browser():
    webbrowser.open_new(f"http://localhost:{PORT}/")

if __name__ == "__main__":
    # Muda o diretório atual para a pasta do script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
        print(f"Servidor rodando na porta {PORT}...")
        print("Abrindo o navegador automaticamente...")
        Timer(1.5, open_browser).start()
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor encerrado.")
