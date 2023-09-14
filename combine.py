import pandas as pd
from tqdm import tqdm

df1 = pd.read_csv('D:/SKTAI/Kaggle Fairytale/merged_clean.tsv', sep='\t', encoding='utf-8')
df2 = pd.read_csv('D:/SKTAI/Kaggle Fairytale/merged_clean_transcom.tsv', sep='\t', encoding='utf-8')

ko = []
for i in tqdm(df1.iloc, total=len(df1)):
    df = df2[df2.en==i.en]
    if df.empty: 
        ko.append('')
        continue
    ko.append(df.iloc[0].ko)

print(*map(len, (ko, df1.story_id.tolist(), df1.en.tolist())))

df3 = pd.DataFrame({'idx': [*range(len(ko))],
                    'story_id': df1.story_id.tolist(), 
                    'en': df1.en.tolist(),
                    'ko': ko}).set_index('idx')

df3.to_csv('D:/SKTAI/Kaggle Fairytale/merged_clean_trans.tsv', sep='\t', encoding='utf-8')