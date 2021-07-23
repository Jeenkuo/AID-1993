"""
编写一个服务程序,编写一个服务端和一个客户端,
从客户端发送给服务端,
文件可以为一个文本也可以是二进制文件
"""
import socket
socket_object = socket.socket()
server_addr = ('127.0.0.1',8889)
socket_object.connect(server_addr)

"""
读取文件内容,发送给客户端
"""
file_object = open('../file_IO/xiaoze.jpeg','rb')

for line in file_object:
    socket_object.send(line)

file_object.close()
socket_object.close()