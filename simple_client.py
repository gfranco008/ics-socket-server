import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(('127.0.0.1', 65432))

# Send data to the server
client_socket.sendall(b'Hello from client!')

# Receive response from the server
data = client_socket.recv(1024)
print(f"Received: {data.decode()}")

# Close the connection
client_socket.close()
