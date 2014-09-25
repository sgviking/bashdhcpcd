#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8
# vim:tabstop=4

from pydhcplib.dhcp_packet import *
from pydhcplib.dhcp_network import *

netopt = {'client_listen_port':"68",
           'server_listen_port':"67",
           'listen_address':"0.0.0.0"}

class Server(DhcpServer):
	def __init__(self, options):
		DhcpServer.__init__(self,options["listen_address"],
                            options["client_listen_port"],
                            options["server_listen_port"])

	def HandleDhcpDiscover(self, packet):
		print "discover"
		print packet.str()        
	def HandleDhcpRequest(self, packet):
		print "request"
		print packet.str()
	def HandleDhcpDecline(self, packet):
		print "decline"
		print packet.str()        
	def HandleDhcpRelease(self, packet):
		print "release"
		print packet.str()        
	def HandleDhcpInform(self, packet):
		print "inform"
		print packet.str()

if __name__ == "__main__":
	server = Server(netopt)

	while True :
		server.GetNextDhcpPacket()

