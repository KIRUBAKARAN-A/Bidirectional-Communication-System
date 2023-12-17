import socket
def server_program():
    host=socket.gethostname()
    port=8000
    server_socket=socket.socket()
    server_socket.bind((host,port))
    server_socket.listen(100)
    conn,address=server_socket.accept()
    while True:
        data=conn.recv(1000).decode()
        if not data:
            break
        print(data)
        data=input("Enter your message: ")
        conn.send(data.encode())
    conn.close()
if __name__=="__main__":
    server_program()

