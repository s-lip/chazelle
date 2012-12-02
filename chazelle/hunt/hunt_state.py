import datetime
import os.path
import ConfigParser

class HuntState(object):
    def __init__(self):
        self.parser = ConfigParser.RawConfigParser()
        self.parser.read(os.path.join(
                os.path.dirname(__file__),
                'hunt_state.ini'))

class Hunt():
    def __init__(self, team, rounds=[]):
        self.team = team
        self.rounds = rounds
        
    def next_autounlock_time(self):
        return datetime.datetime.now() + datetime.timedelta(hours=1)

class Round():
    def __init__(self, slug, name, is_unlocked=False, is_solved=False, trap_solved=False, puzzles=[]):
        self.slug = slug
        self.name = name
        self.is_unlocked = is_unlocked
        self.puzzles = puzzles
        self.is_solved = is_solved
        self.trap_solved = trap_solved
    
    def __unicode__(self):
        return self.name

class Puzzle():
    def __init__(self, slug, answer, name='', is_unlocked=True, is_solved=False):
        self.slug = slug
        self.name = name if name else slug
        self.is_unlocked = is_unlocked
        self.is_solved = is_solved
        self.answer = answer
        
    def __unicode__(self):
        return self.name
        
class Note():
    def __init__(self, slug, name, is_unlocked=False):
        self.slug = slug
        self.name = name
        self.is_unlocked=is_unlocked
        
    def __unicode__(self):
        return self.name
        
# initialize data!!!!

hunt = Hunt(team="Manic Sages")

# initialize rounds
opening = Round(slug="evilbank_server", name="EVILBank Server", is_unlocked=True, is_solved=True)
feynman = Round(slug="feynman", name="Richard Feynman")
agent_99 = Round(slug="agent_86", name="Agent 86", is_unlocked=True)
agent_99.is_99 = False
oceans_11 = Round(slug="oceans_11", name="Danny Ocean", is_unlocked=True)
sneakers = Round(slug="sneakers", name="Marty Bishop", is_unlocked=True, is_solved=True, trap_solved=True)
rubik = Round(slug="rubik", name="Erno Rubik")
indiana = Round(slug="indiana_jones", name="Indiana Jones")

hunt.rounds = [opening, feynman, agent_99, oceans_11, sneakers, rubik, indiana]

# opening round
a = Puzzle(slug="test_puzzle_1", answer="RUBIK", is_solved=True)
b = Puzzle(slug="test_puzzle_2", answer="MAXWELLSMART", is_solved=True)
c = Puzzle(slug="test_puzzle_3", answer="MARTYBISHOP", is_solved=True)
d = Puzzle(slug="test_puzzle_4", answer="INDIANAJONES", is_solved=True)
e = Puzzle(slug="test_puzzle_5", answer="RICHARDFEYNMAN", is_solved=True)
f = Puzzle(slug="test_puzzle_6", answer="DANNYOCEAN", is_solved=True)
g = Puzzle(slug="meta", answer="PASSWORD")

opening.puzzles = [a,b,c,d,e,f,g]

# feynman puzzles
a = Puzzle(slug="test_puzzle_1", answer="JONESING")
b = Puzzle(slug="test_puzzle_2", answer="ROCKAFELLER")
c = Puzzle(slug="test_puzzle_3", answer="SLIP")
d = Puzzle(slug="feynman_diagram", answer="ELECTRICSLIDE")
feynman.puzzles = [a,b,c,d]

# agent 99
a = Puzzle(slug="puzzle1", answer="PILSNER")
b = Puzzle(slug="puzzle2", answer="HEROINE", is_solved=True)
c = Puzzle(slug="puzzle3", answer="LONGISLANDEXPRESS")
d = Puzzle(slug="meeting_agenda", answer="TERROR")
agent_99.puzzles = [a,b,c,d]

# ocean's 11
a = Puzzle(slug="Danny Ocean", answer="GOBBLEGOBBLE", is_solved=True)
b = Puzzle(slug="Frank Catton", answer="BLIP")
c = Puzzle(slug="Rusty Ryan", answer="YELLOWDART", is_solved=True)
d = Puzzle(slug="Reuben Tishkoff", answer="WAXPAPER", is_solved=True)
e = Puzzle(slug="Virgil Malloy", answer="BRICKHOUSE")
f = Puzzle(slug="Turk Malloy", answer="BUBBLICIOUS")
g = Puzzle(slug="Basher Tarr", answer="MUSICBOX")
h = Puzzle(slug="The Amazing Yen", answer="SPIES", is_solved=True)
i = Puzzle(slug="Saul Bloom", answer="SVALBARD")
j = Puzzle(slug="Linus Caldwell", answer="REDHAT")
k = Puzzle(slug="mirage", answer="NORTHCAROLINA")
l = Puzzle(slug="mgm_grand", answer="SUCCULENT")
m = Puzzle(slug="stratosphere", answer="BACONCAT")
n = Puzzle(slug="luxor", answer="SPHINXES")
o = Puzzle(slug="caesars_palace", answer="JOHNMADISON")

oceans_11.puzzles = [a,b,c,d,e,f,g, h, i, j, k, l, m, n, o]

# sneakers

a = Puzzle(slug="document_1", answer="SUFFERINGSUCCOTASH", is_solved=True)
b = Puzzle(slug="document_2", answer="NUTSTOYOU", is_solved=True)
c = Puzzle(slug="document_3", answer="CHICKENFINGERS", is_solved=True)
d = Puzzle(slug="federal_reserve", answer="DOTHETWIST", is_solved=True)
e = Puzzle(slug="national_power_grid", answer="SKINTASTIC", is_solved=True)
f = Puzzle(slug="air_traffic_control", answer="MANDOLIN", is_solved=True)

sneakers.puzzles = [a, b, c, d, e, f]

# rubik

# indiana jones
         
notes = {'opening_ceremony_note_unlocked': True, 'opening_round_note_unlocked': True, 'agent_99_note_unlocked': False}

state = {
    'team': hunt.team,
    'next_autounlock_time': hunt.next_autounlock_time,
    'rounds': hunt.rounds,
    'notes': notes,
}

