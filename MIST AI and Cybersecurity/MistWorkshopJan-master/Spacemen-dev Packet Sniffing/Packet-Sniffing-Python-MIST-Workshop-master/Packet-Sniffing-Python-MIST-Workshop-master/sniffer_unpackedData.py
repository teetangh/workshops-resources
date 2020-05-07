import socket
import struct
def receiveData(s):
    data = ''
    try:
        data = s.recvfrom(65565)#Biggest length we can get
    except timeout:
        data = ''
    except:
        print("Error!")
        sys.exc_info()#imported from sys 
    return data[0]
# the public network interface
HOST = socket.gethostbyname(socket.gethostname())

# create a raw socket and bind it to the public interface
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
s.bind((HOST, 0))

# Include IP headers
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# receive all packages
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

data = receiveData(s)
unpackedData = struct.unpack('!BBHHHBBH4s4s', data[:20])
print("Unpacked Data is  : "+str(unpackedData))
# disabled promiscuous mode
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)