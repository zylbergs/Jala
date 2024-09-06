import pandas as pd

def trans_meas():
    mea = pd.read_csv(r"Source\Data\measurements.csv")
    mea.cycle_id = mea.cycle_id.astype(str)
    mea.pond_id = mea.pond_id.astype(str)
    mea['measured_date'] = pd.to_datetime(mea['measured_date'])
    #bak df
    mea_ori = mea.copy()
    mea[['morning_temperature', 'evening_temperature', 'morning_do',
        'evening_do', 'morning_salinity', 'evening_salinity', 'morning_pH',
        'evening_pH', 'transparency', 'turbidity', 'ammonia', 'nitrate',
        'nitrite', 'alkalinity', 'hardness', 'calcium', 'magnesium',
        'carbonate', 'bicarbonate', 'tom', 'total_plankton_']] = mea[['morning_temperature', 'evening_temperature', 'morning_do',
        'evening_do', 'morning_salinity', 'evening_salinity', 'morning_pH',
        'evening_pH', 'transparency', 'turbidity', 'ammonia', 'nitrate',
        'nitrite', 'alkalinity', 'hardness', 'calcium', 'magnesium',
        'carbonate', 'bicarbonate', 'tom', 'total_plankton_']].fillna(0)

    mea_agg = mea.groupby('cycle_id',as_index=False).agg({'morning_temperature':'mean',
                                                        'evening_temperature':'mean',
                                                        'morning_do':'mean',
                                                        'morning_salinity':'mean',
                                                        'evening_salinity':'mean',
                                                        'morning_pH':'mean',
                                                        'evening_pH':'mean',
                                                        'transparency':'mean',
                                                        'turbidity':'mean',
                                                        'ammonia':'mean',
                                                        'nitrate':'mean',
                                                        'nitrite':'mean',
                                                        'alkalinity':'mean',
                                                        'hardness':'mean',
                                                        'calcium':'mean',
                                                        'magnesium':'mean',
                                                        'carbonate':'mean',
                                                        'bicarbonate':'mean',
                                                        'tom':'mean',
                                                        'total_plankton_':'mean'})
    return mea_agg