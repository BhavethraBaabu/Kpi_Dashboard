import os
import pandas as pd
from langchain.llms import OpenAI 
# use langchain_community import
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def calculate_kpis(df):
    # Ensure 'Date' is datetime
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')

    # Calculate MRR (assuming Revenue = monthly recurring revenue)
    df['MRR'] = df['Revenue']

    # Calculate churn rate = churned customers / (previous month customers)
    df['Customers'] = df['New Customers'].cumsum() - df['Churned Customers'].cumsum()
    df['Churn Rate'] = df['Churned Customers'] / (df['Customers'].shift(1) + 1)  # +1 to avoid div0
    df['Churn Rate'] = df['Churn Rate'].fillna(0)

    # Calculate monthly growth % in revenue
    df['Growth'] = df['Revenue'].pct_change().fillna(0) * 100

    return df[['Date', 'Revenue', 'Churn Rate', 'MRR', 'Growth']]

def generate_summary(kpis):
    prompt = PromptTemplate(
        input_variables=["kpi_table"],
        template=(
            "Here is a summary of a startup's monthly KPIs:\n\n{kpi_table}\n\n"
            "Write a clear, concise summary highlighting revenue trends, churn rate, MRR, and growth percentage."
        )
    )
    kpi_str = kpis.tail(3).to_string(index=False)

    llm = OpenAI(
        model="gpt-3.5-turbo",
        temperature=0,
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    summary = chain.run(kpi_table=kpi_str)
    return summary
