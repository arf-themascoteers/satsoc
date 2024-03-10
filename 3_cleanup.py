import pandas as pd

complete_df = pd.read_csv("IL-BR.csv")
filtered_columns = ["location_id", "X", "Y", "SOCc"]
complete_df = complete_df[filtered_columns]
complete_df.to_csv("cleaned.csv", index=False)