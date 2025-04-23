import pandas as pd
import plotly.express as px
import plotly.io as pio

# Step 1: Load the processed dataset
df = pd.read_csv("processed_diet_impact.csv")

# Step 2: Generate Treemap
fig = px.treemap(
    df,
    path=['diet_group', 'sex', 'age_group'],
    values='mean_ghgs',
    color='mean_ghgs',
    color_continuous_scale='RdBu',
    title='Greenhouse Gas Emissions by Diet Type, Gender, and Age Group'
)

# Step 3: Display interactive plot in browser (optional)
fig.show()

# Step 4: Save full interactive HTML
fig.write_html("diet_ghgs_treemap.html", full_html=True, include_plotlyjs='cdn')

# Step 5: Save static PNG image (requires kaleido)
pio.write_image(fig, "diet_ghgs_treemap.png")

print("Treemap HTML and PNG files generated successfully.")