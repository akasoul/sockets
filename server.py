import socket
import numpy as np
import sys
import struct
sock = socket.socket()
sock.bind(('', 9090))


while True:
    sock.listen(1)
    conn, addr = sock.accept()
    print('connected:', addr)
    npdata=np.zeros(shape=[3,2])
    for i in range(0,3):
        data=conn.recv(sys.getsizeof(float))
        if  data:
            #data2=np.frombuffer(data,dtype=np.uint8)
            print(type(data))
            msg=struct.unpack_from('d',
                              data)
            print(msg)
            conn.send(b'odne')

conn.close()