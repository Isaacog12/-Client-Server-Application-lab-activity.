import socket

def start_client(host='127.0.0.1', port=65432):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    try:
        while True:
            message = input("Enter message to send (type 'exit' to close): ")
            if message.lower() == 'exit':
                break
            client_socket.sendall(message.encode('utf-8'))
            response = client_socket.recv(1024).decode('utf-8')
            print(f"Received from server: {response}")
    except ConnectionAbortedError:
        print("Connection closed by server.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()
