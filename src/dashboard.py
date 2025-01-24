import streamlit as st
import pandas as pd
from dotenv import load_dotenv
from .modules.generate_insights import generate_insights
from .modules.generate_graphs import plot_call_distribution, plot_call_ratio

load_dotenv()


class Dashboard:
    def __init__(self):
        pass

    def run(self):
        st.set_page_config(page_title="Customer Support Dashboard", layout="wide")
        st.title("📈 Customer Support Dashboard")

        st.header("⤳ Call Trends Over Time")
        data = pd.read_csv("./src/data/call_center_data.csv")
        data["Answer Rate"] = data["Answer Rate"].str.rstrip("%").astype(float) / 100

        incoming_avg = data["Incoming Calls"].mean()
        answered_avg = data["Answered Calls"].mean()
        ans_rate_avg = data["Answer Rate"].mean()

        col1, col2, col3 = st.columns(3)
        col1.metric("📞 Incoming Calls AVG", round(incoming_avg))
        col2.metric("✅ Answered Calls AVG", round(answered_avg))
        col3.metric("📈 Average Answer Rate", f"{round(ans_rate_avg * 100, 1)}%")

        st.line_chart(data[["Incoming Calls", "Answered Calls"]])

        st.header("⤳ Call Distribution")
        plot_call_distribution(data)

        st.header("⤳ Call Ratio")
        plot_call_ratio(data)

        self.ai_report(data)

    def ai_report(self, data):
        st.header("🤖 AI Insights")
        response = generate_insights(data)
        report_message = response.text
        st.markdown(report_message)
