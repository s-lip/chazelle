import logging; logger = logging.getLogger(__name__)

from veil.unlock.basic import TeamState, BasicEngine
from .checkers import TestChecker
from . import unlock_core

class Hunt2013TeamState(TeamState):

    def __init__(self, team_id, engine, log_collection):
        TeamState.__init__(self, team_id, engine, log_collection)
        self.events = []
        self.checker = TestChecker(self, engine)
        self.core = unlock_core.HuntTeamState()
        self.team_ctx = self.core.team_ctx_proxy
        self.round_ctx = self.core.round_ctx_proxy

    def get_checker(self, ref):
        logger.info('[%s].get_checker(ref=%r)', self.team_id, ref)
        self.events.append({'event': 'get_checker',
                            'ref': ref})
        return self.checker

    def start_hunt(self):
        logger.info('[%s].start_hunt()', self.team_id)
        self.events.append({'event': 'start_hunt'})
        self.unlock(*self.core.unlocked)

    def get_team_state_report(self):
        return {'next_unlock_timestamp': 'Someday FIXME',
                'next_unlock_puzzles': 'FIXME a billion',
                'name': 'extrayes',
                'options': '3.14 FIXME',
                }

class TestUnlockEngine(BasicEngine):
    TEAMSTATE_CLASS = Hunt2013TeamState

    def rpc_get_team_round_report(self):
        # FIXME
        return {}

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
