#Author: Victor Jiang


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
            if len(items) ==4:
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

        if float(items[3]) < 20:
            unkclick += float(items[2])
            unkimp += float(items[3])
        else:
            P_fea_click = (float(items[2])+1)/(click+total)
            P_fea_no_click = (float(items[3])-float(items[2])+1)/(impression - click+total)
            print '%s\t%s\t%s\t%s' % (feature_type, value, P_fea_click,\
                                      P_fea_no_click)
    temp = float(unkimp) - float(unkclick)
    print '%s\t%s\t%s\t%s' % ('ad_ctr', 'UNK', float(unkclick)/float(click),\
                              temp/(float(impression)-click))
    print '%s\t%s\t%s\t%s' % ('Total', 'Total', float(click)/impression,\
                              float(no_click)/impression)
    

find_probability('part')


