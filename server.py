import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

def run_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("==================================================")
        print(f"[*] Local Web Server started successfully!")
        print(f"[*] Serving files from current directory...")
        print(f"[*] URL: http://localhost:{PORT}")
        print("==================================================")
        print("Press CTRL+C to shut down the server safely.\n")
        
        try:    
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[!] Server is shutting down...")

if __name__ == "__main__":
    run_server()