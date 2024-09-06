import pandas as pd

def trans_fast():
    fas = pd.read_csv(r"Source\Data\fasting.csv")
    fas_s = pd.read_csv(r"Source\Data\fastings.csv")
    #fasting transform
    fast = pd.concat([fas,fas_s])
    fast.logged_date = pd.to_datetime(fast.logged_date)
    fast.cycle_id = fast.cycle_id.astype(str)
    fast.fasting = fast.fasting.astype(str)
    fast.cycle_id = fast.cycle_id.str.split('.').str[0]
    fast.fasting = fast.fasting.str.split('.').str[0]
    fast = fast.drop_duplicates(subset=['logged_date','cycle_id','fasting'])
    fast.fasting.replace('nan','0',inplace=True)
    fast.fasting = fast.fasting.astype(int)
    fast = fast[fast.fasting ==1].sort_values(['cycle_id','logged_date'])
    #feature count of fasting for fast to cycle end ratio
    fast_agg = fast.groupby(['cycle_id'],as_index=False).fasting.sum()

    fast_test = fast.copy()
    for i in fast_test.cycle_id.unique():
        fast_test.loc[fast_test.cycle_id == i,'cons_fast_count'] =  (fast_test[fast_test.cycle_id == i]['logged_date'].diff().dt.days == 1).sum()

    #feature: count of consecutive day
    fast_test = fast_test.drop_duplicates('cycle_id')
    fast_test = fast_test[['cycle_id','cons_fast_count']]
    #adjust +1
    fast_test['cons_fast_count'] = fast_test['cons_fast_count']+1
    fasting = fast_agg.merge(fast_test,how='left',on='cycle_id')
    return fasting