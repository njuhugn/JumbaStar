#Author:Victor Jiang


def find_probability(train):
    click = 0
    impression = 0
    data = [line.strip() for line in open(train)]
    total = 0
    unkclick = 0
    unkimp = 0
    current = None
    value = None
    t=[]
    f=[]
    for line in data:
        line = line.strip()
        items = line.split('\t')
        try:
            if len(items) == 16:
                click = click + float(items[2])
                impression = impression + float(items[3])
                total += 1
            no_click = impression - click
        except Exception:
            continue
    for line in data:
        line = line.strip()
        items = line.split('\t')
        value = items[15]
        feature_type = 'position_depth'
        current = feature_type
        print '%s\t%s\t%s\t%s' % (feature_type, "{0:.5f}".format(float(value)), float(items[2]),\
                                      float(items[3]))
find_probability('vali.txt')

