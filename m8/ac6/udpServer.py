import socket

def main():
	host ='10.1.134.217'
	port =5000

	s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host,port))

	print("Server Started... ")
	while True:
		data, addr = s.recvfrom(1024)
		print("message from: " + str(addr))
		print("from connect user: "+ str(data))
		data= str(data.decode('ASCII')).upper()
		print("sending:  "+ str(data))
		s.sendto(str(data).encode('ASCII'),addr)
	s.close()

if __name__=='__main__':
	main()