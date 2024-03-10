import pandas as pd

complete_df = pd.read_csv("complete.csv")
il_br_df = complete_df[(complete_df["site"] == "IL-BR") & (complete_df["sample_depth_min"] == 0)]
il_br_df.to_csv("IL-BR.csv", index=False)