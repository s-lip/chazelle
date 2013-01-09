import sys
import json
import os.path


GOOD_STATUSES = set(['Post-Production',])

def make_sample_puzzle_if_necessary(roundslug, puzzleslug):
    # look, a guess at the asset path
    guessed_asset_path = os.path.abspath(
        os.path.join(
            # Start here...
            os.path.abspath(os.path.dirname(__file__)),
            # Go up one level...
            '..',
            # Grab 'assets'
            'assets'))
    assert os.path.exists(guessed_asset_path)
    return None

def main(argv):
    data = json.loads(sys.stdin.read())
    for puzzle in data:
        if puzzle['status'] not in GOOD_STATUSES:
            make_sample_puzzle_if_necessary(puzzle['roundslug'],
                                            puzzle['titleslug'])
        print puzzle

if __name__ == '__main__':
    main(sys.argv)
