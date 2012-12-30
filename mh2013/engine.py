import logging; logger = logging.getLogger(__name__)

from veil.unlock.basic import TeamState, BasicEngine 
from .checkers import TestChecker

class TestState(TeamState):
    def __init__(self, team_id, engine, log_collection):
        TeamState.__init__(self, team_id, engine, log_collection)
        self.events = []
        self.checker = TestChecker(self, engine)
        self.round_ctx['round'] = {'foo': None}

    def get_checker(self, ref):
        logger.info('[%s].get_checker(ref=%r)', self.team_id, ref)
        self.events.append({'event': 'get_checker',
                            'ref': ref})
        return self.checker

    def start_hunt(self):
        logger.info('[%s].start_hunt()', self.team_id)
        self.events.append({'event': 'start_hunt'})
        self.unlock(*self.checker.BUNDLES[0])
        if self.checker.bundle_idx == 0:
            self.checker.bundle_idx += 1

class TestUnlockEngine(BasicEngine):
    TEAMSTATE_CLASS = TestState