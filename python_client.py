import socket
import ssl

def start_client():
    host = '0.0.0.0'  # Change to the server's IP address
    port = 12345

    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as secure_socket:
            print(f"Secure connection established with {host}")

            welcome_message = secure_socket.recv(1024).decode()
            print(welcome_message)

            username = input("Enter your username: ")
            secure_socket.send(username.encode())

            password_prompt = secure_socket.recv(1024).decode()
            print(password_prompt)

            password = input("Enter your password: ")
            secure_socket.send(password.encode())

            response = secure_socket.recv(1024).decode()
            print(response)

            if "successful" in response.lower():
                system_info = secure_socket.recv(1024).decode()
                print("System Information:", system_info)

if __name__ == "__main__":
    start_client()