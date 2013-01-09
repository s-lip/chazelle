import sys
import json

def main(argv):
    data = json.loads(sys.stdin.read())
    for puzzle in data:
        print puzzle

if __name__ == '__main__':
    main(sys.argv)
