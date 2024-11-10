import socket

from modbus import COMMAND_DICT, COMMANDS

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind(("127.0.0.1", 65432))

# Start listening for incoming connections
server_socket.listen()
print("Server is listening on port 65432...")

# Accept a client connection
conn, addr = server_socket.accept()
print(f"Connected by: {addr}")

try:
    # Get a response from the server user
    response = """Welcome to the ModBus Emulator
    ====================================
    
    If you want a list of commands type `help`

    What is your command?
    """
    conn.sendall(response.encode())

    while True:
        # Receive data from the client
        data = conn.recv(1024)
        if not data:
            break  # Exit the loop if no data is received

        print(f"Client: {data.decode()}")

        if data.decode() not in COMMANDS:
            response = f"""Command was not valid!
            Use one of the following:
            {COMMANDS}"""
            conn.sendall(response.encode())

        else:
            response = COMMAND_DICT.get(data.decode())
            conn.sendall(response.encode())

        # End the connection if the server sends 'exit'
        if response.lower() == "exit":
            break
finally:
    # Close the connection
    conn.close()
    print("Connection closed.")
