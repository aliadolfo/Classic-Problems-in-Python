
if __name__=='__main__':

    import socket # Import Socket Module

    sock = socket.socket()  # Create a socket object
    host = socket.gethostname() # get a local machine name
    port = 12312

    sock.connect((host, port))
    sock.send(b"Hello Server")

    with open("Received_file", "wb") as out_file:
        print("file opened")
        print("receiving data....")
        while True:
            data = sock.recv(1024)
            print(f"data={data}")
            if not data:
                break
            out_file.write(data) # write data to a file 

    print("Successfully  got the file")
    sock.close()
    print("connection close")

