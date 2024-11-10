import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind(('127.0.0.1', 65432))

# Start listening for incoming connections
server_socket.listen()

print("Server is listening on port 65432...")

# Accept a client connection
conn, addr = server_socket.accept()
print(f"Connected by: {addr}")

# Receive data from the client
data = conn.recv(1024)
if data:
    print(f"Received: {data.decode()}")

# Send data to the client
conn.sendall(b'Hello from server!')

# Close the connection
conn.close()
