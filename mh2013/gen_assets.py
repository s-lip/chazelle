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

    # Does the roundslug directory exist? It better.
    roundpath = os.path.join(guessed_asset_path, roundslug)
    assert os.path.exists(roundpath)

    return None

def main(argv):
    data = json.loads(sys.stdin.read())
    for puzzle in data:
        if puzzle['status'] not in GOOD_STATUSES:
            if not puzzle['titleslug'] or not puzzle['roundslug']:
                print "Skipping", puzzle
                continue

            make_sample_puzzle_if_necessary(puzzle['roundslug'],
                                            puzzle['titleslug'])
        print puzzle

if __name__ == '__main__':
    main(sys.argv)
