import pandas as pd

def trans_meas():
    mea = pd.read_csv(r"Source\Data\measurements.csv")
    mea.cycle_id = mea.cycle_id.astype(str)
    mea.pond_id = mea.pond_id.astype(str)
    mea['measured_date'] = pd.to_datetime(mea['measured_date'])

    mea[['morning_temperature','morning_salinity','morning_pH']].fillna(0,inplace=True)
    #treshold for missing value = 33%
    mea_agg = mea.groupby('cycle_id',as_index=False)\
        .agg({'morning_temperature':'mean','morning_salinity':'mean','morning_pH':'mean'})
    return mea_agg