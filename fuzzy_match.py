import pandas as pd
from fuzzywuzzy import process

choices = list(pd.read_csv('~/projects/coned/ot_analytics/central/case_studies/maximo_location_id.csv', header=None).iloc[:,0])
toms    = list(pd.read_csv('~/projects/coned/ot_analytics/central/case_studies/toms_location_equip.csv', header=None).iloc[:,0])

with open('/Users/charles.hack/projects/coned/ot_analytics/central/case_studies/toms_maximo_mapping.csv','w') as outfile:
    for x in toms[1053:]:
        try:
            choice, confidence = process.extractOne(x, choices)
        except:
            print x, 'FAILED'
            outfile.write(','.join((str(x), 'FAILURE', '0')))
            outfile.write('\n')
            continue
        print x, '-->', choice, confidence
        outfile.write(','.join((x, choice, str(confidence))))
        outfile.write('\n')