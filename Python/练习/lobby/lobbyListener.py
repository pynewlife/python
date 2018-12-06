import socket
import sys
import threading
import time
import struct

TCP_HOST = ''
TCP_PORT = 10000  # port for listening to MH clients

serverID = 31
serstats = 1
sercount = 1


def lobby():
    try:
        tcps = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcps.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tcps.bind((TCP_HOST, TCP_PORT))
        tcps.listen(2)
        time.sleep(0.5)
        print ' > Lobby server up on port ' + str(TCP_PORT) + '.'
        while True:
            tcpc, tcpa = tcps.accept()
            print ' > [L] New connection from: ' + tcpa[0] + ':' + str(tcpa[1]) + '.'
            statusLock = threading.RLock()
            with statusLock:
                global serstats, serverID, sercount
                packet = [0x10, 0x00, 0x00, 0x00, #packetHeader
						sercount, 0x00, 0x00, 0x00, #every single line of this packet stands for an Int32 type
						serverID, 0x00, 0x00, 0x00, #what does it mean? well, if server count setted up at global variable is 1,
						serstats, 0x00, 0x00, 0x00] #and a byte after it is "0x01", then client would interprete it as 256 running servers.
                tcpc.sendall(struct.pack('B' * len(packet), *packet))
            tcpc.close()
    except socket.error as err:
        print ' > Failed to bind Lobby socket: ' + str(err[0]) + '.'
        sys.exit()