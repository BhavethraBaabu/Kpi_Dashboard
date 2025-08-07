# Automated KPI Dashboard Generator

This project allows users to upload a sales CSV or Excel file and automatically generates key performance indicator (KPI) visualizations and a natural language summary of the data.

## Features

- Upload CSV or Excel sales data with columns: Date, New Customers, Churned Customers, Revenue
- Calculate KPIs: Revenue, Churn Rate, Monthly Recurring Revenue (MRR), Growth Percentage
- Visualize KPIs with Matplotlib charts
- Generate a concise KPI summary using Langchain and OpenAI LLM
- Built with Streamlit for an interactive UI

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Set your OpenAI API key:

```bash
export OPENAI_API_KEY='your_api_key_here'
```

Run the Streamlit app:

```bash
streamlit run app.py
```

Upload your CSV or Excel file and see the dashboard and summary.

## Sample CSV format

| Date       | New Customers | Churned Customers | Revenue ($) |
|------------|---------------|-------------------|-------------|
| 2025-01-01 | 50            | 5                 | 5000        |
| 2025-02-01 | 55            | 7                 | 5400        |

## License

MIT License