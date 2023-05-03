import socket
import sys

def main():
    host = socket.gethostname()
    print("Host name: " + str(host))

    if len(sys.argv) != 2:
        print("Usage: python server.py <port_number>")
        sys.exit()
    
    port = int(sys.argv[1])

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((host, port))

    server_socket.listen(2)

    while True:
        conn, address = server_socket.accept()
        print("Connection from: " + str(address))

        #data
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break

            print("From connected user: " + str(data))
            data = str(data).upper()
            conn.send(data.encode())
        
        conn.close()


if __name__ == "__main__":
    main()