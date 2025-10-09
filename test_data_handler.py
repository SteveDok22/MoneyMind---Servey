from src.data_handler import DataHandler

# Initialize handler
dh = DataHandler()

# Load data
print("\n=== LOADING DATA ===")
success = dh.load_csv('data/sample_survey.csv')

if success:
    # Get summary
    print("\n=== DATA SUMMARY ===")
    summary = dh.get_data_summary()
    for section, data in summary.items():
        print(f"\n{section}:")
        for key, value in data.items():
            print(f"  {key}: {value}")
    
    # Get validation report
    print("\n=== VALIDATION REPORT ===")
    report = dh.get_data_validation_report()
    print(f"Issues: {report['Data Quality Issues']}")
    print(f"Recommendations: {report['Recommendations']}")
    
    # Filter data
    print("\n=== FILTERING DATA ===")
    filtered = dh.filter_data(min_age=25, max_age=35, owns_crypto=True)
    print(f"Found {len(filtered)} respondents aged 25-35 who own crypto")
    
    # Export
    print("\n=== EXPORTING DATA ===")
    dh.export_cleaned_data('exports/data/cleaned_data.csv')

print("\n=== TEST COMPLETE ===")