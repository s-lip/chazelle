import datetime
import os.path
import ConfigParser
import iso8601

class HuntState(object):
    def __init__(self):
        self.parser = ConfigParser.RawConfigParser()
        self.parser.read(os.path.join(
                os.path.dirname(__file__),
                'hunt_state.ini'))

    def get_context(self, injected_data=None, general_data=None):
        context = {}
        if injected_data:
            for item in injected_data:
                if item == 'rounds':
                    context.update(self._get_rounds())
                elif item in self._get_rounds()['rounds']:
                    context.update(self._get_round(item))
                else:
                    raise NotImplemented

        if general_data:
            for item in general_data:
                if item == 'team':
                    context[item] = self._get_team()
                else:
                    raise NotImplemented

        return context

    def _config_parser_section_to_dict(self, section_name):
        ret = {}
        items = self.parser.items(section_name)
        for (key, value) in items:
            if key.startswith('is_') or key.startswith('trap_'):
                value = self.parser.getboolean(section_name, key)
            if key.endswith('_date'):
                value = iso8601.parse_date(value)
            ret[key] = value
        return ret

    def _get_rounds(self):
        data = {}
        rounds_list = self.parser.get('rounds_ordering', 'order'
                                      ).split()
        for r in rounds_list:
            r_data = self._config_parser_section_to_dict(r)
            data[r_data['slug']] = r_data

        data['rounds'] = rounds_list

        return data
        
    def _get_round(self, round_slug):
        data = {}
        r_data = self._config_parser_section_to_dict(round_slug)
        data[round_slug] = r_data
        puzzle_list = self.parser.get(round_slug, 'puzzles'
                                      ).split()
        puzzles = []
        for p in puzzle_list:
            p_data = self._config_parser_section_to_dict(p)
            data[p_data['slug']] = p_data
            puzzles.append(p_data['slug'])
        data[round_slug]['puzzles'] = puzzles
        return data

    def _get_team(self):
        data = self._config_parser_section_to_dict('team')
        for intify in ('points', 'extra_credit'):
            data[intify] = int(data[intify])
        return data
