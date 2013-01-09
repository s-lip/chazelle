import logging; logger = logging.getLogger(__name__)

from veil.unlock.basic import TeamState, BasicEngine 
from .checkers import TestChecker
from copy import deepcopy

class Hunt2013TeamState(TeamState):
    INITIAL_UNLOCK = [
            '/',
            '/media/',
            '/media/fonts/',
            '/media/img/',
            '/media/img/traps/',
            '/media/js/',
            '/media/less/',
    ]

    INITIAL_TEAM_CTX = {
            'evilserver': {
                'is_solved': False
                },
    }

    def __init__(self, team_id, engine, log_collection):
        TeamState.__init__(self, team_id, engine, log_collection)
        self.events = []
        self.checker = TestChecker(self, engine)
        self.round_ctx['round'] = {'foo': None}
        self.team_ctx = deepcopy(self.INITIAL_TEAM_CTX)

    def get_checker(self, ref):
        logger.info('[%s].get_checker(ref=%r)', self.team_id, ref)
        self.events.append({'event': 'get_checker',
                            'ref': ref})
        return self.checker

    def start_hunt(self):
        logger.info('[%s].start_hunt()', self.team_id)
        self.events.append({'event': 'start_hunt'})
        self.unlock(*self.INITIAL_UNLOCK)

class TestUnlockEngine(BasicEngine):
    TEAMSTATE_CLASS = Hunt2013TeamState
    def __init__(self, stomp_connection,
                 tellme,
                 destination,
                 db_connection):
        BasicEngine.__init__(self,
                             stomp_connection,
                             tellme,
                             destination,
                             db_connection)

        # Create teams
        logger.info('creating teams...')
        self.create_team('paulproteus')
        self.create_team('jalonso')
