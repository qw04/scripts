from pynput.keyboard import Key, Controller, HotKey, Listener
import time
import random
import sys
import threading

def thing(timeToSleep):
	# does the sleep avoiding
	controller = Controller()
	time.sleep(2)
	
	while True:
		controller.press(Key.alt)
		controller.press(Key.tab)
		controller.release(Key.alt)
		controller.release(Key.tab)

		time.sleep(0.1)

		controller.press(Key.alt)
		controller.press(Key.tab)
		controller.release(Key.alt)
		controller.release(Key.tab)
		
		time.sleep(timeToSleep)

def on_activate():
	print("hotkey pressed")
	global thread
	thread.join()


def main():
	if len(sys.argv) < 2:
		raise Exception("Usage python stopSleep <time to sleep between 2 alt-tabs>")

	else:	
		start = time.time()
		global thread
		thread = threading.Thread(target=thing, args=(float(sys.argv[1]),))
		thread.start()

		hotkey = HotKey(HotKey.parse('<ctrl>+<alt>+h'), on_activate = on_activate)
		with Listener(on_press=lambda k: hotkey.press(l.canonical(k))) as l:
			l.join()
		
		print(f"program ran for{time.time() - start} seconds")


if __name__ == "__main__":
      main()