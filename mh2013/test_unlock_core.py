import unittest2
import mh2013.unlock_core


class UnlockTests(unittest2.TestCase):
    def test_hunt_start(self):
        hts = mh2013.unlock_core.HuntTeamState()
        golden = set([
                '/',
                '/enigmavalley/',
                '/enigmavalley/changing_states/',
                '/enigmavalley/open_secrets/',
                '/enigmavalley/the_silver_screen/',
                '/enigmavalley/the_thomas_crown_scare/',
                '/enigmavalley/you_will_not_go_to_space_today/',
                '/enigmavalley/meta/',
                '/enigmavalley/changing_states/answer/',
                '/enigmavalley/open_secrets/answer/',
                '/enigmavalley/the_silver_screen/answer/',
                '/enigmavalley/the_thomas_crown_scare/answer/',
                '/enigmavalley/you_will_not_go_to_space_today/answer/',
                '/enigmavalley/meta/answer/',
                ## FIXME: enigmavalley media will move, I guess
                '/media/js/less-1.3.0.min.js',
                '/media/fonts/leaguegothic-regular-webfont.ttf',
                '/media/js/fixie-nav.js',
                '/media/less/base.less',
                '/media/less/hunt_theme.less',
                '/media/less/enigmavalley.less',
                '/media/img/evillogo.png',
                '/media/img/file-icon.png',
                '/media/img/folder-icon.png',
                ])
        self.assertEqual(hts.unlocked, golden)

    def test_solve_round0(self):
        hts = mh2013.unlock_core.HuntTeamState()
        hts.do_unlock(['/enigmavalley/solved'])
        need_unlocked = set([
                '/oceans_11/',
                '/oceans_11/puzzle1/',
                '/oceans_11/puzzle2/',
                '/oceans_11/puzzle3/',
                '/oceans_11/puzzle4/',
                '/oceans_11/puzzle5/',
                '/oceans_11/puzzle6/',
                '/oceans_11/puzzle7/',
                '/oceans_11/puzzle8/',
                '/oceans_11/puzzle9/',
                '/oceans_11/puzzle10/',
                '/oceans_11/puzzle11/',
                ])
        for item in need_unlocked:
            self.assert_(item in hts.unlocked, "Missing %s" % (item,))

    ### FIXME: There should be a test for each casino fragment, maybe
    def test_solve_round1_casino_fragment(self):
        hts = mh2013.unlock_core.HuntTeamState()
        hts.do_unlock(['/enigmavalley/solved'])
        hts.do_unlock(['/oceans_11/puzzle1/solved'])
        needs_unlocked = set(['/oceans_11/fragment1/',
                              '/oceans_11/fragment2/',
                              ])
        self.assertTrue(hts.unlocked.issuperset(needs_unlocked))
        self.assertFalse('/oceans_11/fragment3/' in hts.unlocked)

    def test_solve_round1_puzzles_gives_you_casinos(self):
        hts = mh2013.unlock_core.HuntTeamState()
        hts.do_unlock(['/enigmavalley/solved'])
        hts.do_unlock(['/oceans_11/puzzle1/solved'])
        needs_unlocked = set([
                '/oceans_11/casino1/',
                ])
        self.assertTrue(hts.unlocked.issuperset(needs_unlocked))

    ## FIXME: Round 1 supermeta?

    def test_solve_round1_entirely_gives_you_round2(self):
        hts = mh2013.unlock_core.HuntTeamState()
        hts.do_unlock(['/enigmavalley/solved'])
        hts.do_unlock(['/oceans_11/solved'])
        needs_unlocked = set([
                '/feynman/',
                '/feynman/puzzle1/',
                '/feynman/puzzle1/answer/',
                ])
        self.assertEqual(hts.unlocked.intersection(needs_unlocked),
                         needs_unlocked)


### Note: There should be a semi-manual test that when veil is running,
### and "unlock" is set to True, that all the URLs we use above actually
### return HTTP status 200, except the ones that end in "/solved" because
### that is an internal thingamabob.


