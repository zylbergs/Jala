import pandas as pd 
import datetime
import numpy as np
pd.set_option('display.max_columns',None)
import warnings
warnings.filterwarnings('ignore')
import sys 
sys.path.append(r'..\.')
from transform import cycle,fasting,feed,measurement,pond_farm,sampling_harvest

def feature_store(gen_version=True):
    """
    gen_version =True if you want to generate versioning features
    """
    cyc = cycle.trans_cycle()
    fas = fasting.trans_fast()
    fee = feed.trans_feed()
    mea = measurement.trans_meas()
    pon = pond_farm.trans_pond()
    sam = sampling_harvest.trans_samhar()

    features = cyc.merge(fas, how='left', on='cycle_id') \
        .merge(fee, how='left', on='cycle_id') \
        .merge(pon, how='left', on='pond_id') \
        .merge(mea, how='left', on='cycle_id') \
        .merge(sam, how='left', on='cycle_id')

    # fill features.species_id with mode
    features.species_id.fillna(features.species_id.mode()[0], inplace=True)

    # fill features.initial_age with min
    features.initial_age.fillna(features.initial_age.min(), inplace=True)

    # fill features.total_seed_type with mode
    features.total_seed_type.fillna(features.total_seed_type.mode()[0], inplace=True)

    # fill features.fasting with 0
    features.fasting.fillna(0, inplace=True)

    # fill features.cons_fast_count with 0
    features.cons_fast_count.fillna(0, inplace=True)

    # fill features.morning_temperature with percentile 50
    features.morning_temperature.fillna(features.morning_temperature.quantile(0.5), inplace=True)

    # fill features.morning_salinity with percentile 50
    features.morning_salinity.fillna(features.morning_salinity.quantile(0.5), inplace=True)

    # fill features.morning_pH with percentile 50
    features.morning_pH.fillna(features.morning_pH.quantile(0.5), inplace=True)

    # fill features.pond_length with percentile 50
    features.pond_length.fillna(features.pond_length.quantile(0.5), inplace=True)

    features.pond_width.fillna(features.pond_width.quantile(0.5), inplace=True)

    features.pond_depth.fillna(features.pond_depth.quantile(0.5), inplace=True)

    # List of column names
    to_drop = [
        "started_at",
        "mnt_tz",
        "timezone",
        "sampled_at",
        "finished_at",
        "h_tz",
        "created_at",
        "updated_at",
        "created_at",
        "updated_at",
        "limit_weight_per_area",
        "target_cultivation_day",
        "target_size",
        "extracted_at",
        "length",
        "width",
        "deep",
        "max_seed_density",
        "province",
        "regency",
        "pond_id",
        "ordered_at"
    ]
    features["total_biocunt"] = features["size"] * features["weight"]
    features["survival_rate"] = features["total_biocunt"] / features["total_seed"]
    # fill na avg_growth_rate with features['size']/features['cyc_dur']
    features["avg_growth_rate"] = features["avg_growth_rate"].fillna(features['size']/features['cyc_dur'])
    features['generated_date'] = datetime.datetime.now()
    features = features.drop(columns=to_drop)
    # write versioning features

    if gen_version:
        version = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        filename = rf".\feature\version_{version}.parquet"
        features.to_parquet(filename, index=False)

    return features