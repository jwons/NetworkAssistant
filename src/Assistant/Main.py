'''
Created on Aug 20, 2017

@author: Wonsil
'''

from Tkinter import *
import ScheduleReader
import DailyLogResource
import MainWindow

if __name__ == '__main__':
    #Create a ScheduleReader object that will read in the closet and survey schedules so that
    #we can get them from it later
    schedule = ScheduleReader.ScheduleReader()
    
    with DailyLogResource.DailyLogResource() as dailyLog:
        root = Tk()
       
        window = MainWindow.MainWindow(root, dailyLog)
        
        root.mainloop()