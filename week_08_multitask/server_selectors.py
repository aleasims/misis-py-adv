import socket
import selectors


selector = selectors.DefaultSelector()


def create_server():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind(('localhost', 8000))
    server_sock.listen()
    selector.register(server_sock, selectors.EVENT_READ, accept_client)


BUFSIZE = 4096

MSG = '''HTTP/1.1 200 OK
Content-Length: 13
Connection: Closed

Hello, world!
'''.encode()


def accept_client(server_sock: socket.socket):
    client_sock, addr = server_sock.accept()
    print(f'Connection from {addr}')
    selector.register(client_sock, selectors.EVENT_READ, serve_client)


def serve_client(client_sock: socket.socket):
    request = client_sock.recv(BUFSIZE)
    if request:
        client_sock.send(MSG)
    else:
        selector.unregister(client_sock)
        client_sock.close()


def event_loop():
    while True:
        events = selector.select()
        for key, _ in events:
            callback = key.data
            callback(key.fileobj)


if __name__ == "__main__":
    create_server()
    event_loop()
