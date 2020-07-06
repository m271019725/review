"""
tcp_client.py
"""
import socket

# 1.创建套接字
sock_fd = socket.socket()

# 2.请求连接

sock_fd.connect(('127.0.0.1', 8888))

while True:
    data = input("msg>>")
    if not data:
        break
    sock_fd.send(data.encode())
    data = sock_fd.recv(1024)
    print("server", data.decode())

sock_fd.close()
