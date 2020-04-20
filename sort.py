import pandas as pd
df=pd.read_csv("/Users/khushboosingh/Desktop/Anshu.csv")
df.Anshu_values("Name",axis=0,ascending=True,inplace=True,na_position='last')
print(df)
