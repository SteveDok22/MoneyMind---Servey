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