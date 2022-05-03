from pynput.keyboard import Key, Controller
import time
import random

keyboard = Controller()



def main():
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
		
		time.sleep(180)


if __name__ == "__main__":
      main()