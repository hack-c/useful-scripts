# Favorite IPython Notebook Imports
# Charles Hack
# <charles.hack@accenture.com>
# 2017

%matplotlib inline
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set_style('whitegrid')
from pylab import rcParams
from datetime import datetime
rcParams['figure.figsize'] = (16,9)
sns.set_context('notebook')
pd.options.display.max_columns = 100
pd.options.display.max_rows = 500

date = datetime.now().strftime('%Y%m%d') # for output filenames