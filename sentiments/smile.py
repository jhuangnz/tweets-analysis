##
#   Implement a program that categorizes a word as positive or negative.
# 
#   Author: Julie Huang, julie@juliehuang.co.nz
#  
#   This file contains a solution to part 1 of 'Sentiments' from pset6
# 
#   CS50x

import os
import sys

from analyzer import Analyzer
from termcolor import colored

def main():

    # ensure proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: ./smile word")

    # absolute paths to lists - my notes: establising file directory path to the appropriate .txt file
    positives = os.path.join(sys.path[0], "positive-words.txt")
    negatives = os.path.join(sys.path[0], "negative-words.txt")

    # instantiate analyzer
    analyzer = Analyzer(positives, negatives)

    # analyze word
    score = analyzer.analyze(sys.argv[1])
    if score > 0.0:
        print(colored(":)", "green"))
    elif score < 0.0:
        print(colored(":(", "red"))
    else:
        print(colored(":|", "yellow"))

if __name__ == "__main__":
    main()
