import os
import time
import argparse


class constants:
    DONE = 'done'
    EVEN = 'even'
    ODD = 'odd'


def do_operations(constants_variable: int, original_number: int, number: int, steps: int, status: str) -> int:
    if status == constants_variable.EVEN:
        print('Step {} on {}: {} / 2 = {}\n'.format(steps, original_number, number, number / 2))
        number /= 2
        steps += 1
    elif status == constants_variable.ODD:
        print('Step {} on {}: 3 * {} + 1 = {}\n'.format(steps, original_number, number, number * 3 + 1))
        number = number * 3 + 1
        steps += 1
    elif status == constants_variable.DONE:
        print('{} reached 1.'.format(original_number))
        original_number, number, steps = reset_variables(original_number, number, steps)

        output_to_file(original_number, '{},{}\n'.format(steps, number), 'a')

    return original_number, number, steps


def output_to_file(original_number: int, message: str, mode: str) -> None:
    with open('data/{}.csv'.format(original_number), mode) as file:
        file.write(message)


def reset_variables(original_number: int, number: int, steps: int) -> int:
    original_number += 1
    number = original_number
    steps = 1
    output_to_file(original_number, 'x_value,y_value\n', 'w')

    return original_number, number, steps


def main():
    # ARGPARSE
    parser = argparse.ArgumentParser()

    parser.add_argument('--start', help='Enter the starting digit')
    parser.add_argument('--stop', help='Enter the starting digit')

    args = parser.parse_args()

    # VARIABLES
    constants_variable = constants()
    original_number = 1
    add_on = 1000000000000000
    max_number = original_number + add_on
    number = original_number
    steps = 1

    # CHECKING FOR ARGPARSE ARGUMENTS
    if args.start != None:
        original_number = int(args.start)
        number = int(args.start)
        max_number = original_number + add_on
    if args.stop != None:
        max_number = int(args.stop)

    output_to_file(original_number, 'x_value,y_value\n', 'w')

    # MAIN FOR LOOP
    while True:
        # CHEKING IF THE NUMBER IS DIVISIBLE BY 2 OR NOT AND CHECKING IF IT IS EQUAL TO 1
        if number % 2 == 0:
            original_number, number, steps = do_operations(constants_variable, original_number, number, steps, constants_variable.EVEN)
        elif number != 1:
            original_number, number, steps = do_operations(constants_variable, original_number, number, steps, constants_variable.ODD)
        elif number == 1:
            original_number, number, steps = do_operations(constants_variable, original_number, number, steps, constants_variable.DONE)

        if original_number > max_number:
            break


if __name__ == '__main__':
    main()
