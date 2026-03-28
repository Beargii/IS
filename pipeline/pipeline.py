import sys
import pandas as pd

month = int(sys.argv[1])


print(month)

print('arguments:', sys.argv)

print(f'hello pipeline, month={month}')

df = pd.DataFrame({"day": [1,2], "num_passengers":[3,4]})
df['month'] = month
print(df.head())



#DataFrame → 轉成檔案 → 存落 disk - output_12.parquet
#df.to_parquet("s3://bucket/data.parquet")
df.to_parquet(f'output_{month}.parquet')    

