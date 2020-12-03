#!/usr/bin/env python3

import socket
from redis import Redis

cli = Redis('localhost')

HOST = '172.16.17.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            str_temp = data.decode()
            cli.set('shared_temp', str_temp)
            print(str_temp)
