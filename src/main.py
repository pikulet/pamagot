import logging
import argparse

from engine.interface import Pamagot

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', default=False, action='store_true')    
    args = parser.parse_args()

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.WARNING)

    Pamagot()