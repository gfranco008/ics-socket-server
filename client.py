import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(("127.0.0.1", 65432))

try:
    while True:
        # Get a message from the client user
        message = input("Enter your message: ")
        client_socket.sendall(message.encode())

        # End the connection if the client sends 'exit'
        if message.lower() == "exit":
            break

        # Receive response from the server
        data = client_socket.recv(1024)
        if not data:
            break  # Exit the loop if no data is received

        print(f"Server: {data.decode()}")
finally:
    # Close the connection
    client_socket.close()
    print("Connection closed.")
