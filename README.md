
# Secure Client-Server Application

## Overview
This is a simple client-server application that demonstrates secure communication using SSL/TLS encryption. The server authenticates users with a username and password, and upon successful authentication, provides system information to the client.

## Features
- Secure connection using SSL/TLS
- Basic authentication system
- System information retrieval (CPU, RAM, OS details)
- Cross-platform compatibility

## Requirements
- Python 3.6+
- Required Python packages:
  - `psutil` (for system information)
  - `socket` and `ssl` (built-in Python libraries)

Install requirements with:
```
pip install psutil
```

## Setup Instructions

### SSL Certificates
The project includes pre-generated SSL certificates:
- `certificate.pem`: SSL certificate
- `key.pem`: Private key

For production use, you should generate your own certificates.

### Authentication
The server uses a simple hardcoded dictionary of usernames and passwords:
- Username: `user3`, Password: `password3`

## Running the Application

### Start the Server
```
python python_server.py
```
The server will start listening on 0.0.0.0:12345

### Start the Client
```
python python_client.py
```
The client will connect to the server and prompt for authentication details.

## How It Works
1. The server starts and listens for incoming connections
2. When a client connects, the server establishes a secure SSL/TLS connection
3. The server prompts the client for a username and password
4. If authentication is successful, the server sends system information
5. The client displays the received information

## Security Notes
- The SSL implementation uses a self-signed certificate (for demonstration purposes)
- Passwords are stored in plaintext (not recommended for production)
- In a real-world application, you would want to implement more robust security measures

## Project Structure
- `python_server.py`: Server implementation
- `python_client.py`: Client implementation
- `certificate.pem`: SSL certificate
- `key.pem`: Private key for SSL
