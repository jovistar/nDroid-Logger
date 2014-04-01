#!/usr/bin/python

from cnfmanager import CnfManager
from netmanager import NetManager
from logmanager import LogManager
from twisted.internet import reactor
import ndutil

def ndl_loop():
	ndutil.setTimezone()

	cnfManager = CnfManager()
	cnfManager.load('./ndl.cnf')
	cnfData = cnfManager.getCnfData()

	logManager = LogManager(cnfData['mode'], cnfData['logFile'])
	logManager.intLog('Iniatiating')

	netManager = NetManager()
	netManager.setLogManager(logManager)

	reactor.listenUDP(cnfData['port'], netManager)
	logManager.intLog('Listening Com Port')
	reactor.run()

if __name__ == '__main__':
	ndl_loop()

