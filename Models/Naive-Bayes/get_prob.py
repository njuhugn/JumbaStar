
### get prior probability for each feature for naive bayes
### put "input.txt" in the same directory and run this file directly in terminal.

def find_probability(train):
    click = 0
    impression = 0
    data = [line.strip() for line in open(train)]
    for line in data:
        line = line.strip()
        items = line.split('\t')
        try:
            if len(items) ==4:
                click = click + int(items[3])
                impression = impression + int(items[2])
            no_click = impression - click
        except Exception:
            continue
    
    for line in data:
        line = line.strip()
        items = line.split('\t')
        value = items[1]
        feature_type = items[0]
        P_fea_click = float(items[3])/click
        P_fea_no_click = float(int(items[2])-int(items[3]))/(impression - click)
        if P_fea_no_click == 0:
            P_fea_no_click = 0.0000001
        if P_fea_click == 0:
            P_fea_click = 0.0000001
        if value == "impression<=20":
            value = "UNK"
        print '%s\t%s\t%s\t%s' % (feature_type, value, P_fea_click,\
                                  P_fea_no_click)
    print '%s\t%s\t%s\t%s' % ('Total', 'Total', float(click)/impression,\
                              float(no_click)/impression)
    

find_probability('input.txt')

