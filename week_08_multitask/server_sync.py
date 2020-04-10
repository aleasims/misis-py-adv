import socket


server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_sock.bind(('localhost', 8000))
server_sock.listen()

BUFSIZE = 4096

MSG = '''HTTP/1.1 200 OK
Content-Length: 13
Connection: Closed

Hello, world!
'''


def accept_client(server_sock):
    client_sock, addr = server_sock.accept()
    print(f'Connection from {addr}')
    serve_client(client_sock)


def serve_client(client_sock):
    request = client_sock.recv(BUFSIZE)

    if request:
        client_sock.sendall(MSG.encode())
    else:
        client_sock.close()


def server_loop():
    while True:
        accept_client(server_sock)


if __name__ == "__main__":
    server_loop()
