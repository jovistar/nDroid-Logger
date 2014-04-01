#!/usr/bin/python

from twisted.internet.protocol import DatagramProtocol
from logmanager import LogManager

class NetManager(DatagramProtocol):
	def setLogManager(self, logManager):
		self.logManager = logManager

	def datagramReceived(self, data, (host, port)):
		self.logManager.extLog(data)
