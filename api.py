from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import urllib.parse

data = {}
id_counter = 1

class MyHandler(BaseHTTPRequestHandler):

    def _set_headers(self, status=200):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()

   
    def do_GET(self):
        self._set_headers()
        self.wfile.write(json.dumps(data).encode())

   
    def do_POST(self):
        global id_counter
        length = int(self.headers['Content-Length'])
        body = self.rfile.read(length)

        user = json.loads(body) 

        data[id_counter] = user

        response = {
            "message": "User created",
            "id": id_counter,
            "data": user
        }

        id_counter += 1

        self._set_headers(201)
        self.wfile.write(json.dumps(response).encode())

    
    def do_PUT(self):
        query = urllib.parse.urlparse(self.path).query
        user_id = int(query.split("=")[1])

        length = int(self.headers['Content-Length'])
        body = self.rfile.read(length)
        user = json.loads(body)

        if user_id in data:
            data[user_id] = user
            response = {"message": "Updated", "data": user}
            self._set_headers(200)
        else:
            response = {"error": "User not found"}
            self._set_headers(404)

        self.wfile.write(json.dumps(response).encode())

  
    def do_DELETE(self):
        query = urllib.parse.urlparse(self.path).query
        user_id = int(query.split("=")[1])

        if user_id in data:
            deleted = data.pop(user_id)
            response = {"message": "Deleted", "data": deleted}
            self._set_headers(200)
        else:
            response = {"error": "User not found"}
            self._set_headers(404)

        self.wfile.write(json.dumps(response).encode())


server = HTTPServer(('localhost', 5000), MyHandler)
print("Server running at http://localhost:5000")
server.serve_forever()
