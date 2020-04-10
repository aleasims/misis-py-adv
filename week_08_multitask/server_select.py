import socket
import select


server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_sock.bind(('localhost', 8000))
server_sock.listen()

sockets = []
sockets.append(server_sock)

BUFSIZE = 4096

MSG = '''HTTP/1.1 200 OK
Content-Length: 13
Connection: Closed

Hello, world!
'''


def accept_client(server_sock):
    client_sock, addr = server_sock.accept()
    sockets.append(client_sock)
    print(f'Connection from {addr}')


def serve_client(client_sock):
    request = client_sock.recv(BUFSIZE)

    if request:
        client_sock.sendall(MSG.encode())
    else:
        client_sock.close()
        sockets.remove(client_sock)


def event_loop():
    while True:
        ready_to_read, _, _ = select.select(sockets, [], [])

        for sock in ready_to_read:
            if sock is server_sock:
                accept_client(sock)
            else:
                serve_client(sock)


if __name__ == "__main__":
    event_loop()
