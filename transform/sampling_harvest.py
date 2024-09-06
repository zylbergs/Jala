import pandas as pd
import datetime
import numpy as np

def trans_samhar():
    har = pd.read_csv(r"Source\Data\harvests.csv")
    sam = pd.read_csv(r"Source\Data\samplings.csv")
    #sampling + harvest transform
    #manual correction w/ assum on created_at date
    sam.loc[sam.sampled_at == '1-01-01','sampled_at'] = '2023-10-12'

    sam.updated_at = pd.to_datetime(sam.updated_at,format="%Y-%m-%d %H:%M:%S")
    sam.sampled_at = pd.to_datetime(sam.sampled_at,format="%Y-%m-%d")
    sam.created_at = pd.to_datetime(sam.created_at,format="%Y-%m-%d %H:%M:%S")

    sam.average_weight = sam.average_weight.astype(float)
    sam.id = sam.id.astype(str)
    sam.cycle_id = sam.cycle_id.astype(str)

    sam.cycle_id = sam.cycle_id.str.split('.').str[0]
    sam.id = sam.id.str.split('.').str[0]

    #get last updated sampling record
    sam.sort_values(by=['id','updated_at'],inplace=True)
    sam.drop_duplicates(subset='id',keep='last',inplace=True)
    #get cycle last sample
    sam.sort_values(by=['cycle_id','sampled_at'],inplace=True)
    sam.drop_duplicates(subset='cycle_id',keep='last',inplace=True)

    har.id = har.id.astype(str)
    har.cycle_id = har.cycle_id.astype(str)

    har.cycle_id = har.cycle_id.str.split('.').str[0]
    har.id = har.id.str.split('.').str[0]

    har.updated_at = pd.to_datetime(har.updated_at,format="%Y-%m-%d %H:%M:%S")
    har.created_at = pd.to_datetime(har.created_at,format="%Y-%m-%d %H:%M:%S")
    har.harvested_at = pd.to_datetime(har.harvested_at,format="%Y-%m-%d")
    har.selling_price.fillna(0,inplace=True)

    #get non failed harvest
    har = har[har.status !='Failed']

    #standardize weigth metric
    har['avg_weight_har'] = 1000/har['size']

    #aggregate partial harvest
    har_agg = har.groupby('cycle_id',as_index=False)\
        .agg({'weight':'sum','size':'mean','updated_at':'max','selling_price':'sum'})
    #standardize weigth metric
    har_agg['avg_weight_har'] = 1000/har_agg['size']
    sam_har = har_agg.merge(sam,how='left',on='cycle_id',suffixes=('_har','_sam'))\
        .drop(columns=['created_at','updated_at_sam','updated_at_har','id','remark'])
    
    return sam_har