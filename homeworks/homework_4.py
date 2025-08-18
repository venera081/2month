from datetime import datetime as dt
from time import sleep

def checktime_before_after(function):
    def wrapper(*args, **kwargs):
        time_now = dt.now().strftime("%H:%M:%S %Y/%m/%d")
        print(f"Функция была вызвана в {time_now}")
        result = function(*args, **kwargs)
        time_end = dt.now().strftime("%H:%M:%S %Y/%m/%d")
        print(f"Функция была завершена в {time_end} ")
        return result
    return wrapper


@checktime_before_after
def hello_world():
    print("Hello World")
    sleep(1)

hello_world()




