import socket
import numpy as np


data=np.array([1.1,1.2,2.1,2.2,3.1,3.2])
#np.array2
sock = socket.socket()
sock.connect(('localhost', 9090))
for i in range(0,6):
    sock.send(data[i,])
    ans = sock.recv(1024)
    print(ans)
sock.close()

