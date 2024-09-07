import pandas as pd
import os
import numpy as np
import sys
sys.path.append('../.')
pd.set_option('display.max_columns', None)
import warnings
warnings.filterwarnings('ignore')

def gen_report_sr():
    #report directory
    rep_dir = r'.\report'
    #get the latest feature file
    filename = os.listdir(r'.\feature')[-1]
    df = pd.read_parquet(r'.\feature\{}'.format(filename))
    #export survival rate and avg daily growth rate
    df[df.survival_rate.notnull()][['cycle_id','survival_rate','avg_growth_rate']]\
        .to_excel(rep_dir + r'\SR_ADG_CYCLE.xlsx',index=False)