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
    print '%s\t%s' % (line[11], [line[0], line[1]])
    


"""
python mapper_ctr1.py < smallinstances.txt
python mapper_ctr1.py < smallinstances.txt >  ctrmapper_1_out.txt
python mapper_ctr2.py < smalluser.txt
python mapper_ctr2.py < smalluser.txt >  ctrmapper_2_out.txt

sort  ctrmapper_1_out.txt  ctrmapper_2_out.txt > ctrreducer_input.txt

python reducer_ctr.py < ctrreducer_input.txt
python reducer_ctr.py < ctrreducer_input.txt > ctrreducer_input_2.txt

python reducer_ctr2.py < ctrreducer_input_2.txt

"""

