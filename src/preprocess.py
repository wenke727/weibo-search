import pandas as pd
import seaborn as sns


df = pd.read_csv("../result/施工安全/施工安全.csv", parse_dates=['发布时间'])

df.info()

sns.kdeplot(df['发布时间'])