import socket
socket_object = socket.socket()
socket_object.bind(('127.0.0.1',8889))
socket_object.listen()

print("Waiting for connect...")
connect_object,addr = socket_object.accept()#该函数有两个返回值
print("Connect from",addr)

"""
思路:先recv()接收内容,再write()写入一个文件中
"""
file_object = open("1111.jpeg", 'wb')
while True:
    data = connect_object.recv(1024)
    if not data:
        break#网络无法发送空,客户端断开时break
    file_object.write(data)

file_object.close()
socket_object.close()