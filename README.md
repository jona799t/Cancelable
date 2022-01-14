# Usage
```python
from cancelable import time
import threading

def count():
  i = 1
  while True:
    time.sleep(1)
    i += 1
    print(i)

threading._start_new_thread(count, ())

input("Click enter to cancel counting")
time.cancel()
```
