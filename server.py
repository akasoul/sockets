import socket
import numpy as np
import sys
import struct
sock = socket.socket()
sock.bind(('', 9090))

_array=np.empty(shape=[3,2],dtype=np.float)
while True:
    sock.listen(1)
    conn, addr = sock.accept()
    print('connected:', addr)
    npdata=np.zeros(shape=[3,2])
    for i in range(0,3):
        for j in range(0,2):
            data=conn.recv(sys.getsizeof(float))
            if  data:
                print(type(data))
                msg=struct.unpack_from('d',
                                  data)
                print(msg)

                _array[i][j]=msg[0]
                conn.send(b'odne')
    print(_array)

conn.close()