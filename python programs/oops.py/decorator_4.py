from datetime import datetime
from time import sleep



def cal_time(fuction):
    def wrapper(*args):
        start_time = datetime.now()
        print(f"start_time = {start_time}")
        fuction(*args)
        end_time = datetime.now()
        sleep(1)
        print(f"{end_time - start_time }")
    return wrapper

@cal_time
def sums(*args):
    print(sum(args))

sums(1,2,4,5,6,7,8,9,5)





