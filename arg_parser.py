import argparse

parser = argparse.ArgumentParser(description='Anti-Donut-Protection.')
parser.add_argument('-t', '--time', dest='activation_time', type=int, action='store', default=5,
                    help='Time after which ADP is activated.')

args = parser.parse_args()
