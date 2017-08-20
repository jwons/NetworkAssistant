'''
Created on Aug 20, 2017

@author: Wonsil
'''
from appJar import gui
import scheduleReader

if __name__ == '__main__':
    schedule = scheduleReader.scheduleReader()
    
    surveyInfo = "Network Support should survey " + schedule.getSurveyOfDay() + " today."
    closetInfo = "The " + schedule.getClosetOfDay() + " closet needs to be checked today"
    window = gui("Network Helper", "400x200")
    window.addLabel("Title", "Welcome Network Support Employee")
    window.setLabelBg("Title", "white")
    window.addLabel("surveyInfo", surveyInfo)
    window.setLabelBg("surveyInfo", "white")
    window.addLabel("closetInfo", closetInfo)
    window.setLabelBg("closetInfo", "white")
    window.go()
