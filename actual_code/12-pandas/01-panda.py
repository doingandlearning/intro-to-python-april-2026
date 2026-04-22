import pandas as pd

df = pd.read_csv('bpm.csv')

# Data Familarisation - getting to know the data
print(df.head())
print(df.tail())
print(df.sample(5))
print(df.columns)
print(df.shape)
print(df.info())
print(df.describe())
    

# Add a new column
df["beam_energy_tev"] = df["beam_energy_gev"] / 1000
# df["is_deviation"] = df["position_mm"] > 2.0 or df["position_mm"] < -2.0
df["is_deviation"] = df["position_mm"].abs() >= 2.0
print(df.head())

# Filtering
deviations_df = df[df["is_deviation"]]

# Setting deviation limit to more than 2mm
deviations_df = df[df["position_mm"].abs() >= 2.0]
print(deviations_df.head())
print(deviations_df.shape, df.shape)

# Sorting
sorted_df = df.sort_values("position_mm", ascending=False)
print(sorted_df[["monitor_id", "timestamp", "position_mm"]].head())

# Grouping
summary_df = df.groupby("monitor_id").agg(
    avg_position_mm=("position_mm", "mean"),
    reading_count=("position_mm", "count"),
)
print(summary_df.head())

summary_df.to_csv("summary.csv")
sorted_df[["monitor_id", "is_deviation", "position_mm"]].to_csv("sorted.csv")