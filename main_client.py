'''
Created on Nov 10, 2013

@author: Rex
'''

from client.startup_window import StartupGui   

if __name__ == '__main__':
    f = open('serverinfo', 'r')
    temp = f.readline().strip().split()
    ip = temp[0]
    temp = f.readline().strip().split()
    port = int(temp[0])
    start = StartupGui(ip, port)
    #input()
