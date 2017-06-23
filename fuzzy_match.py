# Fuzzy Match
# Charlie Hack
# <charles.hack@accenture.com>
# January 2017
#
# Fuzzy match `input` (single-column text file) to `choices`, a single-column text file of possible choices.
# Output file is same # of rows as `input` in the format:
#
# [Input value 1],[Closest match from `choices`],[Confidence 0-100]
# ...
# 
# It's a good idea to filter out matches with confidence < 90. 
#
#

import click
import pandas as pd
from fuzzywuzzy import process

date = datetime.now().strftime('%Y%m%d') # for output filenames


@click.command()
@click.argument('input_path', type=click.Path(exists=True))
@click.argument('choices_path', type=click.Path(exists=True))
@click.option('--outpath', '-o', type=click.Path(exists=False), default=None)
def main(input_path, choices_path, outpath=None):

    choices = list(pd.read_csv(choices_path, header=None).iloc[:,0])
    input   = list(pd.read_csv(input_path, header=None).iloc[:,0])

    if outpath is None:
        orig, ext = os.path.splitext(choices_path)
        outpath = orig + '_Fuzzy_Mapped_v{}'.format(date) + ext

    with open(outpath,'w') as outfile:
        for x in input:
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