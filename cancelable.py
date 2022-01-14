class time:
    def sleep(seconds):
        endSleep = time.time() + seconds
        while True:
            if shouldCancelSleep:
                break
            if time.time() >= endSleep:
                break

#Lav det til et module som også understøtter input()
#Det skal bruges til programmer hvor man skal kunne annullere en thread
