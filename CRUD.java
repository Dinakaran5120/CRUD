import com.sun.net.httpserver.*;
import java.io.*;
import java.net.InetSocketAddress;
import java.util.*;

public class CRUD {

    static Map<Integer, String> data = new HashMap<>();
    static int idCounter = 1;

    public static void main(String[] args) throws Exception {

        HttpServer server = HttpServer.create(new InetSocketAddress(8080), 0);

        server.createContext("/users", exchange -> {
            String method = exchange.getRequestMethod();
            String response = "";

            if ("POST".equals(method)) {
                // CREATE
                String body = new String(exchange.getRequestBody().readAllBytes());
                data.put(idCounter, body);
                response = "User created with ID: " + idCounter;
                idCounter++;
            }

            else if ("GET".equals(method)) {
                // READ
                response = data.toString();
            }

            else if ("PUT".equals(method)) {
                // UPDATE
                String query = exchange.getRequestURI().getQuery(); // id=1
                int id = Integer.parseInt(query.split("=")[1]);

                if (data.containsKey(id)) {
                    String body = new String(exchange.getRequestBody().readAllBytes());
                    data.put(id, body);
                    response = "User updated";
                } else {
                    response = "User not found";
                }
            }

            else if ("DELETE".equals(method)) {
                // DELETE
                String query = exchange.getRequestURI().getQuery();
                int id = Integer.parseInt(query.split("=")[1]);

                if (data.remove(id) != null) {
                    response = "User deleted";
                } else {
                    response = "User not found";
                }
            }

            sendResponse(exchange, response);
        });

        server.start();
        System.out.println("Server running at http://localhost:8080/users");
    }

    static void sendResponse(HttpExchange exchange, String response) throws IOException {
        exchange.sendResponseHeaders(200, response.getBytes().length);
        OutputStream os = exchange.getResponseBody();
        os.write(response.getBytes());
        os.close();
    }
}
