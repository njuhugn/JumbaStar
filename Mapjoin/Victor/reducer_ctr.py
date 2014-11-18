from operator import itemgetter
import sys

current_user = None
current_age = None
current_info = [0, 0]

# input comes from STDIN
total = {}
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    if (len(line.split('\t', 1))) == 2:
        user, extra = line.split('\t', 1)
        if current_user == user or current_user == None:
            if len(extra) == 1:
                current_user = user
                current_age = extra
            else:
                current_info[0] += int(extra[2])
                current_info[1] += int(extra[7])


        else:
            if float(current_info[1]) == 0:
                print '%s\t%s' % (current_age, 0.0)
            else:
                print '%s\t%s' % (current_age, [current_info[0], current_info[1]])
            current_user = user
            current_age = extra
            current_info[0] = 0
            current_info[1] = 0

# do not forget to output the last word if needed!
if current_user == user:
    if float(current_info[1]) == 0:
        print '%s\t%s' % (current_age, 0.0)
    else:
        print '%s\t%s' % (current_age, [current_info[0], current_info[1]])
