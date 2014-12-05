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
    for line in data:
        line = line.strip()
        items = line.split('\t')
        try:
            if len(items) == 4:
                click = click + float(items[2])
                impression = impression + float(items[3])
                total += 1
            no_click = impression - click
        except Exception:
            continue
    for line in data:
        line = line.strip()
        items = line.split('\t')
        value = items[0]
        feature_type = items[1]
        current = feature_type
        if float(items[3]) < 20:
            unkclick += float(items[2])
            unkimp += float(items[3])
        else:
            P_fea_click = float((float(items[2])+1)/(click+total))
            P_fea_no_click = float((float(items[3])-float(items[2])+1)/(impression - click+total))
            print '%s\t%s\t%s\t%s' % (feature_type, "{0:.5f}".format(float(value)), P_fea_click,\
                                      P_fea_no_click)
    temp = float(unkimp) - float(unkclick)
    a=float(unkclick)/float(click)
    b=temp/(float(impression)-click)
    c=float(click)/impression
    d=float(no_click)/impression
    print '%s\t%s\t%s\t%s' % (current, 'UNK', "{0:.5f}".format(a),"{0:.5f}".format(b))
    print '%s\t%s\t%s\t%s' % ('Total', 'Total', "{0:.5f}".format(c),"{0:.5f}".format(d))
    

find_probability('part0')

