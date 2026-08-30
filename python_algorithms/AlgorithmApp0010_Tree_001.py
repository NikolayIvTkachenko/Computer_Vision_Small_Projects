# Tree Decision
# https://kaggle.com/pascalbliem/european-social-survey-ess-8-ed21-201617

# import kagglehub
# Download latest version
# path = kagglehub.dataset_download("pascalbliem/european-social-survey-ess-8-ed21-201617")
# print("Path to dataset files:", path)


import pandas as pd
ess = pd.read_csv('ml_data/ESS8e02.1_F1.csv')
# DtypeWarning: Columns (164) have mixed types. Specify dtype option on import or set low_memory=False.

print(ess.shape)

print(ess.loc[:, 'happy'].head())

print(ess.loc[:, 'happy'].head())

print(ess.loc[:, 'sclmeet'].head())

print("=======================================")
ess = ess.loc[ess['sclmeet'] <= 10, :].copy()
ess = ess.loc[ess['rlgdgr'] <= 10, :].copy()
ess = ess.loc[ess['hhmmb'] <= 50, :].copy()
ess = ess.loc[ess['netusoft'] <= 5, :].copy()
ess = ess.loc[ess['agea'] <= 200, :].copy()
ess = ess.loc[ess['health'] <= 5, :].copy()
ess = ess.loc[ess['happy'] <= 10, :].copy()
ess = ess.loc[ess['eduyrs'] <= 100, :].copy().reset_index(drop=True)

print("======== Разбиение данных ============")

import numpy as np
social = list(ess.loc[:, 'sclmeet'])
happy = list(ess.loc[:, 'happy'])

low_social_happiness = [hap for soc, hap in zip(social, happy) if soc <= 5]
high_social_hapiness = [hap for soc, hap in zip(social, happy) if soc > 5]

meanlower = np.mean(low_social_happiness)
meanhigher = np.mean(high_social_hapiness)

print(f"meanlower = {meanlower}")
print(f"meanhigher = {meanhigher}")












print("=======================================")













