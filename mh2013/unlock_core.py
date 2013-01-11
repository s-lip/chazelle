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
    '/': requirements(required_points=0, prerequisites=set(), and_answer=False),
    '/enigmavalley/': requirements(required_points=0, prerequisites=set(), and_answer=False),
    '/enigmavalley/changing_states/': requirements(required_points=0,
                                                   prerequisites=set(), and_answer=True),
    '/enigmavalley/open_secrets/': requirements(required_points=0,
                                                prerequisites=set(), and_answer=True),
    '/enigmavalley/the_silver_screen/': requirements(required_points=0,
                                                     prerequisites=set(), and_answer=True),
    '/enigmavalley/the_thomas_crown_scare/': requirements(required_points=0,
                                                          prerequisites=set(), and_answer=True),
    '/enigmavalley/you_will_not_go_to_space_today/': requirements(required_points=0,
                                                                  prerequisites=set(), and_answer=True),

    '/media/js/fixie-nav.js': requirements(required_points=0,
                                                  prerequisites=set(), and_answer=False),
    '/media/js/less-1.3.0.min.js': requirements(required_points=0,
                                                  prerequisites=set(), and_answer=False),
    '/media/less/base.less': requirements(required_points=0,
                                                  prerequisites=set(), and_answer=False),
    '/media/less/hunt_theme.less': requirements(required_points=0,
                                                  prerequisites=set(), and_answer=False),
    '/media/less/enigmavalley.less': requirements(required_points=0,
                                                  prerequisites=set(), and_answer=False),
    '/media/img/evillogo.png': requirements(required_points=0,
                                                  prerequisites=set(), and_answer=False),
    '/media/img/evillogo.png': requirements(required_points=0,
                                                  prerequisites=set(), and_answer=False),
    '/media/img/folder-icon.png': requirements(required_points=0,
                                                  prerequisites=set(), and_answer=False),
    '/media/img/file-icon.png': requirements(required_points=0,
                                                  prerequisites=set(), and_answer=False),
    '/media/fonts/leaguegothic-regular-webfont.ttf': requirements(required_points=0,
                                                  prerequisites=set(), and_answer=False),

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

    @staticmethod
    def _get_thing_and_bundle(thing):
        ret = set([thing])
        if UNLOCK_MES[thing].and_answer:
            assert thing.endswith('/')
            ret.add(thing + 'answer/')
        return ret

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
                    unlocked_stuff_this_run = True
                    thing_bundle = self._get_thing_and_bundle(maybe_unlock)
                    unlock_things.update(thing_bundle)
                    logging.warning("Unlocked: %s", unlock_things)

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
                unlock_bundle = self._get_thing_and_bundle(maybe_unlock)
                unlock_these.update(unlock_bundle)

        if unlock_these:
            self.do_unlock(unlock_these)
            logging.info("Unlocked %s", unlock_these)
