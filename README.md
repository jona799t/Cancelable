# Usage
```python
from cancelable import time
import threading

def count():
  i = 1
  while True:
    time.sleep(1)
    print(i)
    i += 1

threading._start_new_thread(count, ())

input("Click enter to cancel counting\n")

time.cancel()
```

# To do
Add more functions such as input()
