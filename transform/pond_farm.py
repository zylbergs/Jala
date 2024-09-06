import pandas as pd

def trans_pond():
    #pond + farm Transform
    pon = pd.read_csv(r"Source\Data\ponds.csv")
    far = pd.read_csv(r"Source\Data\farms.csv")
    pon.farm_id = pon.farm_id.astype(str)
    pon.id = pon.id.astype(str)
    pon.rename(columns={'id':'pond_id'},inplace=True)

    pon.created_at = pd.to_datetime(pon.created_at)
    pon.updated_at = pd.to_datetime(pon.updated_at)
    pon.extracted_at = pd.to_datetime(pon.extracted_at)

    pon.length = pon.length.astype(float)
    pon.width = pon.width.astype(float)
    pon.deep = pon.deep.astype(float)
    pon.max_seed_density = pon.max_seed_density.astype(float)

    far.id = far.id.astype(str)
    far['h_tz'] = far.timezone.str.replace('+','').str.split(':').str[0]
    far['h_tz'] = far['h_tz'].astype(int)
    far['mnt_tz'] = far.timezone.str.replace('+','').str.split(':').str[1]
    far['mnt_tz'] = far['mnt_tz'].astype(int)
    far.rename(columns={'id':'farm_id'},inplace=True)
    #merge pond with farm
    pon_far = pon.merge(far,how='left',on='farm_id')
    pon_far = pon_far[['pond_id','length','width','deep','max_seed_density','province','regency','timezone','h_tz','mnt_tz']]
    return pon_far