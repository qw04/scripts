from pynput.keyboard import Key, Controller
import time
import random
import sys

keyboard = Controller()



def main():
	timeToSleep = int(sys.argv[1])
	time.sleep(2)
	while True:
		keyboard.press(Key.alt)
		keyboard.press(Key.tab)
		keyboard.release(Key.alt)
		keyboard.release(Key.tab)

		time.sleep(0.1)

		keyboard.press(Key.alt)
		keyboard.press(Key.tab)
		keyboard.release(Key.alt)
		keyboard.release(Key.tab)
		
		time.sleep(timeToSleep)


if __name__ == "__main__":
      main()