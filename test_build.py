import sys
from build import fizzbuzz

def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
    
test(fizzbuzz(21)) #number divisible by 3
test(fizzbuzz(10)) #number divisible by 5
test(fizzbuzz(30)) #number divisible by 3 and 5
test(fizzbuzz(11)) #number neither divisible by 3 nor by 5
