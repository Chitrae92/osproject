import socket
from random import randint
HOST, PORT = '', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(5)
print ('Serving HTTP on port %s ...' % PORT)
a = [randint(0,50) for x in range(11)]
b = [randint(100,500) for x in range(11)]
c = [randint(1000,5000) for x in range(11)]
print(a)

i = 0  # counter for selecting a
j = 0
k = 0
while True:
    client_connection, client_address = listen_socket.accept()
    
    while True:
        request = client_connection.recv(1024).decode()
        print(request)
        if request == "a":
            print(i)
            astr = a[i]
            http_response = str(astr)
            client_connection.sendall(http_response.encode())
            i += 1
        elif request == "b":
            print(j)
            bstr = b[j]
            http_response = str(bstr)
            client_connection.sendall(http_response.encode())
            j += 1
        elif request == "c":
            print(k)
            cstr = c[k]
            http_response = str(cstr)
            client_connection.sendall(http_response.encode())
            k += 1
        else:
            # client_connection.sendall("Q".encode())
            client_connection.close()
            i = 0
            j = 0
            k = 0
            break