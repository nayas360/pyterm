# time command prints current time
import time


def main():
    time_stamp = time.strftime('%I:%M:%S %p')
    print(time_stamp)
