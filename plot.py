# 580000

import os
import argparse
import pandas as pd
import matplotlib.pyplot as plt


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument('--start', help='Enter the starting digit')

    args = parser.parse_args()

    if args.start != None:
        filename = int(args.start)
    else:
        filename = 1

    while True:
        f = os.path.join('data', str(filename) + '.csv')
        if os.path.isfile(f):
            data = pd.read_csv(f)
            x = data['x_value']
            y = data['y_value']

            plt.plot(x, y)
            plt.title('Number: {}'.format(str(filename)))

            plt.show()

            x = 0
            y = 0

            filename += 1
        else:
            break

if __name__ == '__main__':
    main()
