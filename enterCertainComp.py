#! python2
import pyautogui
import time
from time import gmtime, strftime
from random import uniform
import string
#1920 X 1080 screen

#configurable session
_TARGET_TIME_ = [94, 45, 0]



_GAME_RELOAD_WT_ = 60






#do not modify this section
_SCREEN_WIDTH_ = 1920
_SCREEN_HEIGHT_ = 1080

_H_ = 0
_M_ = 1
_S_ = 2

_MINIMUM_WT_ = 1

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

def enterComp():
	notEntered = True
	while(notEntered == True):
		currentTime = getTime()
		print currentTime
		if (currentTime[_M_] == _TARGET_TIME_[_M_] and currentTime[_S_] > _TARGET_TIME_[_S_]):
			notEntered = False
			removeInactivityScreen()
			#clear potential offer screen 2
			pyautogui.moveTo(983, 460)
			click(0.5)
			delay(0.6)
			click(0.5)
		time.sleep(5)
			
	return

enterComp()