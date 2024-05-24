from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class Server(DatagramProtocol):
    def __init__(self):
        self.clients = set()
    
    def datagramReceived(self, datagram, addr):
        datagram = datagram.decode("utf-8")
        if datagram == "ready":
            addresses = "\n".join([str(x) for x in self.clients])
            
            self.transport.write(addresses.encode('utf-8'), addr) # using generator for better list formatting
            self.clients.add(addr)
            
if __name__ == "__main__":
    reactor.listenUDP(9999, Server()) # every client on this server
    reactor.run()