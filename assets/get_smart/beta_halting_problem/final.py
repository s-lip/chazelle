import subprocess
import sys
import re

clj_out = long(subprocess.check_output(['clojure-1.4','halting_problem.clj']))
subprocess.call(['g++','halting_problem.cpp','-o','halting_problem'])
cpp_out = long(subprocess.check_output(['./halting_problem']))
erl_out = long(subprocess.check_output(['escript','halting_problem.erl']))
hs_out = long(subprocess.check_output(['runghc','halting_problem.hs']))
ml_out = long(subprocess.check_output(['ocaml','halting_problem.ml']))
pl_out = long(subprocess.check_output(['perl','halting_problem.pl']))
scala_out = long(subprocess.check_output(['scala','halting_problem.scala']))

def print_char(n):
    sys.stdout.write(chr(65+((n-1)%26)))

print_char(cpp_out/109+scala_out/13+1)
print_char(erl_out/89+scala_out/41+2)
print_char(clj_out/67+pl_out/181+3)
print_char(clj_out/233+hs_out/191+4)
print_char(cpp_out/103+erl_out/113+5)
print_char(erl_out/127+ml_out/47+6)
print_char(cpp_out/23+pl_out/73+7)
print_char(clj_out/31+ml_out/71+8)
print_char(ml_out/29+scala_out/53+9)
print_char(hs_out/167+pl_out/149+10)
print_char(pl_out/17+scala_out/19+11)
print_char(hs_out/151+scala_out/37+12)
print_char(erl_out/61+hs_out/7+13)
print_char(cpp_out/157+ml_out/83+14)
print_char(ml_out/107+pl_out/163+15)
print_char(clj_out/3+erl_out/229+16)
print_char(cpp_out/101+hs_out/5+17)
sys.stdout.write('\n')
