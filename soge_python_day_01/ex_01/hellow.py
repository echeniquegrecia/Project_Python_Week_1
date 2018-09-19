#!/usr/bin/python3
import sys

def main():

    
    print(len(sys.argv)-1))
    print('\n')
    print(len(sys.argv), file=sys.stderr) 

if __name__ == "__main__":
    main()