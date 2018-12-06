import socket
import sys

TCP_HOST = ''
TCP_PORT = 10031
GAME_HOST = '127.0.0.1'
GAME_HHOST = '79.184.88.135'
GAME_PORT = '666'

connectionArray = bytearray(8)
connectionArray[0] = (8+len(GAME_HHOST)+len(GAME_PORT)+1)
connectionArray[4] = 0x17
connectionArray.extend((GAME_HHOST + ' ' + GAME_PORT))

connectionArrayz = bytearray(8)
connectionArrayz[0] = (8+len(GAME_HOST)+len(GAME_PORT)+1)
connectionArrayz[4] = 0x17
connectionArrayz.extend((GAME_HOST + ' ' + GAME_PORT))



def connectionDispatcher():
    try:
        tcps = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcps.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tcps.bind((TCP_HOST, TCP_PORT))
        tcps.listen(2)
        print ' > CDP server up on port ' + str(TCP_PORT) + '. Serves ' + GAME_HHOST + ':' + GAME_PORT + '.'
        while True:
            tcpc, tcpa = tcps.accept()
            print ' > [CDP] New connection from: ' + tcpa[0] + ':' + str(tcpa[1]) + '.'
            if tcpa[0] == '127.0.0.1':
                tcpc.sendall(connectionArrayz)
            else:
                tcpc.sendall(connectionArray)
            tcpc.close()

    except socket.error as err:
        print ' > Failed to bind CDP socket: ' + str(err[0]) + '.'
        sys.exit()