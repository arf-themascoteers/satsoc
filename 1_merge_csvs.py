import pandas as pd

locations_df = pd.read_csv("locations.csv")
measurements_df = pd.read_csv("measurements.csv")

complete_df = pd.merge(locations_df, measurements_df, on='location_id', how='inner')
complete_df.to_csv("complete.csv",index=False)
