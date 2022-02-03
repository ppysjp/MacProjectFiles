# A PRIMITIVE COUNT DOWN TIMER
import time

num_seconds = 3 
for countdown in reversed(range(num_seconds + 1)):
    if countdown > 0:
        #print(countdown, end='...')
        print(countdown, end='...', flush=True)
        time.sleep(1)
    else:
        print('Go!')

# This doesn' behave in exactly the way we would like unless we use flush

