import pandas as pd

def trans_feed():
    fee = pd.read_csv(r"Source\Data\feeds.csv")
    #feed transform
    fee.cycle_id = fee.cycle_id.astype(str)
    fee.logged_at = fee.logged_at.fillna(method='ffill')
    fee.logged_at = fee.logged_at.str.split('.').str[0]
    fee.logged_at = pd.to_datetime(fee.logged_at,format="%Y-%m-%d %H:%M:%S")

    fee.sort_values(['cycle_id','logged_at'],inplace=True)
    fee['log_date'] = fee.logged_at.dt.date
    fee['log_date'] = pd.to_datetime(fee['log_date'])

    #feature feed qty
    feed_qty = fee.groupby(['cycle_id'],as_index=False).quantity.sum()

    fee_test = fee.groupby(['cycle_id','log_date'],as_index=False)['quantity'].sum().copy()
    for i in fee_test.cycle_id.unique():
        fee_test.loc[fee_test.cycle_id == i,'cons_feed_count'] =  (fee_test[fee_test.cycle_id == i]['log_date'].diff().dt.days == 1).sum()

    #feature: count of consecutive day
    fee_test = fee_test.drop_duplicates('cycle_id')
    fee_test = fee_test[['cycle_id','cons_feed_count']]
    #adjust +1
    fee_test['cons_feed_count'] = fee_test['cons_feed_count']+1

    feed = feed_qty.merge(fee_test,how='left',on='cycle_id')
    return feed