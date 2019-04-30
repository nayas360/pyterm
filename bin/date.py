# date command prints date

import time


def main():
    time_stamp = time.strftime('%A, %d %B %Y')
    print(time_stamp)
