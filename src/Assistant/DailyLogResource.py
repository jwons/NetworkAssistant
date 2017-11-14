'''
Created on Sep 28, 2017

@author: Wonsil
'''

import csv
import datetime
import os
from cgi import logfile

class DailyLogResource(object):
    def __enter__(self):
        class DailyLog(object):
    
            def __init__(self):
                #Get the current time and date
                today = datetime.datetime.now()
                self.dayOfTheMonth = datetime.datetime.today().day
    
                #create a dict that will hold the information from the log
                self.monthlyLog = []
            
                self.currentEntry = []
                self.currentEntry.append(self.dayOfTheMonth)
            
                self.filename = today.strftime("%B") + "_" + today.strftime("%Y") + ".csv"
            
                if not os.path.exists(self.filename):
                    file(self.filename, 'w').close()
                else:
                    with open(self.filename, 'rU') as logFile:
                        logReader = csv.reader(logFile)
                        for row in logReader:
                            tempArr = []
                            for element in row:
                                tempArr.append(element)
                            self.monthlyLog.append(tempArr)
                        
                    logFile.close()
                
                while (len(self.monthlyLog) < self.dayOfTheMonth - 1):
                    self.monthlyLog.append([len(self.monthlyLog) + 1])
        
            def addEntry(self,name,building):
                self.currentEntry.append(name)
                self.currentEntry.append(building)
                
            def writeOut(self):
                #There will either be one(3 entries) or two surveys done (5 entries)
                if len(self.currentEntry) == 3:
                    if len(self.monthlyLog) != self.dayOfTheMonth:
                        while len(self.monthlyLog) < self.dayOfTheMonth:
                            self.monthlyLog.append([])
                    self.monthlyLog[self.dayOfTheMonth - 1] = [self.currentEntry[0], self.currentEntry[1], self.currentEntry[2], "", ""]
                if len(self.currentEntry) == 5:
                    if len(self.monthlyLog) != self.dayOfTheMonth:
                        while len(self.monthlyLog) < self.dayOfTheMonth:
                            self.monthlyLog.append([])
                    self.monthlyLog[self.dayOfTheMonth - 1] = [self.currentEntry[0],
                                                           self.currentEntry[1],
                                                           self.currentEntry[2],
                                                           self.currentEntry[3],
                                                           self.currentEntry[4]]
    
                with open (self.filename, 'wb') as logFile:
                    logWriter = csv.writer(logFile, delimiter =',')
                    logWriter.writerows(self.monthlyLog)
                        
        self.dailyLogObj = DailyLog()
        return self.dailyLogObj
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.dailyLogObj.writeOut()
        