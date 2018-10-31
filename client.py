import socket
import numpy as np


data=np.array([65535.1213,100.7867,2000.5545])
#np.array2
sock = socket.socket()
sock.connect(('localhost', 9090))
for i in range(0,3):
    sock.send(data[i,])
    ans = sock.recv(1024)
    print(ans)
sock.close()

