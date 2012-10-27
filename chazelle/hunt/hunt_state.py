import datetime

team = 'Manic Sages'

next_autounlock_time = datetime.datetime.now() + datetime.timedelta(1)

rounds = {
            'evilbank_server': {
                'unlocked': True,
                'puzzles': {
                    '1': {
                        'unlocked': True,
                        'solved': True,
                        'answer': "DANNYOCEAN"
                        },
                    '2': {
                        'unlocked': True,
                        'solved': True,
                        'answer': "AGENT86"
                        },
                    '3': {
                        'unlocked': True,
                        'solved': True,
                        'answer': "ERNORUBIK"
                        },
                    '4': {
                        'unlocked': True,
                        'solved': True,
                        'answer': "INDIANAJONES"
                        },
                    '5': {
                        'unlocked': True,
                        'solved': True,
                        'answer': "MARTYBISHOP"
                        },
                    '6': {
                        'unlocked': True,
                        'solved': True,
                        'answer': "RICHARDFEYNMAN"
                        },
                    'meta': {
                        'unlocked': True,
                        'solved': True,
                        'answer': 'WONTOFORFIVE'
                        },
                    },
                },
            'oceans_11': {
                'unlocked': True, 
                'puzzles' : {
                    'Danny Ocean': {
                            'unlocked': True,
                            'solved': True,
                            'answer': 'AWESOMESAUCE',
                        },
                    'Frank Catton': {
                            'unlocked': True,
                            'solved': False,
                            'answer': 'BLIP',
                        },
                    'Rusty Ryan': {
                            'unlocked': True,
                            'solved': False,
                            'answer': 'YELLOWDART',
                        },
                    'Mirage': {
                            'part_one_unlocked': True,
                            'part_two_unlocked': False,
                            'part_three_unlocked': False,
                        },
                    },
                },
            'agent_86': {
                'unlocked': False,
                'is_99': False,
                'puzzles': {
                    'mission_1': {
                        'unlocked': False,
                        'solved': False,
                        'answer': "NUTSTOYOU"
                        },
                    'mission_2': {
                        'unlocked': False,
                        'solved': False,
                        'answer': "FLUBBER"
                        },
                    'mission_3': {
                        'unlocked': False,
                        'solved': False,
                        'answer': "CHICKENBUTT"
                        },
                    'mission_4': {
                        'unlocked': False,
                        'solved': False,
                        'answer': "SUFFERINGSUCCOTASH"
                        },
                    'meeting_raid': {
                        'unlocked': False,
                        'solved': False,
                        'answer': "PUNGOESHERE"
                    }
                },
            }
         }
         
notes = {'opening_ceremony_unlocked': True, 'the_plan_unlocked': True, 'control_memo_unlocked': False}

state = {
    'team': team,
    'next_autounlock_time': next_autounlock_time,
    'rounds': rounds,
    'notes': notes,
}

