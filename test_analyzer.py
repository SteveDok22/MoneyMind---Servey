from src.data_handler import DataHandler
from src.analyzer import FinanceAnalyzer

# Load data
dh = DataHandler()
dh.load_csv('data/sample_survey.csv')

# Create analyzer
analyzer = FinanceAnalyzer(dh.data)

# Test spending analysis
print("\n=== SPENDING ANALYSIS ===")
spending = analyzer.get_spending_analysis()
print(spending["Spending Overview"])
print("\nInsights:", spending["Insights"])

# Test investment analysis
print("\n=== INVESTMENT ANALYSIS ===")
investment = analyzer.get_investment_analysis()
print(investment["Cryptocurrency Analysis"])

print("\n=== TEST COMPLETE ===")