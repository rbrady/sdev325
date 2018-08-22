#/usr/bin/env python
import datetime


def main():
    popcorn = datetime.datetime.today().strftime('%Y-%m-%d')
    message = "Hello, World!  Today is {}."
    print(message.format(popcorn))


if __name__ == '__main__':
    main()
