#!/usr/bin/python

from datetime import *
import time
import os
import threading
import socket

class LogManager():
	def __init__(self, logMode, logFile):
		self.logFile = open(logFile, 'w')

		if logMode in ['LOGONLY', 'LOGPRINT']:
			if logMode == 'LOGONLY':
				self.logPrint = False
			elif logMode == 'LOGPRINT':
				self.logPrint = True
		else:
			self.logPrint = False

		#multithread
		self.lock = threading.Lock()

	def extLog(self, msg):
		curTime = datetime.now()

		finalMsg = '[MSG] ' + curTime.strftime('%Y-%m-%d %H:%M:%S') + ' %s' % msg
		self.writeLog(finalMsg)


	def intLog(self, msg):
		curTime = datetime.now()

		finalMsg = '[MSG] ' + curTime.strftime('%Y-%m-%d %H:%M:%S') + ' nDroid-Logger : %s' % msg
		self.writeLog(finalMsg)


	def writeLog(self, msg):
		self.lock.acquire()

		if self.logPrint:
			print msg

		self.logFile.write(msg + '\n')
		self.lock.release()

