import socket
import ssl
import platform
import psutil

def get_cpu_model():
    try:
        return platform.processor()
    except Exception as e:
        print(f"Error getting CPU model: {e}")
        return "Unknown"

def get_system_info():
    cpu_model = get_cpu_model()
    gpu_info = "GPU: [Not implemented in this example]"
    ram_info = f"RAM: {psutil.virtual_memory().total / (1024**3):.2f} GB"
    return f"CPU: {cpu_model}, {gpu_info}, {ram_info}, OS: {platform.system()} {platform.release()}"

def start_server():
    user_credentials = {
        'garv': 'garv',
        'divya': 'divya',
        'user3': 'password3',
    }

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '0.0.0.0'
    port = 12345

    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="C:\\Users\\Garv\\cn mini\\certificate.pem", keyfile="C:\\Users\\Garv\\cn mini\\key.pem")  # Adjust the path to your certificate and key

    server_socket.bind((host, port))
    server_socket.listen(5)
    server_socket = context.wrap_socket(server_socket, server_side=True)
    print(f"Server listening on {host}:{port} with SSL")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '0.0.0.0'
port = 12345

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="C:\\Users\\Garv\\cn mini\\certificate.pem", keyfile="C:\\Users\\Garv\\cn mini\\key.pem")  # Adjust the path to your certificate and key

server_socket.bind((host, port))
server_socket.listen(5)
server_socket = context.wrap_socket(server_socket, server_side=True)
print(f"Server listening on {host}:{port} with SSL")

while True:
    secure_socket, addr = server_socket.accept()
    print(f"Secure connection from {addr}")

    secure_socket.send("Welcome to the server! Please enter your username:".encode())
    username = secure_socket.recv(1024).decode().strip()

    username = secure_socket.recv(1024).decode().strip()

    if username in user_credentials:
            secure_socket.send("Enter your password:".encode())
            password = secure_socket.recv(1024).decode().strip()

            if password == user_credentials[username]:
                secure_socket.send("Login successful!".encode())
                system_info = get_system_info()
                secure_socket.send(system_info.encode())
            else:
                secure_socket.send("Incorrect password. Connection closed.".encode())
                secure_socket.close()
    else:
            secure_socket.send("Username not found. Connection closed.".encode())
            secure_socket.close()

if __name__ == "__main__":
    start_server()
