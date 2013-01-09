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

    # Does the puzzle directory exist?
    puzzlepath = os.path.join(roundpath, puzzleslug)
    # If it does exist, we are done.
    if os.path.exists(puzzlepath):
        assert os.path.exists(os.path.join(puzzlepath, 'index.html')), puzzlepath
        return

    # Otherwise, make one, copying from sample-puzzle
    os.mkdir(puzzlepath)
    round_sample_puzzle_html = open(os.path.join(
            roundpath, 'sample-puzzle', 'index.html')).read()
    with open(os.path.join(puzzlepath, 'index.html'), 'w') as p:
        p.write(round_sample_puzzle_html)

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
