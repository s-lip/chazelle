import types
import unittest2
import logging
import collections

requirements = collections.namedtuple('requirements',
                                      'required_points prerequisites and_answer')
## We treat 'requirements' as an OR -- if you have ANY item in the
## list of things in requirements, OR you have the required points, we
## should unlock it.
##
## I jammed also_unlock_answer into it because I didn't have
## anywhere else to put that.
##
## In the future, and_answer will probably have to be replaced with a
## set of sub-URLs to also unlock. This will be required for e.g.
## the git puzzle.

POINT_THRESHHOLDS = {
    'oceans_11': 1000,
}

# XXX:
# puzzles need to imply the unlocking of:
# - their /answer/
# - their stuff from /media/, if any
# - the stuff not in /media/ you get for free
# - some puzzles may have a /hint/... those presumably are unlocked manually (or time-based)
# - some puzzles have /visit/ -- ??!!

UNLOCK_MES = {
    # Round 0
    '/enigmavalley/': requirements(required_points=0, prerequisites=set(), and_answer=False),
    '/enigmavalley/things_and_flags/': requirements(required_points=0,
                                           prerequisites=set(), and_answer=True),
    '/enigmavalley/puzzle2/': requirements(required_points=0,
                                           prerequisites=set(), and_answer=True),
    '/enigmavalley/puzzle3/': requirements(required_points=0,
                                           prerequisites=set(), and_answer=True),
    '/enigmavalley/puzzle4/': requirements(required_points=0,
                                           prerequisites=set(), and_answer=True),
    '/enigmavalley/puzzle5/': requirements(required_points=0,
                                           prerequisites=set(), and_answer=True),
    '/enigmavalley/puzzle6/': requirements(required_points=0,
                                           prerequisites=set(), and_answer=True),
    '/enigmavalley/meta/': requirements(required_points=0,
                                        prerequisites=set(), and_answer=True),
    # Round 1
    '/oceans_11/': requirements(required_points=POINT_THRESHHOLDS['oceans_11'],
                                prerequisites=set(['/enigmavalley/solved']), and_answer=False),
    '/oceans_11/puzzle1/': requirements(required_points=POINT_THRESHHOLDS['oceans_11'],
                                        prerequisites=set(['/enigmavalley/solved']), and_answer=False),
    '/oceans_11/puzzle2/': requirements(required_points=POINT_THRESHHOLDS['oceans_11'],
                                        prerequisites=set(['/enigmavalley/solved']), and_answer=False),
    '/oceans_11/puzzle3/': requirements(required_points=POINT_THRESHHOLDS['oceans_11'],
                                        prerequisites=set(['/enigmavalley/solved']), and_answer=False),
    '/oceans_11/puzzle4/': requirements(required_points=POINT_THRESHHOLDS['oceans_11'],
                                        prerequisites=set(['/enigmavalley/solved']), and_answer=False),
    '/oceans_11/puzzle5/': requirements(required_points=POINT_THRESHHOLDS['oceans_11'],
                                        prerequisites=set(['/enigmavalley/solved']), and_answer=False),
    '/oceans_11/puzzle6/': requirements(required_points=POINT_THRESHHOLDS['oceans_11'],
                                        prerequisites=set(['/enigmavalley/solved']), and_answer=False),
    '/oceans_11/puzzle7/': requirements(required_points=POINT_THRESHHOLDS['oceans_11'],
                                        prerequisites=set(['/enigmavalley/solved']), and_answer=False),
    '/oceans_11/puzzle8/': requirements(required_points=POINT_THRESHHOLDS['oceans_11'],
                                        prerequisites=set(['/enigmavalley/solved']), and_answer=False),
    '/oceans_11/puzzle9/': requirements(required_points=POINT_THRESHHOLDS['oceans_11'],
                                        prerequisites=set(['/enigmavalley/solved']), and_answer=False),
    '/oceans_11/puzzle10/': requirements(required_points=POINT_THRESHHOLDS['oceans_11'],
                                         prerequisites=set(['/enigmavalley/solved']), and_answer=False),
    '/oceans_11/puzzle11/': requirements(required_points=POINT_THRESHHOLDS['oceans_11'],
                                         prerequisites=set(['/enigmavalley/solved']), and_answer=False),
    '/oceans_11/fragment1/': requirements(required_points=POINT_THRESHHOLDS['oceans_11'],
                                         prerequisites=set(['/oceans_11/puzzle1/solved']), and_answer=False),
    '/oceans_11/fragment2/': requirements(required_points=POINT_THRESHHOLDS['oceans_11'],
                                         prerequisites=set(['/oceans_11/puzzle1/solved']), and_answer=False),
    '/oceans_11/fragment3/': requirements(required_points=POINT_THRESHHOLDS['oceans_11'],
                                         prerequisites=set(['/oceans_11/puzzle2/solved']), and_answer=False),


    # Round 1 casinos
    '/oceans_11/casino1/': requirements(required_points=POINT_THRESHHOLDS['oceans_11'],
                                        prerequisites=set([
                '/oceans_11/fragment1/',
                '/oceans_11/fragment3/',
                ]), and_answer=False),

}

class HuntTeamState(object):
    def __init__(self):
        self.unlocked = set()
        self.handle_time_tick(0)
        # The following are trivial things that provide
        # read-only views of the team state, and of the
        # round context.
        self.team_ctx_proxy = None
        self.round_ctx_proxy = None

    def recursive_unlock_propagate(self):
        unlocked_stuff_this_run = True
        unlock_things = set()

        while unlocked_stuff_this_run:
            unlocked_stuff_this_run = False

            for maybe_unlock in UNLOCK_MES:
                if ((maybe_unlock in self.unlocked) or
                    (maybe_unlock in unlock_things)):
                    continue
                reqs = UNLOCK_MES[maybe_unlock]
                if (self.unlocked.intersection(reqs.prerequisites) or
                    unlock_things.intersection(reqs.prerequisites)):
                    logging.warning("Unlocked: %s", maybe_unlock)
                    unlock_things.add(maybe_unlock)
                    if reqs.and_answer:
                        assert maybe_unlock.endswith('/')
                        unlock_things.add(maybe_unlock + 'unlocked/')
                        logging.warning("Unlocked answery thing: %s", maybe_unlock)
                    unlocked_stuff_this_run = True

        return unlock_things


    def do_unlock(self, things):
        assert type(things) not in types.StringTypes
        # Store the fact that we have unlocked it
        for thing in things:
            self.unlocked.add(thing)
        # unlock anything recursively now
        unlock_things = self.recursive_unlock_propagate()
        self.unlocked.update(unlock_things)

        # FIXME: Trigger any event pushes to jason code
        # ...

    def get_points(self):
        return 0

    def handle_time_tick(self, time):
        current_points = self.get_points()

        unlock_these = set()

        for maybe_unlock in UNLOCK_MES:
            if maybe_unlock in self.unlocked:
                continue

            req = UNLOCK_MES[maybe_unlock]
            if current_points >= req.required_points:
                unlock_these.add(maybe_unlock)

        if unlock_these:
            self.do_unlock(unlock_these)
            logging.info("Unlocked %s", unlock_these)

class UnlockTests(unittest2.TestCase):
    def test_hunt_start(self):
        hts = HuntTeamState()
        self.assertEqual(hts.unlocked, set([
                    '/enigmavalley/',
                    '/enigmavalley/puzzle1/',
                    '/enigmavalley/puzzle2/',
                    '/enigmavalley/puzzle3/',
                    '/enigmavalley/puzzle4/',
                    '/enigmavalley/puzzle5/',
                    '/enigmavalley/puzzle6/',
                    '/enigmavalley/meta/',
                    '/enigmavalley/puzzle1/answer/',
                    '/enigmavalley/puzzle2/answer/',
                    '/enigmavalley/puzzle3/answer/',
                    '/enigmavalley/puzzle4/answer/',
                    '/enigmavalley/puzzle5/answer/',
                    '/enigmavalley/puzzle6/answer/',
                    '/enigmavalley/meta/answer/',
                    ]))

    def test_solve_round0(self):
        hts = HuntTeamState()
        hts.do_unlock(['/enigmavalley/solved'])
        need_unlocked = set([
                '/oceans_11/',
                '/oceans_11/puzzle1/',
                '/oceans_11/puzzle2/',
                '/oceans_11/puzzle3/',
                '/oceans_11/puzzle4/',
                '/oceans_11/puzzle5/',
                '/oceans_11/puzzle6/',
                '/oceans_11/puzzle7/',
                '/oceans_11/puzzle8/',
                '/oceans_11/puzzle9/',
                '/oceans_11/puzzle10/',
                '/oceans_11/puzzle11/',
                ])
        for item in need_unlocked:
            self.assert_(item in hts.unlocked, "Missing %s" % (item,))

    ### FIXME: There should be a test for each casino fragment, maybe
    def test_solve_round1_casino_fragment(self):
        hts = HuntTeamState()
        hts.do_unlock(['/enigmavalley/solved'])
        hts.do_unlock(['/oceans_11/puzzle1/solved'])
        needs_unlocked = set(['/oceans_11/fragment1/',
                              '/oceans_11/fragment2/',
                              ])
        self.assertTrue(hts.unlocked.issuperset(needs_unlocked))
        self.assertFalse('/oceans_11/fragment3/' in hts.unlocked)

    def test_solve_round1_gives_you_casinos(self):
        hts = HuntTeamState()
        hts.do_unlock(['/enigmavalley/solved'])
        hts.do_unlock(['/oceans_11/puzzle1/solved'])
        needs_unlocked = set([
                '/oceans_11/casino1/',
                ])
        self.assertTrue(hts.unlocked.issuperset(needs_unlocked))

    ## FIXME: Round 1 supermeta?



### Note: There should be a semi-manual test that when veil is running,
### and "unlock" is set to True, that all the URLs we use above actually
### return HTTP status 200, except the ones that end in "/solved" because
### that is an internal thingamabob.

