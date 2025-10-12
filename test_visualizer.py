from src.data_handler import DataHandler
from src.visualizer import DataVisualizer

print("Loading data...")
dh = DataHandler()
dh.load_csv('data/sample_survey.csv')

print("Creating visualizer...")
viz = DataVisualizer(dh.data)

print("\n📊 Creating spending charts...")
viz.create_spending_charts()

print("\n💰 Creating savings charts...")
viz.create_savings_charts()

print("\n🪙 Creating investment charts...")
viz.create_investment_charts()

print("\n✅ Visualization test complete!")