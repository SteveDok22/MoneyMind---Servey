"""
Personal Finance Survey Analyzer
A command-line application for analyzing personal finance survey data.

This application provides insights into spending patterns, savings behavior,
investment preferences, and fintech adoption among survey respondents.
"""

import os
import sys
from src.data_handler import DataHandler
from src.analyzer import FinanceAnalyzer
from src.visualizer import DataVisualizer
from src.google_sheets_handler import GoogleSheetsHandler
from src.utils import clear_screen, validate_choice


class PersonalFinanceAnalyzer:
    """Main application class for the Personal Finance Survey Analyzer."""
    
    def __init__(self):
        """Initialize the application components."""
        self.data_handler = None
        self.analyzer = None
        self.visualizer = None
        self.sheets_handler = None
        self.data_loaded = False
        self.sheets_connected = False
        self.username = ""
        
    def display_welcome(self):
        """Display welcome message and application information."""
        clear_screen()
        print("=" * 60)
        print("    PERSONAL FINANCE SURVEY ANALYZER")
        print("=" * 60)
        print("\nWelcome to the Personal Finance Survey Analyzer!")
        print("This tool helps you analyze personal finance survey data")
        print("to gain insights into spending patterns, savings behavior,")
        print("and fintech adoption trends.\n")
        
        # Get username
        self.username = input("Please enter your name: ").strip()
        if not self.username:
            self.username = "Guest"
        print(f"\nWelcome, {self.username}!")
        input("\nPress Enter to continue...")
        
    def display_menu(self):
        """Display the main menu options."""
        print("\n" + "=" * 50)
        print("           MAIN MENU")
        print("=" * 50)
        print("📂 DATA SOURCES:")
        print("1. Load Local CSV Data")
        print("2. Connect to Google Sheets")
        print("3. Load Data from Google Sheets")
        print("\n📊 ANALYSIS:")
        print("4. View Data Summary")
        print("5. Analyze Spending Patterns")
        print("6. Compare Income vs Savings")
        print("7. Cryptocurrency & Investment Analysis")
        print("8. Financial Literacy Insights")
        print("9. Generate Complete Report")
        print("\n💾 EXPORT:")
        print("10. Export Analysis Results")
        print("11. Save Results to Google Sheets")
        print("\n🔧 OPTIONS:")
        print("12. View Google Sheets Info")
        print("13. Exit Application")
        print("=" * 50)
        
    def handle_menu_choice(self, choice):
        """Handle user menu selection."""
        actions = {
            '1': self.load_local_data,
            '2': self.connect_google_sheets,
            '3': self.load_google_sheets_data,
            '4': self.view_data_summary,
            '5': self.analyze_spending_patterns,
            '6': self.compare_income_savings,
            '7': self.analyze_crypto_investments,
            '8': self.analyze_financial_literacy,
            '9': self.generate_complete_report,
            '10': self.export_results,
            '11': self.save_to_google_sheets,
            '12': self.view_sheets_info,
            '13': lambda: False
        }
        
        action = actions.get(choice)
        if action:
            return action() if choice != '13' else False
        else:
            print("\n❌ Invalid choice. Please select a number from 1-13.")
            input("Press Enter to continue...")
            return True