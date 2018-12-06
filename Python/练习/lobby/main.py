import sys
import thread
import time
from lobbyListener import lobby
from connectionDispatcher import connectionDispatcher

thread.start_new_thread(lobby, ())
thread.start_new_thread(connectionDispatcher, ())
time.sleep(1)
print ' > Threads has been started successfully.'
print ' > To stop this application type \'exit\' or \'die\'.'
while True:
    reader = raw_input('')
    if reader == 'die' or reader == 'exit':
        print( ' > Application exit')
        sys.exit()