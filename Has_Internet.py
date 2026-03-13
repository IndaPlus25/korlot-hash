import sys

class House:
    
    def __init__(self):
        self.internet = False
        self.connecting = []

    def has_internet(self):
        self.internet = True
    
    def set_connection(self, corded):
        self.connecting.append(corded)
        


data = sys.stdin.read().split()

if data[0].len() < 2