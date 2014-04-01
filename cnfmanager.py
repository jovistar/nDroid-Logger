#!/usr/bin/python

import ConfigParser
import os

class CnfManager():
	def load(self, cnfFile):
		if not os.path.isfile(cnfFile):
			cnfFile = './ndl.cnf'

		cf = ConfigParser.ConfigParser()
		cf.read(cnfFile)

		self.cnfData = {}
		self.cnfData['mode'] = cf.get('common', 'mode')
		self.cnfData['logFile'] = cf.get('common', 'logFile')
		self.cnfData['port'] = int(cf.get('com', 'port'))

	def getCnfData(self):
		return self.cnfData
