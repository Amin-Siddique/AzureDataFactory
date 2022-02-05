import pandas as pd
df = pd.read_csv('country_response.csv')
df.to_parquet('output.parquet')


#import pandas as pd
#df = pd.read_parquet('output.parquet')
#df.to_csv('new.csv')
