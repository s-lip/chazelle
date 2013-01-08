import types
import unittest2
import logging
import collections

requirements = collections.namedtuple('requirements',
                                      'required_points prerequisites')
## We treat 'requirements' as an OR -- if you have ANY item in the
## list of things in requirements, OR you have the required points, we
## should unlock it.

POINT_THRESHHOLDS = {
    'oceans_11': 1000,
}

UNLOCK_MES = {
    # Round 0
    '/enigmavalley/': requirements(required_points=0, prerequisites=set()),
    '/enigmavalley/puzzle1/': requirements(required_points=0,
                                           prerequisites=set()),
    '/enigmavalley/puzzle2/': requirements(required_points=0,
                                           prerequisites=set()),
    '/enigmavalley/puzzle3/': requirements(required_points=0,
                                           prerequisites=set()),
    '/enigmavalley/puzzle4/': requirements(required_points=0,
                                           prerequisites=set()),
    '/enigmavalley/puzzle5/': requirements(required_points=0,
                                           prerequisites=set()),
    '/enigmavalley/puzzle6/': requirements(required_points=0,
                                           prerequisites=set()),
    '/enigmavalley/meta/': requirements(required_points=0,
                                        prerequisites=set()),
    # Round 1
    '/oceans_11/': requirements(required_points=POINT_THRESHHOLDS['oceans_11'],
                                prerequisites=set(['/enigmavalley/solved'])),
    '/oceans_11/puzzle1/': requirements(required_points=POINT_THRESHHOLDS['oceans_11'],
                                        prerequisites=set(['/enigmavalley/solved'])),
    '/oceans_11/puzzle2/': requirements(required_points=POINT_THRESHHOLDS['oceans_11'],
                                        prerequisites=set(['/enigmavalley/solved'])),
    '/oceans_11/puzzle3/': requirements(required_points=POINT_THRESHHOLDS['oceans_11'],
                                        prerequisites=set(['/enigmavalley/solved'])),
    '/oceans_11/puzzle4/': requirements(required_points=POINT_THRESHHOLDS['oceans_11'],
                                        prerequisites=set(['/enigmavalley/solved'])),
    '/oceans_11/puzzle5/': requirements(required_points=POINT_THRESHHOLDS['oceans_11'],
                                        prerequisites=set(['/enigmavalley/solved'])),
    '/oceans_11/puzzle6/': requirements(required_points=POINT_THRESHHOLDS['oceans_11'],
                                        prerequisites=set(['/enigmavalley/solved'])),
    '/oceans_11/puzzle7/': requirements(required_points=POINT_THRESHHOLDS['oceans_11'],
                                        prerequisites=set(['/enigmavalley/solved'])),
    '/oceans_11/puzzle8/': requirements(required_points=POINT_THRESHHOLDS['oceans_11'],
                                        prerequisites=set(['/enigmavalley/solved'])),
    '/oceans_11/puzzle9/': requirements(required_points=POINT_THRESHHOLDS['oceans_11'],
                                        prerequisites=set(['/enigmavalley/solved'])),
    '/oceans_11/puzzle10/': requirements(required_points=POINT_THRESHHOLDS['oceans_11'],
                                         prerequisites=set(['/enigmavalley/solved'])),
    '/oceans_11/puzzle11/': requirements(required_points=POINT_THRESHHOLDS['oceans_11'],
                                         prerequisites=set(['/enigmavalley/solved'])),
    '/oceans_11/fragment1/': requirements(required_points=POINT_THRESHHOLDS['oceans_11'],
                                         prerequisites=set(['/oceans_11/puzzle1/solved'])),
    '/oceans_11/fragment2/': requirements(required_points=POINT_THRESHHOLDS['oceans_11'],
                                         prerequisites=set(['/oceans_11/puzzle1/solved'])),
    '/oceans_11/fragment3/': requirements(required_points=POINT_THRESHHOLDS['oceans_11'],
                                         prerequisites=set(['/oceans_11/puzzle2/solved'])),
}

class HuntTeamState(object):
    def __init__(self):
        self.unlocked = set()
        self.handle_time_tick(0)

    def do_unlock(self, things):
        assert type(things) not in types.StringTypes
        # Store the fact that we have unlocked it
        for thing in things:
            self.unlocked.add(thing)
        # unlock anything recursively now
        for maybe_unlock in UNLOCK_MES:
            if maybe_unlock in self.unlocked:
                continue
            reqs = UNLOCK_MES[maybe_unlock]
            if self.unlocked.issuperset(reqs.prerequisites):
                self.do_unlock([maybe_unlock])
                logging.warning("Unlocking %s", maybe_unlock)
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

### Note: There should be a semi-manual test that when veil is running,
### and "unlock" is set to True, that all the URLs we use above actually
### return HTTP status 200, except the ones that end in "/solved" because
### that is an internal thingamabob.


