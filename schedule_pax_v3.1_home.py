#! python2
import pyautogui
import time
from time import gmtime, strftime
from random import uniform
import string
import urllib2
from urllib2 import URLError
import os
import sys
import gc
#1920 X 1080 screen
#edit as you wish for other screen sizes

#enter time of bid
#lay back and relax
#all WT values are in seconds

#configurable session
_TARGET_TIME_ = [0, 27, 00]

_TEST_MODE_ = False
#_TEST_MODE_ = True



_GAME_RELOAD_WT_ = 60


_ACCOUNT_MAIL_="acct"
_ACCOUNT_PASS_="pwd"



#do not modify this section
_SCREEN_WIDTH_ = 1920
_SCREEN_HEIGHT_ = 1080

_100K_ = 100000

_H_ = 0
_M_ = 1
_S_ = 2

_MINIMUM_WT_ = 1

_STATE_CONTINUE_ = 'continue'
_STATE_PAUSE_ = 'pause'
_STATE_SHUTDOWN_ = 'shutdown'

pyautogui.FAILSAFE = False

def getTime():
	gmtTime = strftime("%H:%M:%S", gmtime())
	gmtList = string.split(gmtTime, ':')
	h = (int(gmtList[_H_]) + 3) % 24
	m = int(gmtList[_M_])
	s = int(gmtList[_S_])
	return [h, m, s]


def delay(wt):
	time.sleep(wt + _MINIMUM_WT_ + uniform(0, 1))

def click(wt=0.1):
	pyautogui.mouseDown()
	time.sleep(wt + uniform(0, 1))
	pyautogui.mouseUp()
	return


def removeInactivityScreen():
	pyautogui.moveTo(_SCREEN_WIDTH_ / 2, 710)
	click(0.5)
	delay(0.5)
	return

def enterCorporationTab():
	pyautogui.moveTo(_SCREEN_WIDTH_ / 2 + 15, 990)
	click(0.5)
	delay(0.5)
	return

def enterWorkerTab():
	enterCorporationTab()
	pyautogui.moveTo(_SCREEN_WIDTH_ / 2 + 175, 360)
	click(0.5)
	delay(0.5)
	return

def increaseWorkerBid(sum):
	bid = 0
	enterWorkerTab()
	pyautogui.moveTo(_SCREEN_WIDTH_ / 2 + 175, 760)
	
	while(bid < sum):
			click(0.05)
			if (bid < _100K_):
				bid = bid + 1000
			elif (bid < 250000):
				bid = bid + 5000
	time.sleep(0.01)
	return

def placeWorkerBid():
	enterWorkerTab()
	pyautogui.moveTo(_SCREEN_WIDTH_ / 2 + 320, 760)
	click(0.5)
	delay(0.5)
	return

def clickOnCenter():
	pyautogui.moveTo(_SCREEN_WIDTH_ / 2, _SCREEN_HEIGHT_ / 2)
	click(0.5)
	delay(0.9)
	return


def enterPlanningOffice():
	removeInactivityScreen()
	#move to Planning Office
	pyautogui.moveTo(1110, 1000)
	click()
	delay(1)
	return
	
def enterTimetableCalculator():
	enterPlanningOffice()
	#move to Timetable Calculator
	pyautogui.moveTo(1280, 386)
	click(1)
	delay(0.5)
	return
	
def selectTimetableCalculatorPax():
	enterTimetableCalculator()
	n = 1
	#to do: some clicks if needed on arrows (816, 476) (840, 476)
	#to do: some clicks if needed on arrows (816, 476) (840, 476) -> left right
	for i in range(0, n):
		#click left arrow
		delay(20)
		pyautogui.moveTo(816, 476)
		click(1)
	delay(10)
	return
	
def selectTimetableCalculatorBestRoute():
	pyautogui.moveTo(1003, 673)
	click(0.3)
	delay(0.3)
	click(0.2)
	delay(0.5)
	return

def clickOnTrainsList():
	pyautogui.moveTo(37, 1012)
	click()
	delay(0.5)
	return
	
def enterBestPaxTrainSchedule():
	#move to Timetable Calculator
	#trainLocationX = 242 hermes 2
	#trainLocationY = 670
	trainLocationX = 163
	#trainLocationY = 341 First pos
	#trainLocationX = 163
	trainLocationY = 341
	schedButtonX = 309
	schedButtonY = 413
	pyautogui.moveTo(trainLocationX, trainLocationY)
	click()
	delay(2)
	#click on schedule
	pyautogui.moveTo(schedButtonX, schedButtonY)
	click()
	delay(2)
	return

def setTourRetourBestPax():
	#increase pax load
	#For Kangaroo pyautogui.moveTo(1004, 921)
	#for Hades pyautogui.moveTo(987, 921)
	#for Hermes pyautogui.moveTo(913, 921)
	pyautogui.moveTo(913, 921)
	click(0.3)
	delay(0.3)
	click(0.3)
	delay(2)
	#center start city for current route
	pyautogui.moveTo(503, 810)
	click(0.5)
	delay(5.8)
	#set click on current route start city as destination for retour
	clickOnCenter()
	return
	
def adoptScheduleForAll():
	#click on Adopt Schedule
	pyautogui.moveTo(779, 1016)
	click(0.3)
	delay(1.7)
	#click on Select All
	pyautogui.moveTo(628, 768)
	click(0.2)
	delay(1.2)
	#click on confirm
	pyautogui.moveTo(1289, 768)
	if (_TEST_MODE_ != True):
		click(0.5)
	delay(3.2)
	
	return

def scheduleBestRoutePaxFromTimetableCalculator():
	#move to Planning Office
	selectTimetableCalculatorPax()
	selectTimetableCalculatorBestRoute()
	#schedule tour - retour route
	#open trains list
	#clickOnTrainsList()
	enterBestPaxTrainSchedule()
	delay(2)
	setTourRetourBestPax()
	adoptScheduleForAll()
	#close trains list
	clickOnTrainsList()
	return

def startGame():
	startOperaBrowser()
	delay(3);
	closeFirstBrowserTab()
	#click on address bar
	#pyautogui.moveTo(_SCREEN_WIDTH_ / 2 + 100, 48)
	#click(0.5)
	clickOnCenter()

	pyautogui.moveTo(_SCREEN_WIDTH_ / 2 + 100, 48)
	click(0.2)
	delay(0.2)
	pyautogui.typewrite('http://www.railnation.ro/home/', interval=0.03)
	#press enter
	pyautogui.press('enter')
	delay(3)
	#click on login button
	pyautogui.moveTo(550, 80)
	click(0.5)
	delay(3)
	#enter credentials if needed
	pyautogui.moveTo(960, 470)
	click(0.1)
	pyautogui.typewrite(_ACCOUNT_MAIL_, interval=0.03)
	pyautogui.moveTo(960, 570)
	click(0.1)
	pyautogui.typewrite(_ACCOUNT_PASS_, interval=0.03)
	pyautogui.moveTo(960, 615)
	click(0.1)
	delay(3)
	#click on continue with last game world button
	pyautogui.moveTo(1130, 427)
	click(0.5)
	delay(3)
	time.sleep(_GAME_RELOAD_WT_)

	return

#threeAM_Worker()
def clearWelcomeScreens():
	#clear welcome screen
	pyautogui.moveTo(1338, 331)
	click(0.5)
	delay(2)
	#clear potential offer screen
	#pyautogui.moveTo(1338, 1338)
	#click(0.5)
	#delay(2)
	#clear potential offer screen 2
	#pyautogui.moveTo(1338, 1338)
	#click(0.5)
	#delay(1)
	#close trains list
	#clickOnTrainsList()
	return


def closeFirstBrowserTab():
	pyautogui.moveTo(243, 13)
	click(0.5)
	return
	
def closeGame():
	closeFirstBrowserTab()
	closeOperaBrowser()
	gc.collect()
	return

def schedulePax():
	startGame()
	#clearWelcomeScreens()
	scheduleBestRoutePaxFromTimetableCalculator()
	closeGame()
	return

def lockScreen():
	#pyautogui.hotkey('win', 'l');
	pyautogui.moveTo(25, 1056)
	delay(1)
	click(0.1)
	
	pyautogui.moveTo(348, 1005)
	delay(1)
	click(0.5)
	
	pyautogui.moveTo(413, 953)
	delay(1)
	click(0.5)
	
	sys.exit()
	return
	
def startOperaBrowser():
	#select Opera browser as first from left to right from launch bar
	#os.system('"C:\\Program Files (x86)\\Opera\\launcher.exe"')
	os.system('"C:\\Program Files (x86)\\Opera\\launcher.exe"')
	delay(3)
	return

def closeOperaBrowser():
	pyautogui.moveTo(_SCREEN_WIDTH_ - 20, 5)
	click(0.3)
	return
	

def shutdownComputer():
	delay(60)
	os.system('shutdown /s /f /t 120')
	return
	
def schedulePaxLoop():

	while(True):
		currentTime = getTime()
		print currentTime
		if ((currentTime[_M_] == _TARGET_TIME_[_M_] and currentTime[_S_] > _TARGET_TIME_[_S_])):
			schedulePax()
			return
		time.sleep(20)

	return


#_TEST_MODE_ = True
if (_TEST_MODE_ != True):
	schedulePaxLoop()
else:
	schedulePax()
