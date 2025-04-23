import pandas as pd

# === Step 1: Load the original dataset ===
file_path = "Results_21Mar2022.csv"  # Modify this path if needed
df = pd.read_csv(file_path)

# === Step 2: Select relevant columns for analysis ===
columns_to_keep = [
    'diet_group', 'sex', 'age_group', 'n_participants',
    'mean_ghgs', 'mean_land', 'mean_watscar', 'mean_watuse',
    'mean_acid', 'mean_eut', 'mean_bio',
    'mean_ghgs_ch4', 'mean_ghgs_n2o'
]

df_selected = df[columns_to_keep]

# === Step 3: Group by diet, sex, and age group, and calculate the mean of each metric ===
grouped_df = df_selected.groupby(['diet_group', 'sex', 'age_group'], as_index=False).mean()

# === Step 4: Round the values to 3 decimal places for clarity ===
grouped_df = grouped_df.round(3)

# === Step 5: Save the processed data to a new CSV file for visualization ===
output_path = "processed_diet_impact.csv"
grouped_df.to_csv(output_path, index=False)

print("Data processing complete! Aggregated dataset saved to:", output_path)