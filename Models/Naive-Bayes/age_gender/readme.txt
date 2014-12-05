To get AUC, you can follow this order:

mapper: organize the orginal data to get the columns I am interested
input: ['0.0822', 'train', '0', '1', '11092342671025131053', '20883284', '26561', '2', '1', '11929585', '65174', '1000019', '505595', '0']	\t additional feature
output: value \t featurename \t click \t impression

reducer:aggregate the values with the same key
input: value \t featurename \t click \t impression
output:  featurename \t value \t  click \t impression


