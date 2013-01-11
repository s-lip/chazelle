import types
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
    'oceans_11': None, # None is a special value meaning do not use points
    'feynman': 2000, # FIXME: Pick a value here
    'feynman_puzzle': 2000, # A linear proportion of this is allocated to each puzzle within Feynman
}

POINTS_GIVEN = {
    '/oceans_11/solved': 2000, # FIXME: Set this threshhold
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

    # Round 2
    '/feynman/': requirements(required_points=POINT_THRESHHOLDS['feynman'],
                              prerequisites=set(), and_answer=False),
    '/feynman/puzzle1/': requirements(required_points=(
            POINT_THRESHHOLDS['feynman'] + ((0/25.) * POINT_THRESHHOLDS['feynman_puzzle'])),
            prerequisites=set(), and_answer=False),

}

class HuntTeamState(object):
    def __init__(self):
        self.points = 0
        self.unlocked = set()
        self.handle_time_tick()
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

    @staticmethod
    def calculate_points_for_things_unlocked(things):
        '''Note: This is purely functional -- it does not use any state
        from within the instance.'''
        points = 0
        for thing in things:
            if thing in POINTS_GIVEN:
                howmany = POINTS_GIVEN[thing]
                logging.warn("Adding %d points for %s", howmany, thing)
                points += howmany
        return points

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
        self.points = self.calculate_points_for_things_unlocked(self.unlocked)
        self.handle_time_tick()

    def get_points(self):
        return self.points

    def handle_time_tick(self):
        current_points = self.get_points()

        unlock_these = set()

        for maybe_unlock in UNLOCK_MES:
            if maybe_unlock in self.unlocked:
                continue

            req = UNLOCK_MES[maybe_unlock]
            # For unlock items that have opted out of the points
            # system... do not unlock them.
            if req.required_points is None:
                continue

            # Otherwise, do the point-based unlock logic.
            if current_points >= req.required_points:
                unlock_bundle = self._get_thing_and_bundle(maybe_unlock)
                unlock_these.update(unlock_bundle)

        if unlock_these:
            self.do_unlock(unlock_these)
            logging.info("Unlocked %s", unlock_these)
