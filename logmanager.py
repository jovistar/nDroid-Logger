#!/usr/bin/python

from datetime import *
import time
import os
import threading
import socket

class LogManager():
	def __init__(self, logMode, logFile):
		self.logFile = open(logFile, 'w')

		if logMode not in ['LOGONLY', 'LOGPRINT', 'PRINTONLY']:
			logMode = 'PRINTONLY'

		if logMode == 'LOGONLY':
			self.doLog = True
			self.doPrint = False
		if logMode == 'LOGPRINT':
			self.doLog = True
			self.doPrint = True
		if logMode == 'PRINTONLY':
			self.doLog = False
			self.doPrint = True

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

		if self.doPrint == True:
			print msg

		if self.doLog == True:
			self.logFile.write(msg + '\n')

		self.lock.release()

