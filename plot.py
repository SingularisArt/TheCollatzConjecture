import os
import argparse
import pandas as pd
import matplotlib.pyplot as plt


def main():
    for filename in os.listdir('data'):
        f = os.path.join('data', filename)
        if os.path.isfile(f):
            data = pd.read_csv(f)
            x = data['x_value']
            y = data['y_value']

            plt.plot(x, y)
            plt.title('Number: {}'.format(filename[:-4]))

            plt.show()

            x = 0
            y = 0

if __name__ == '__main__':
    main()
