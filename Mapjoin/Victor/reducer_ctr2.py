from operator import itemgetter
import sys

current_age = None
current_info = [0, 0]

# input comes from STDIN
total = {}
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    if (len(line.split('\t', 1))) == 2:
        age, extra = line.split('\t', 1)
        if extra[5] != ']':
            temp = extra[4:6]
        else:
            temp = extra[4]

        if current_age == age or current_age == None:
            current_age = age
            current_info[0] += int(extra[1])
            current_info[1] += int(temp)


        else:
            if float(current_info[1]) == 0:
                print '%s\t%s' % (current_age, 0.0)               
            else:
                print '%s\t%s' % (current_age, float(current_info[0])/float(current_info[1]))
            current_age = age
            current_info[0] = int(extra[1])
            current_info[1] = int(temp)

# do not forget to output the last word if needed!
if current_age == age:
    if float(current_info[1]) == 0:
        print '%s\t%s' % (current_age, 0.0)
    else:
        print '%s\t%s' % (current_age, float(current_info[0])/float(current_info[1]))
