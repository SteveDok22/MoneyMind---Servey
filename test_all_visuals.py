from src.data_handler import DataHandler
from src.visualizer import DataVisualizer

print("=" * 60)
print("VISUALIZATION MODULE - FULL TEST")
print("=" * 60)

# Load data
print("\n📂 Loading data...")
dh = DataHandler()
dh.load_csv('data/sample_survey.csv')

# Create visualizer
viz = DataVisualizer(dh.data)

# Test each visualization
print("\n" + "=" * 60)
print("Creating individual chart sets...")
print("=" * 60)

print("\n1️⃣ Spending Charts...")
viz.create_spending_charts()

print("\n2️⃣ Savings Charts...")
viz.create_savings_charts()

print("\n3️⃣ Investment Charts...")
viz.create_investment_charts()

print("\n4️⃣ Financial Literacy Charts...")
viz.create_financial_literacy_charts()

print("\n5️⃣ Comprehensive Dashboard...")
viz.create_comprehensive_dashboard()

# Test export all
print("\n" + "=" * 60)
print("Exporting all charts to files...")
print("=" * 60)
viz.export_all_charts()

print("\n" + "=" * 60)
print("✅ ALL VISUALIZATIONS COMPLETE!")
print("=" * 60)
print("\nCheck the 'exports/charts/' folder for saved files!")