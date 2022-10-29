from cancelable import time, input, cancelInput
import threading

name = ""
def ask():
  global name
  name = input("Your name: ")
  time.cancel()

threading._start_new_thread(ask, ())

time.sleep(5)
cancelInput()

print(name)