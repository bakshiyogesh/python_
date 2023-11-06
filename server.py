import socket
CHUNK=65535
port=3000
#create a socket object
#socket.socket(family,type)
#AF_INET: family of IpV4 for ip address
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#SOCK_DGRAM for udp
#SOCK_STREAM for tcp
hostname='127.0.0.1'
s.bind((hostname,port))
print(f"server is running on {s.getsockname()}")

while True:
    data,clientAddress=s.recvfrom(CHUNK)
    message=data.decode('ascii') #data by default travels un bytes
    print(f"Apporava at {clientAddress} Says:{message}")
    message_send=input("Reply:")
    data=message_send.encode('ascii')
    s.sendto(data,clientAddress)