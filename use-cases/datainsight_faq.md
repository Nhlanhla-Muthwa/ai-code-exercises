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