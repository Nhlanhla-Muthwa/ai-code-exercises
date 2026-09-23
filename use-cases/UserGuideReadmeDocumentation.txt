Prompt 1: Project README Generation
Please create a comprehensive README.md file for my project based on the following information:

Project name: DataInsight
Description: A data analysis and visualization framework for scientific data

Key features:
- Data import from various sources (CSV, Excel, SQL, APIs)
- Data cleaning and transformation tools
- Statistical analysis functions
- Interactive visualizations
- Report generation
- Export capabilities

Technologies used: Python, Pandas, NumPy, Matplotlib, Plotly, Jupyter
Installation requirements: Python 3.8+, pip

Project structure:
/datainsight - Main package
/datainsight/io - Data import/export modules
/datainsight/transform - Data transformation tools
/datainsight/analysis - Analysis algorithms
/datainsight/viz - Visualization tools
/datainsight/report - Report generation
/examples - Example notebooks
/tests - Unit tests

Technologies used: [List technologies, frameworks, languages]
Installation requirements: [List prerequisites]

The README should include:
1. Clear project title and description
2. Installation instructions
3. Basic usage examples
4. Features overview
5. Configuration options
6. Troubleshooting section
7. Contributing guidelines
8. License information

Code structure overview:
[Briefly describe main directories/files or paste project structure]

AI Response:
# DataInsight

**DataInsight** is a robust, modular data analysis and visualization framework designed specifically for scientific data. Built on top of industry-standard Python data science libraries, DataInsight streamlines the pipeline from raw data ingestion to publication-ready visualization and automated report generation.

---

## Features Overview

- **Flexible Data Import:** Seamlessly ingest data from various sources including CSV files, Excel spreadsheets, SQL databases, and REST APIs.
- **Data Cleaning & Transformation:** Powerful toolkit for handling missing values, filtering, normalization, and reshaping scientific datasets.
- **Statistical Analysis:** Comprehensive suite of built-in statistical analysis algorithms tailored for scientific research.
- **Interactive Visualizations:** Generate dynamic and publication-quality plots using Matplotlib and Plotly.
- **Automated Report Generation:** Compile analyses, metrics, and figures directly into structured reports.
- **Export Capabilities:** Save your processed datasets, summaries, and visual outputs in multiple formats.

---

## Technologies Used

- **Language:** Python 3.8+
- **Data Manipulation & Compute:** Pandas, NumPy
- **Visualization:** Matplotlib, Plotly
- **Interactive Development:** Jupyter

---

## Installation Requirements

- **Python:** Version 3.8 or higher
- **Package Manager:** `pip`

---

## Installation Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/datainsight.git
   cd datainsight
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install the package and dependencies:
   ```bash
   pip install -e .
   ```

---

## Code Structure Overview

```text
/datainsight          # Main package source code
├── /io               # Data import and export modules
├── /transform        # Data cleaning and transformation tools
├── /analysis         # Statistical analysis algorithms
├── /viz              # Static and interactive visualization tools
└── /report           # Report generation engine
/examples             # Jupyter notebooks demonstrating use cases
/tests                # Unit tests for verification
```

---

## Basic Usage Example

Here is a quick example of how to import data, run a basic statistical analysis, and generate an interactive visualization using DataInsight:

```python
from datainsight.io import load_csv
from datainsight.analysis import calculate_summary_stats
from datainsight.viz import plot_interactive_scatter

# 1. Load your scientific dataset
df = load_csv("experimental_data.csv")

# 2. Compute summary statistics
stats = calculate_summary_stats(df, target_column="sensor_reading")
print(stats)

# 3. Create an interactive visualization
fig = plot_interactive_scatter(df, x="time", y="sensor_reading", title="Sensor Reading Over Time")
fig.show()
```

---

## Configuration Options

DataInsight allows global configuration adjustments via environment variables or a `config.json` file in your root working directory:

- `DATAINSIGHT_CACHE_DIR`: Specifies the directory for caching intermediate computation results (default: `~/.datainsight/cache`).
- `DATAINSIGHT_DEFAULT_PLOT_THEME`: Sets the default styling theme for visualizations (`default`, `dark`, or `publication`).
- `DATAINSIGHT_LOG_LEVEL`: Controls logging verbosity (`DEBUG`, `INFO`, `WARNING`, `ERROR`).

---

## Troubleshooting

- **`ImportError: No module named 'datainsight'`**
  - *Solution:* Ensure you have activated your virtual environment and installed the package in editable mode (`pip install -e .`).
- **Memory Errors with Large Datasets**
  - *Solution:* Utilize DataInsight's chunking options in the `/io` modules to process large CSV or SQL queries in manageable batches.
- **Plotly Figures Not Rendering in Jupyter**
  - *Solution:* Ensure you have the required Jupyter extensions installed or use the renderer configuration: `import plotly.io as pio; pio.renderers.default = 'jupyterlab'`.

---

## Contributing Guidelines

We welcome contributions from the scientific and developer communities! 

1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

Please ensure all new features or bug fixes include corresponding unit tests in the `/tests` directory.

---

## License Information

This project is licensed under the MIT License - see the `LICENSE` file for details.


Prompt 2: Step-by-Step Guide Creation
Please create a step-by-step guide for how to [specific task/process] in our application.

The guide should:
1. Start with any prerequisites or required access
2. Break down the process into clear, numbered steps
3. Include screenshots or code blocks where indicated [Placeholder]
4. Highlight potential issues or common mistakes
5. End with a troubleshooting section for common problems

Process overview:
[Describe the task or provide notes on what the user needs to accomplish]

User experience level: [Beginner/Intermediate/Advanced]

AI RESPONSE:
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


Prompt 3: FAQ Document Generation
Please help me create a comprehensive FAQ document for [project/feature/product].

Basic information:
- [Brief description of what we're creating FAQs for]
- [Target audience]
- [Any specific areas to focus on]

Please include:
1. Questions about getting started
2. Questions about common features and functionality
3. Questions about troubleshooting common issues
4. Questions about [specific area of interest]

For each question, provide a clear, concise answer that would be helpful to our users.

Known issues or common user questions:
[List any specific questions or issues to include]

AI response:
# DataInsight Frequently Asked Questions (FAQ)

Welcome to the DataInsight FAQ document. This guide provides quick answers to common questions regarding installation, core features, troubleshooting, and advanced performance optimization for scientific data analysis.

---

## 1. Getting Started

### Q: What are the minimum system requirements to run DataInsight?
**A:** DataInsight requires Python 3.8 or higher. We recommend at least 8 GB of RAM for standard scientific datasets and 16 GB+ when working with massive multi-gigabyte files. A standard `pip` installation is all that is required to set up the package locally.

### Q: How do I install DataInsight in my virtual environment?
**A:** First, create and activate your virtual environment, then install the package in editable mode from your local repository root:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e .
```

### Q: How do I securely connect DataInsight to an SQL database?
**A:** You should avoid hardcoding credentials in your scripts. Use environment variables for connection strings and retrieve them in your code:
```python
import os
from datainsight.io import load_sql

db_url = os.getenv("DATAINSIGHT_DB_URL")
df = load_sql(db_url, query="SELECT * FROM telemetry_data")
```

---

## 2. Common Features and Functionality

### Q: What data sources are supported out-of-the-box?
**A:** DataInsight supports ingestion from CSV files, Excel spreadsheets (`.xlsx`), SQL databases via SQLAlchemy connectors, and REST APIs using standard JSON payloads through the `/io` module.

### Q: Can I generate publication-quality static plots alongside interactive ones?
**A:** Yes. While Plotly is used for interactive dashboards, DataInsight integrates with Matplotlib to let you toggle renderers or export figures directly into vector formats like SVG and PDF for scientific publications.

### Q: How do I compile my analysis results into a report?
**A:** You can use the `/report` module to automatically compile summary statistics, data tables, and figures into structured PDF or HTML reports using built-in templates.

---

## 3. Troubleshooting Common Issues

### Q: Why am I encountering a `KeyError` when calling specific columns?
**A:** `KeyError` typically happens when a column name contains unexpected whitespace or casing mismatches. Always inspect your active column headers by running `print(df.columns)` prior to executing analysis functions.

### Q: Why are my Plotly interactive figures not rendering inside my Jupyter Notebook?
**A:** This usually occurs if the notebook renderer is not properly configured. Ensure your environment has the required Jupyter widgets installed, or explicitly set the renderer:
```python
import plotly.io as pio
pio.renderers.default = "jupyterlab"
```

### Q: My script throws an `ImportError: No module named 'datainsight'`. How do I fix this?
**A:** This means Python cannot locate the package. Ensure your virtual environment is active and that you installed DataInsight using `pip install -e .` from the root directory.

---

## 4. Performance and Scalability

### Q: How do I handle memory overflow errors when importing massive CSV files?
**A:** Loading massive multi-gigabyte CSV files entirely into RAM will trigger memory overflow errors. To resolve this, use DataInsight's built-in chunking parameter to load and process data iteratively in batches:
```python
from datainsight.io import load_csv_in_chunks

for chunk in load_csv_in_chunks("massive_dataset.csv", chunk_size=50000):
    # Process each chunk iteratively
    processed_chunk = process_data(chunk)
```

### Q: How can I optimize computation speed for heavy statistical algorithms?
**A:** DataInsight leverages NumPy vectorization under the hood. Avoid iterating over DataFrames using `for` loops where possible; instead, use vectorized functions or leverage DataInsight's multi-core parallel processing flags in the `/analysis` module config.

### Q: How do I customize Plotly interactive dashboards for clean exports?
**A:** You can apply global layout templates or update figure properties before exporting to static image formats (PNG, PDF, SVG) for presentations:
```python
fig = plot_interactive_scatter(df, x="time", y="reading")
fig.update_layout(template="plotly_white", font=dict(family="Arial", size=14))
fig.write_image("publication_plot.pdf")
```
