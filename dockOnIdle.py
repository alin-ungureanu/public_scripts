import time
import sys
from ctypes import *
#import win32api
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController

#   PREREQUISITES
# make sure you have set a destination beforehand
	
class LASTINPUTINFO(Structure):
	_fields_ = [
		('cbSize', c_uint),
		('dwTime', c_int),
	]
		
def getIdleTime():
	lastInputInfo = LASTINPUTINFO()
	lastInputInfo.cbSize = sizeof(lastInputInfo)
	if windll.user32.GetLastInputInfo(byref(lastInputInfo)):
		millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
		return millis / 1000.0
	else:
		return 0

#def getIdleTime():
#	return (win32api.GetTickCount() - win32api.GetLastInputInfo()) / 1000.0

def getWindowFocus():
	print("Getting the focus of the full screen window on the first display")
	mouse = MouseController()

	mouse.position = (400, 200)
	mouse.press(Button.left)
	time.sleep(0.2)
	mouse.release(Button.left)
	time.sleep(0.5)


def retrieveDrones():

	print("Retrieving drones to drone bay")
	keyboard = KeyboardController()
	with keyboard.pressed(Key.shift_l):
		keyboard.press('r')
		time.sleep(0.3)
		keyboard.release('r')
		time.sleep(10)

def stopMinerActivity():
	print("Stopping miner activity")
	keyboard = KeyboardController()
	keyboard.press(Key.f1)
	time.sleep(0.3)
	keyboard.release(Key.f1)
	time.sleep(1)
	keyboard.press(Key.f2)
	time.sleep(0.3)
	keyboard.release(Key.f2)
	time.sleep(1)

def activateAutoPilot():
	
	print("Activating Auto-Pilot")
	keyboard = KeyboardController()

	with keyboard.pressed(Key.ctrl_l):
		keyboard.press('s')
		time.sleep(0.2)
		keyboard.release('s')

timeoutValue = 3 * 60.0#2 minutes
		
while(True):
	idleTime = getIdleTime()
	print("running, idle time is " + str(idleTime) + " seconds")
	if (idleTime > timeoutValue):
		getWindowFocus()
		retrieveDrones()
		stopMinerActivity()
		activateAutoPilot()
		break
	time.sleep(5)
	
print("Exiting")
