import pandas as pd
import plotly.express as px
import plotly.io as pio
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

# === Step 1: Load the processed data ===
file_path = "processed_diet_impact.csv"
df = pd.read_csv(file_path)

# === Step 2: Normalize metrics (0-1 range) for comparison ===
metrics = [
    'mean_ghgs', 'mean_land', 'mean_watscar', 'mean_watuse',
    'mean_acid', 'mean_eut', 'mean_bio', 'mean_ghgs_ch4', 'mean_ghgs_n2o'
]

scaler = MinMaxScaler()
df_scaled = df.copy()
df_scaled[metrics] = scaler.fit_transform(df[metrics])

# === Step 3: Encode 'diet_group' as numeric for coloring ===
le = LabelEncoder()
df_scaled['diet_code'] = le.fit_transform(df_scaled['diet_group'])

# === Step 4: Generate parallel coordinates plot ===
fig = px.parallel_coordinates(
    df_scaled,
    dimensions=metrics,
    color='diet_code',  # use numeric color
    labels={col: col.replace("mean_", "").upper() for col in metrics},
    title="Environmental Impact by Diet Type (Normalized)",
    color_continuous_scale=px.colors.qualitative.Set1,
)

# Show in browser if needed
fig.show()

# Save fully functional HTML
fig.write_html("diet_parallel_plot.html", full_html=True, include_plotlyjs='cdn')

# Step 5: Save static PNG image (requires kaleido)
pio.write_image(fig, "diet_parallel_plot.png")

print("Interactive plot saved as full HTML. Open it via Chrome for full interactivity.")