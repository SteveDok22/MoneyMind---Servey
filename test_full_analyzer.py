from src.data_handler import DataHandler
from src.analyzer import FinanceAnalyzer

print("=" * 60)
print("PERSONAL FINANCE SURVEY ANALYZER - FULL TEST")
print("=" * 60)

# Load data
print("\n📂 Loading data...")
dh = DataHandler()
dh.load_csv('data/sample_survey.csv')

# Create analyzer
analyzer = FinanceAnalyzer(dh.data)

# Test 1: Spending Analysis
print("\n" + "=" * 60)
print("📊 SPENDING ANALYSIS")
print("=" * 60)
spending = analyzer.get_spending_analysis()
for key, value in spending["Spending Overview"].items():
    print(f"{key}: {value}")
print("\n💡 Insights:")
for insight in spending["Insights"]:
    print(f"  • {insight}")

# Test 2: Savings Analysis
print("\n" + "=" * 60)
print("💰 SAVINGS ANALYSIS")
print("=" * 60)
savings = analyzer.get_savings_analysis()
for key, value in savings["Savings Overview"].items():
    print(f"{key}: {value}")
if "Savings Rate Analysis" in savings:
    print("\n📈 Savings Rates:")
    for key, value in savings["Savings Rate Analysis"].items():
        print(f"  {key}: {value}")

# Test 3: Investment & Crypto (FINTECH FOCUS!)
print("\n" + "=" * 60)
print("🪙 CRYPTOCURRENCY & INVESTMENT ANALYSIS")
print("=" * 60)
investment = analyzer.get_investment_analysis()
if "Cryptocurrency Analysis" in investment:
    print("Crypto Stats:")
    for key, value in investment["Cryptocurrency Analysis"].items():
        print(f"  {key}: {value}")
print("\n💡 Insights:")
for insight in investment["Insights"]:
    print(f"  • {insight}")

# Test 4: FinTech Adoption
print("\n" + "=" * 60)
print("📱 FINTECH ADOPTION")
print("=" * 60)
fintech = analyzer.get_fintech_adoption_analysis()
if "Mobile Banking" in fintech:
    for key, value in fintech["Mobile Banking"].items():
        print(f"{key}: {value}")

# Test 5: Financial Literacy
print("\n" + "=" * 60)
print("🎓 FINANCIAL LITERACY")
print("=" * 60)
literacy = analyzer.get_financial_literacy_analysis()
if "Literacy Overview" in literacy:
    for key, value in literacy["Literacy Overview"].items():
        print(f"{key}: {value}")
if "Correlations" in literacy:
    print("\n🔗 Correlations:")
    for key, value in literacy["Correlations"].items():
        print(f"  Literacy vs {key}: {value}")

# Test 6: Comprehensive Report
print("\n" + "=" * 60)
print("📄 COMPREHENSIVE REPORT - EXECUTIVE SUMMARY")
print("=" * 60)
report = analyzer.get_comprehensive_report()
for key, value in report["Executive Summary"].items():
    print(f"{key}: {value}")

print("\n💡 ALL KEY FINDINGS:")
for i, finding in enumerate(report["Key Findings"], 1):
    print(f"  {i}. {finding}")

print("\n" + "=" * 60)
print("✅ FULL ANALYZER TEST COMPLETE!")
print("=" * 60)