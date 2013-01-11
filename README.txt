How to set up this site for design-type work:

(Note: this requires you to do some stuff on the command line. Fortunately, most of the commands are written out for you here.)

0. Make an account on github. Have aldeka, gwillen, or paulproteus add you to the private Sages github account.

1. Install Python 2.7. (On Mac and most Linux systems, you can skip this step.)

2. Make a folder for this project.

3. Fork the chazelle repository on github.com so you have your own fork to play with. Download your fork's code to your computer: 
git clone ******
Your project folder will now have a folder in it called "chazelle".

4. Notice the "assets" folder. This where the templates are.

5. Install "gevent" for your Python. On Linuxy systems, the following should work:

   sudo apt-get install python-gevent

6. Install "veil", the code that actually renders these templates:

All you have to do is "git clone" it into the right place. You can do that with
these steps:

   cd ..
   git clone git@github.com:manicsages/veil.git

7. "cd" back into chazelle

   cd chazelle

8. Run the server!

   python runserver.py

9. Go to http://localhost:3001 in your web browser.

You should see the hunt home page (in whatever state it is so far)!

Also -- 127.0.0.1:3001 will not work, so don't use that. Sorry.

How to make or edit round templates and styles:

1. Update the hunt state:

Right now, the "state" for the fake hunt site (what team is competing, what puzzles and rounds they have unlocked, what puzzles and rounds they have solved, etc) is all stored in a giant ini file in hunt/hunt_state.ini. It's mostly made-up at this point--most rounds only have a couple placeholder puzzles listed, and the answers aren't real. So, the first thing you'll want to do is 1.) make sure that is_unlocked is True for the round you want to work on, 2.) the number of Puzzles associated with your round's Round object is the number you expect. If not, add more by copying and pasting; the only requirement is that each puzzle's "slug" (the name of the puzzle in a form that can be part of a URL, with underscores instead of spaces and no special characters) be unique.
replace 'team.evilserver.is_solved' '"/evilserver/solved" in unlocked' 'oceans_11.is_unlocked' '"/oceans_11/" in unlocked' 'oceans_11.is_solved' '"/oceans_11/solved" in unlocked'  'feynman.is_solved' '"/feynman/solved" in unlocked' 'feynman.is_unlocked' '"/feynman/" in unlocked'  'get_smart.is_99' '"/get_smart/is-99" in unlocked'  'get_smart.is_unlocked' '"/get_smart/" in unlocked' 'get_smart.is_solved' '"/get_smart/solved" in unlocked' 'indiana.is_solved' '"/indiana/solved" in unlocked' 'indiana.is_unlocked' '"/indiana/" in unlocked' 'sneakers.is_solved' '"/sneakers/solved" in unlocked' 'sneakers.is_unlocked' '"/sneakers/" in unlocked' 'rubik.is_solved' '"/rubik/solved" in unlocked' 'rubik.is_unlocked' '"/rubik/" in unlocked' 'oceans_11.is_solved' '"/oceans_11/solved" in solved' 'oceans_11.is_unlocked' '"/oceans_11/" in unlocked' 'oceans_11.trap_solved' '"/oceans_11/trap/solved" in unlocked' 'feynman.is_solved' '"/feynman/solved" in unlocked' 'feynman.is_unlocked' '"/feynman/" in unlocked' 'feynman.trap_solved' '"/feynman/trap/solved" in unlocked' 'get_smart.trap_solved' '"/get_smart/trap/solved" in unlocked' 'indiana.trap_solved' '"/indiana/trap/solved" in unlocked' 'sneakers.trap_solved' '"/sneakers/trap/solved" in unlocked'
