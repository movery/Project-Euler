import problems

import sys
import datetime

def main():
    if len(sys.argv) == 1:
        print "USAGE: python main.py [problem number] ... [problem number]"
        sys.exit()

    for problem in sys.argv[1:]:
        attr = list("pe000")
        for i in range(len(problem), 0, -1):
            attr[-i] = problem[-i]

        try:
            print "-----------------------------------------"
            print " Attempting to solve Problem " + problem
            func = getattr(problems, "".join(attr))

            start = datetime.datetime.now()
            result = func()
            elapsed = datetime.datetime.now() - start
            
            print " %d found in %d.%d seconds" % (result, elapsed.seconds, elapsed.microseconds)
            
        except AttributeError:
            print " Problem " + problem + " has not been solved yet"
            
    print "-----------------------------------------"
    
if __name__ == '__main__':
    main()
