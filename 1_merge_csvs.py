import pandas as pd

locations_df = pd.read_csv("locations.csv")
measurements_df = pd.read_csv("measurements.csv")

locations_df_columns = ["location_id","X","Y"]
measurements_df_columns = ["site", "location_id","sample_depth_min", "SOCc"]

locations_df = locations_df[locations_df_columns]
measurements_df = measurements_df[measurements_df_columns]

complete_df = pd.merge(locations_df, measurements_df, on='location_id', how='inner')
complete_df.to_csv("complete.csv",index=False)
