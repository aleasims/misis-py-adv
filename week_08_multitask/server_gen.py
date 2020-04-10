"""
David Beazley
PyCon US 2015 "Python Concurrency From the Ground Up"
"""

import select
import socket

BUFSIZE = 4096

MSG = '''HTTP/1.1 200 OK
Content-Length: 13
Connection: Closed

Hello, world!
'''


tasks = []
to_read = {}
to_write = {}


def server():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind(('localhost', 8000))
    server_sock.listen()

    while True:

        yield ('read', server_sock)
        client_sock, addr = server_sock.accept()

        print(f'Connection from {addr}')
        tasks.append(serve_client(client_sock))


def serve_client(client_sock):
    while True:

        yield ('read', client_sock)
        request = client_sock.recv(BUFSIZE)

        if request:
            client_sock.sendall(MSG.encode())
        else:
            client_sock.close()
            break


def event_loop():
    while any([tasks, to_read, to_write]):

        while not tasks:
            ready_to_read, ready_to_write, _ = select.select(to_read,
                                                             to_write,
                                                             [])

            for sock in ready_to_read:
                tasks.append(to_read.pop(sock))

            for sock in ready_to_write:
                tasks.append(to_write.pop(sock))

        try:
            task = tasks.pop(0)

            method, sock = next(task)

            if method == 'read':
                to_read[sock] = task
            if method == 'write':
                to_write[sock] = task

        except StopIteration:
            pass


if __name__ == "__main__":
    tasks.append(server())
    event_loop()
