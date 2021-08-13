import os
import time
import argparse

original_number = 1
max_number = original_number + 1000000000000000
number = original_number
steps = 1

def checkArgs(original_number, message, mode):
    with open('data/{}.csv'.format(original_number), mode) as file:
        file.write(message)

def resetVariables(original_number, number, steps):
    original_number += 1
    number = original_number
    steps = 1
    checkArgs(original_number, 'x_value,y_value\n', 'w')
    return original_number, number, steps


def main(original_number, steps, number, max_number):
    parser = argparse.ArgumentParser()

    parser.add_argument('--start', help='Enter the starting digit')
    parser.add_argument('--stop', help='Enter the starting digit')

    args = parser.parse_args()

    if args.start != None:
        original_number = int(args.start)
        number = int(args.start)
        max_number = original_number + 100
    if args.stop != None:
        max_number = int(args.stop)

    checkArgs(original_number, 'x_value,y_value\n', 'w')

    while True:
        if number % 2 == 0:
            print('Step {} on {}: {} / 2 = {}\n'.format(steps, original_number, number, number / 2))
            number /= 2
            steps += 1
        elif number != 1:
            print('Step {} on {}: 3 * {} + 1 = {}\n'.format(steps, original_number, number, number * 3 + 1))
            number = number * 3 + 1
            steps += 1
        elif number == 1:
            print('{} reached 1.'.format(original_number))
            #time.sleep(1)
            original_number, number, steps = resetVariables(original_number, number, steps)
        checkArgs(original_number, '{},{}\n'.format(steps, number), 'a')

        if original_number > max_number:
            break


if __name__ == '__main__':
    main(original_number, steps, number, max_number)
