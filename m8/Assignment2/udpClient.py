import socket


def main():
    host = '10.1.134.217'
    port = 4004


    server=('10.1.134.217',3999)

    s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))

    message = input("Enter message:  ")
    while message !='q':
        s.sendto(str(message).encode('ASCII'),server)
        data, addr = s.recvfrom(1024)
        print("Recieved from server: "+ data.decode('ASCII'))
        message = input("Enter another message: ")
    s.close()

if __name__=='__main__':
 main()