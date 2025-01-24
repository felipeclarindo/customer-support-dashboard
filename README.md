🌍 [Leia em Português](README.pt-BR.md)

# Customer Support Dashboard

Interactive application developed in Streamlit to analyze and visualize the performance of a customer service center. This dashboard allows users to monitor key metrics such as incoming calls, answered calls, and call rates, as well as generate automated insights through artificial intelligence.

## Functionalities

- **Metrics View**: Displays metrics such as incoming calls, answered calls, and call rates clearly and concisely.
- **Interactive Graphics**: Displays line charts and bars to view trends over time and call distribution.
- **AI Report**: Generates an insights report based on historical data, providing recommendations to improve service performance.

## Technologies Used

- [Streamlit](https://streamlit.io) - For building the web application.
- [Pandas](https://pandas.pydata.org) - For data manipulation and analysis.
- [dotenv](https://pypi.org/project/python-dotenv/) - For environment variable management.
- [Gemini API](https://ai.google.dev/gemini-api/docs) - For generating insights using artificial intelligence.

## Steps for installing and run

1. Clone the repository:

```bash
   git clone https://github.com/felipeclarindo/customer-support-dashboard.git
```

2. Enter directory:

```bash
    cd customer-support-dashboard
```

3. Create a virtual environment:

```bash
python -m venv .venv
```

4. Run the `.bat` file in `.venv/Scripts/activate.bat`.

5. Install the dependencies:

```bash
    pip install -r requirements.txt
```

6. Create an `.env` file at the root of the project based on the [.env example](file./.env.example) and add your OpenAI API key:

```bash
    GEMINI_API_KEY=your_api_key
```

7. Run the dashboard:

```bash
    streamlit run ./main.py
```

8. The dashboard is open in your default browser at:
   - `http://localhost:8501`

## Contribution

Contributions are welcome! If you have suggestions for improvements, feel free to open an issue or submit a pull request.

## Author

**Felipe Clarindo**

- [LinkedIn](https://www.linkedin.com/in/felipeclarindo)
- [Instagram](https://www.instagram.com/lipethecoder)
- [GitHub](https://github.com/felipeclarindo)

## License

This project is licensed under the [GNU Affero License](https://www.gnu.org/licenses/agpl-3.0.html).
