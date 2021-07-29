#!/usr/bin/python
'''
Script to create the input CSV file for the parallel coordinates plot
'''

def main(debug):

if __name__ == "__main__":

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", help="Turn on debug messages", action="store_true", default=False)
    args = parser.parse_args()
    debug = args.debug

    main(debug)

