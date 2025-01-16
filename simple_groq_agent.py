from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
load_dotenv()

def get_company_symbol(company: str) -> str:
    """Use this function to get the symbol for a company.

    Args:
        company (str): The name of the company.

    Returns:
        str: The symbol for the company.
    """
    symbols = {
        "Phidata": "MSFT",
        "Infosys": "INFY",
        "Tesla": "TSLA",
        "Apple": "AAPL",
        "Microsoft": "MSFT",
        "Amazon": "AMZN",
        "Google": "GOOGL",
    }
    return symbols.get(company, "Unknown")

agent=Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True),get_company_symbol],
    show_tool_calls=True,
    markdown=True,
    instructions=["Use Tables to display data",
                  " if u dont know the company symbol pls use get_company_symbol tool even if it is not a public company"],
    debug_mode=True
)
agent.print_response("Summarize and compare the analyst recomendations and fundamentals for TESLA and Phidata")
#does not work for llama but works for paid chatgpt4