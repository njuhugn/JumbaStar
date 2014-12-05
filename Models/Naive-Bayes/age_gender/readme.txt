To get AUC, you can follow this order:

mapper.py: organize the orginal data to get the columns I am interested
input: ['0.0822', 'train', '0', '1', '11092342671025131053', '20883284', '26561', '2', '1', '11929585', '65174', '1000019', '505595', '0']	\t additional feature
output: value \t featurename \t click \t impression

reducer.py:aggregate the values with the same key
input: value \t featurename \t click \t impression
output:  value \t featurename \t  click \t impression

1_get_prob.py: concert the training data into sample_prob.txt
input:  value \t featurename \t  click \t impression
output:  featurename \t value \t  P(feature=value|click) \t P(feature=value|nonclick)

validation.py: concert validation set into the format I want
input:  ['0.0822', 'train', '0', '1', '11092342671025131053', '20883284', '26561', '2', '1', '11929585', '65174', '1000019', '505595', '0']	\t additional feature
output:  '0.0822'\t 'train'\t '0'\t '1'\t '11092342671025131053'\t '20883284'\t '26561'\t '2'\t '1'\t '11929585'\t '65174'\t '1000019'\t '505595' \t '0'	\t additional feature


2_nb_step2.py: use the sample_prob.txt to apply naive bayes model to get P(click|feature=value) for the validation set
input:  '0.0822'\t 'train'\t '0'\t '1'\t '11092342671025131053'\t '20883284'\t '26561'\t '2'\t '1'\t '11929585'\t '65174'\t '1000019'\t '505595' \t '0'	\t additional feature
output:  featurename \t adid \t value \t  P(click | feature=value) \t click \t impression

3_expend.py: expand what I have for previous step so that each line only has one impression
input:  featurename \t adid \t value \t  P(click | feature=value) \t click \t impression
output:  featurename \t adid \t value \t  P(click | feature=value) \t click \t impression

4_plot_roc.py: calculate the auc
input:  featurename \t adid \t value \t  P(click | feature=value) \t click \t impression
output: auc value



