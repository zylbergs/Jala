import pandas as pd 
import datetime
import numpy as np

def trans_cycle():
    cyc = pd.read_csv(r"Source\Data\cycles.csv")
    # cyc transform
    cyc.id = cyc.id.astype(str) 
    cyc.pond_id = cyc.pond_id.astype(str) 
    cyc.species_id = cyc.species_id.astype(str)
    #drop dupe assume cycle is unique
    cyc = cyc.drop_duplicates(subset='id')

    cyc.started_at = pd.to_datetime(cyc.started_at)
    cyc.finished_at = pd.to_datetime(cyc.finished_at)
    cyc.created_at = pd.to_datetime(cyc.created_at)
    cyc.updated_at = pd.to_datetime(cyc.updated_at)
    cyc.extracted_at = pd.to_datetime(cyc.extracted_at)
    cyc.ordered_at = pd.to_datetime(cyc.ordered_at)
    cyc.finished_at.fillna(datetime.datetime.now(),inplace=True)

    cyc.species_id = cyc.species_id.replace('nan',np.nan)

    cyc['cyc_dur'] = cyc.finished_at - cyc.started_at
    cyc['cyc_dur'] = cyc['cyc_dur'].astype(str)
    cyc['cyc_dur'] = cyc['cyc_dur'].str.split(' ').str[0]
    cyc['cyc_dur'] = cyc['cyc_dur'].astype(int)
    cyc.rename(columns={'id':'cycle_id'},inplace=True)
    return cyc