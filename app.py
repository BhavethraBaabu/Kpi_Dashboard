import os
import pandas as pd
from langchain.chat_models import ChatOpenAI  # ✅ correct import
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def calculate_kpis(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')

    df['MRR'] = df['Revenue']
    df['Customers'] = df['New Customers'].cumsum() - df['Churned Customers'].cumsum()
    df['Churn Rate'] = df['Churned Customers'] / (df['Customers'].shift(1) + 1)
    df['Churn Rate'] = df['Churn Rate'].fillna(0)
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

    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo",   # ✅ correct for chat models
        temperature=0,
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    summary = chain.run(kpi_table=kpi_str)
    return summary
