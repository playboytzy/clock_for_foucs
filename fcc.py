import time

def pomodoro_timer(minute):
    seconds = minute * 60
    while seconds > 0:
        minutes, sec = divmod(seconds, 60)
        timer = "{:02d}:{:02d}".format(minutes, sec)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print("时间到！专注时间结束。")

if __name__ == "__main__":
    minute = int(input("请输入专注时长（分钟）: "))
    pomodoro_timer(minute);
