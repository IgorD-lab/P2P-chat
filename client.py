from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from random import randint

class Clinet(DatagramProtocol):
    def __init__(self, host, port):
        # Twisted ip recognition fix
        if host == "localhost":
            host = "127.0.0.1"
        
        self.id = host, port
        self.adress = None
        print("Working on id:", self.id)
    
    def datagramReceived(self, data, addr):
        print(addr, ":", datagram)
        
    def send_message(self):
        while True:
            self.transport.write(input(":::").encode('utf-8'), self.adress)

if __name__ == "__main__":
    # Simulate multiple clients on multiple ports with random
    port = (randint(1000, 5000))
    reactor.listenUDP(port, Client('localhost', port))
    reactor.run()