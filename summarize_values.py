# Print DataFrame Fill Rates and Top Values
# For easy pasting to Excel
# Charlie Hack, 3/24/17
# <charles.hack@accenture.com>
# 
# First run the below definitions in a notebook cell, then do
#
# In [1]: summarize(df)
#
# Paste the output into a text editor first to strip formatting
# Then paste to excel! Voila, a summary of the contents of the table.
#

import sys
import re
import string
import types
from __future__ import print_function


# text utils borrowed from fuzzywuzzy

PY3 = sys.version_info[0] == 3
bad_chars = str("").join([chr(i) for i in range(128, 256)])  # ascii!
if PY3:
    translation_table = dict((ord(c), None) for c in bad_chars)
    unicode = str

def asciionly(s):
    if PY3:
        return s.translate(translation_table)
    else:
        return s.translate(None, bad_chars)

def force_ascii(s):
    if type(s) is str:
        return asciionly(s)
    elif type(s) is unicode:
        return asciionly(s.encode('ascii', 'ignore'))
    else:
        return force_ascii(unicode(s))


# print fill rates

def fillcount(frame, col):
    return len(frame[col].dropna()) / float(len(frame[col]))

def value_counts_percents(frame, col, top_n=15):
    counts = list(reversed(sorted(frame[col].fillna('NULL').value_counts(normalize=True).to_dict().items(), key=lambda x: x[1])))
    names  = map(lambda x: force_ascii(x[0]), counts)
    total_count = len(frame)
    
    if len(counts) > top_n:
        counts = counts[:top_n]
        names  = names[:top_n]

    out = []
    out.append(total_count)
    out.append(frame[col].nunique())
    out.append(", ".join(names))
    for x in counts:
        out.append(x[1])
    return out

def summarize(subframe, top_n=15):
    print("Data Element", "Fill Rate", "Count", "Unique", "Top {} Values".format(top_n), sep="\t", end="\t")
    print(*("Value {} % of Total".format(x+1) for x in xrange(top_n)), sep="\t")
    for col in subframe.columns:
        row = [col, fillcount(subframe,col)] + value_counts_percents(subframe,col, top_n=top_n)
        print(*row, sep="\t")

