import logging; logger = logging.getLogger(__name__)

from veil.unlock.basic import AnswerChecker, RejectRequest

class TestChecker(AnswerChecker):
    DESCRIPTIONS = {'puzzle1': 'Test Puzzle 1',
                    'puzzle2': 'Test Puzzle 2'}
    ANSWERS = {'puzzle1': 'REDHERRING',
               'puzzle2': 'BLUEHERRING'}
    BUNDLES = [['/index.html', '/round/puzzle1/', '/round/puzzle1/answer'],
               ['/round/puzzle2/', '/round/puzzle2/answer']]
    bundle_idx = 0

    def __init__(self, team_state, engine):
        AnswerChecker.__init__(self, team_state, engine)
        self.events = []
        for ref in self.ANSWERS:
            self.team_state.puzzle_ctx[ref] = {'past_answers': []}

    def vet_request(self, ref, req_text):
        logger.info('checker(%s).vet_request(ref=%r,req_text=%r)',
                    self.team_id, ref, req_text)
        self.events.append({'event': 'vet_request',
                            'ref': ref,
                            'req_text': req_text})

        if ref not in self.ANSWERS:
            raise RejectRequest()

        answer = self.ANSWERS[ref]
        proposed = ''.join(req_text.upper().split())
        return ('correct' if proposed == answer else 'incorrect')

    def describe_puzzle(self, ref):
        logger.info('checker(%s).describe_puzzle(ref=%r)',
                    self.team_id, ref)
        self.events.append({'event': 'describe_puzzle',
                            'ref': ref})
        return self.DESCRIPTIONS[ref]

    def on_request(self, queue, ref, req_text, contact, request_id):
        logger.info('checker(%s).on_request(queue=%r, ref=%r, req_text=%r, contact=%r, request_id=%r)',
                    self.team_id,
                    queue, ref, req_text, contact, request_id)
        self.events.append({'event': 'on_request',
                            'ref': ref,
                            'req_text': req_text,
                            'contact': contact,
                            'request_id': request_id})

        self.team_state.puzzle_ctx[ref]['past_answers'].append(req_text)
        self.team_state.announce_puzzle(ref)
        return None

    def on_correct(self, operator, ref, req_text, request_id):
        logger.info('checker(%s).on_correct(operator=%r, ref=%r, req_text=%r, request_id=%r)',
                    self.team_id,
                    operator, ref, req_text, request_id)
        self.events.append({'event': 'on_correct',
                            'ref': ref,
                            'req_text': req_text,
                            'request_id': request_id})

        # Unlock something
        if self.bundle_idx < len(self.BUNDLES):
            logger.info('checker(%s) unlocking the next bundle',
                        self.team_id)
            self.team_state.unlock(*self.BUNDLES[self.bundle_idx])
            self.bundle_idx += 1

            # Update round state
            self.team_state.round_ctx['round']['foo'] = 'bar'
            self.team_state.announce_round('round')

    def on_retract(self, operator, ref, req_text, request_id):
        logger.info('checker(%s).on_retract(operator=%r, ref=%r, req_text=%r, request_id=%r)',
                    self.team_id,
                    operator, ref, req_text, request_id)
        self.events.append({'event': 'on_retract',
                            'ref': ref,
                            'req_text': req_text,
                            'request_id': request_id})

    def on_other(self, operator, queue, ref, old_state, action, choice,
                 request_id):
        logger.info('[%s:%d] operator %s chooses %s (%s)',
                    queue, request_id, operator, choice, action)
        self.events.append({'event': 'on_other',
                            'queue': queue,
                            'ref': ref,
                            'old_state': old_state,
                            'action': action,
                            'choice': choice,
                            'request_id': request_id})
