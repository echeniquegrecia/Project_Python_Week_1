#!/usr/bin/env python3
from threading import Thread
import socket
from api import parse_request, HTTPResponse, format_response, HTTPStatus, HTTPDuplex
from configs import read_core_yml
from core.core import *

#To manage the requests and response 
def handle_request(conn, ip, port, addons_list):
    input = conn.recv(4096).decode('utf8').rstrip()
    if input:
        parsed_request = parse_request(input)
        duplex = HTTPDuplex()
        duplex.request = parsed_request
        duplex.socket = conn

        for addon in addons_list:
            testAddon = addon()
            testAddon.execute(duplex)
        
        if duplex.response:
            conn.send(duplex.response)
            conn.close()

        return parsed_request
    else:
        print('Error while parsing request')
        conn.close()


#Creation of socket to establish the TCP connection
class NetworkServer(object):
    def __init__(self,addons_list):  
        self.addons_list = addons_list
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print('Socket created')

        #get host and port from yml file
        core_dict = read_core_yml.start()
        host = core_dict.get('listening').get('host')
        port = core_dict.get('listening').get('port')

        self.conn.bind((host, port))
        self.conn.listen(2)
        print('Socket now listening')


    def start(self):
        while True:
            client_connection, client_address = self.conn.accept()
            ip, port = str(client_address[0]), str(client_address[1])
            print ('Serving HTTP on port %s ...' % port)

            #Thread lets to works handle with differents request at the same time
            Thread(target=handle_request, args=(client_connection, ip, port, self.addons_list)).start()