"""
user   gender age

        1. Click
        2. Impression
        3. DisplayURL
        4. AdID
        5. AdvertiserID
        6. Depth
        7. Position
        8. QueryID
        9. KeywordID
        10. TitleID
        11. DescriptionID
        12. UserID
"""

import sys
import book_rating_lib

# input comes from STDIN (standard input)

for instance in sys.stdin:
    # remove leading and trailing whitespace
    line = instance.strip()
    line = line.split()
    print '%s\t%s' % (line[0], line[2])
    


"""
python mapper_ctr1.py < smallinstances.txt
python mapper_ctr1.py < smallinstances.txt >  ctrmapper_1_out.txt

sort  usermapper_1_out.txt > userreducer_1_input.txt

python reducer_numbooks_1.py < userreducer_1_input.txt
python reducer_numbooks_1.py < userreducer_1_input.txt > usermapper_2_input.txt

python mapper_numbooks_2.py < usermapper_2_input.txt
python mapper_numbooks_2.py < usermapper_2_input.txt >  usermapper_2_out.txt
sort  usermapper_2_out.txt > userreducer_2_input.txt

python reducer_numbooks_2.py < userreducer_2_input.txt
python reducer_numbooks_2.py < userreducer_2_input.txt > userreducer_2_output.txt

"""

