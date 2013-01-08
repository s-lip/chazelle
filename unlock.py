import types
import unittest2
import logging
import collections

requirements = collections.namedtuple('requirements',
                                      'required_points prerequisites')

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
    
}

class HuntTeamState(object):
    def __init__(self):
        self.unlocked = set()
        self.handle_time_tick(0)

    def do_unlock(self, things):
        assert type(things) not in types.StringTypes
        for thing in things:
            self.unlocked.add(thing)
            # FIXME: Trigger any event pushes to jason code

    def get_points(self):
        return 0

    def handle_time_tick(self, time):
        current_points = self.get_points()

        unlock_these = set()

        for maybe_unlock in UNLOCK_MES:
            if maybe_unlock in self.unlocked:
                continue

            req = UNLOCK_MES[maybe_unlock]
            if req.required_points >= current_points:
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

### Note: There should be a semi-manual test that when veil is running,
### and "unlock" is set to True, that all the URLs we use above actually
### return HTTP status 200, except the ones that end in "/solved" because
### that is an internal thingamabob.


