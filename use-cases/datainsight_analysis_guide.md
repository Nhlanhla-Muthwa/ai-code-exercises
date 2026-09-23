# Step-by-Step Guide: Importing and Analyzing Scientific Datasets in DataInsight

Welcome to the DataInsight user guide! This tutorial walks you through the end-to-end process of importing a scientific dataset, cleaning the data, performing a statistical analysis, and exporting your findings. 

**User Experience Level:** Intermediate

---

## 1. Prerequisites and Required Access

Before you begin this tutorial, ensure you have met the following requirements:

* **Software Environment:** Python 3.8+ installed with the `datainsight` package installed in your active virtual environment.
* **Access Permissions:** Read/write access to your working local directory where your dataset and output reports will be saved.
* **Sample Data:** A sample CSV or Excel file containing numeric scientific measurements (e.g., sensor telemetry, experimental readings).

---

## 2. Step-by-Step Instructions

Follow these numbered steps to perform your data analysis workflow:

### Step 1: Initialize Your Environment and Import Modules
Open your preferred Python IDE or Jupyter Notebook, create a new script or notebook cell, and import the required modules from the `datainsight` package.

```python
from datainsight.io import load_csv
from datainsight.transform import clean_missing_values
from datainsight.analysis import calculate_summary_stats
from datainsight.viz import plot_interactive_scatter
```

### Step 2: Load Your Scientific Dataset
Use the I/O module to ingest your raw data file into a DataInsight-compatible DataFrame structure.

```python
# Load dataset from local CSV file
df = load_csv("experimental_data.csv")
print(f"Successfully loaded {len(df)} rows of data.")
```
> `[Placeholder: Insert screenshot of Jupyter notebook cell output showing loaded DataFrame preview]`

### Step 3: Clean and Transform the Data
Scientific datasets often contain missing entries or outliers. Use the transformation utilities to sanitize your data before running statistical tests.

```python
# Drop or interpolate missing values in your target sensor column
cleaned_df = clean_missing_values(df, strategy="interpolate", target_column="sensor_reading")
```

### Step 4: Perform Statistical Analysis
Run the built-in analysis functions to extract critical summary metrics from your cleaned dataset.

```python
# Compute summary statistics
stats_results = calculate_summary_stats(cleaned_df, target_column="sensor_reading")
print(stats_results)
```

### Step 5: Generate and Render Interactive Visualizations
Visualize your findings to verify trends and anomalies.

```python
# Create an interactive scatter plot
fig = plot_interactive_scatter(
    cleaned_df, 
    x="time", 
    y="sensor_reading", 
    title="Sensor Readings Over Experimental Time"
)
fig.show()
```
> `[Placeholder: Insert screenshot of the rendered Plotly interactive visualization dashboard]`

---

## 3. Common Mistakes & Potential Issues

* **Incorrect Data Types:** Passing a column containing string or categorical data directly into statistical functions will throw a type error. Always verify your column types using `df.dtypes` prior to analysis.
* **Uncaught Missing Values:** Skipping the cleaning phase (Step 3) can lead to `NaN` propagation across your analysis results and distorted visualization plots.
* **File Path Errors:** Relative file paths can fail if your script is executed from a different directory than your data source. Use absolute paths or check your working directory with `os.getcwd()`.

---

## 4. Troubleshooting

### Problem: `KeyError` when calling columns
* **Cause:** The column name specified in your analysis or visualization function does not match the exact spelling or case in your raw data file.
* **Solution:** Print the column headers using `print(df.columns)` to verify exact naming conventions.

### Problem: Plotly interactive figures fail to render in standard scripts
* **Cause:** Plotly requires an active renderer configured for your environment when running outside of Jupyter notebooks.
* **Solution:** Explicitly set your renderer before calling `fig.show()`:
  ```python
  import plotly.io as pio
  pio.renderers.default = "browser"
  ```

### Problem: Memory warning during large data import
* **Cause:** Ingesting multi-gigabyte CSV or SQL datasets entirely into RAM.
* **Solution:** Use chunking parameters within the `load_csv()` function to process records iteratively in batches.