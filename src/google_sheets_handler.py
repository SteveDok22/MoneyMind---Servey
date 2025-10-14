"""
Google Sheets Handler Module for Personal Finance Survey Analyzer.

This module handles integration with Google Sheets API for loading survey data
and storing analysis results in the cloud.
"""

import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
from datetime import datetime
from src.utils import (
    display_success_message, 
    display_error_message, 
    display_loading_message
)


class GoogleSheetsHandler:
    """Handles Google Sheets API integration for data management."""
    
    # Define the scope for Google Sheets and Google Drive access
    SCOPE = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
    ]
    
    def __init__(self, credentials_file='creds.json'):
        """
        Initialize Google Sheets handler.
        
        Args:
            credentials_file (str): Path to the credentials JSON file
        """
        self.credentials_file = credentials_file
        self.client = None
        self.spreadsheet = None
        self.connected = False
        
    def connect(self):
        """
        Establish connection to Google Sheets API.
        
        Returns:
            bool: True if connection successful, False otherwise
        """
        try:
            display_loading_message("Connecting to Google Sheets...")
            
            # Load credentials from the JSON file
            creds = Credentials.from_service_account_file(
                self.credentials_file,
                scopes=self.SCOPE
            )
            
            # Authorize the client
            self.client = gspread.authorize(creds)
            self.connected = True
            
            display_success_message("Successfully connected to Google Sheets!")
            return True
            
        except FileNotFoundError:
            display_error_message(f"Credentials file not found: {self.credentials_file}")
            display_error_message("Please ensure creds.json is in the project root directory")
            return False
        except Exception as e:
            display_error_message(f"Failed to connect to Google Sheets: {str(e)}")
            return False
        
    def load_survey_data(self, worksheet_name='survey_data'):
        """
        Load survey data from a Google Sheets worksheet.
        
        Args:
            worksheet_name (str): Name of the worksheet containing survey data
            
        Returns:
            pd.DataFrame or None: Survey data as DataFrame, or None if error
        """
        if not self.spreadsheet:
            display_error_message("No spreadsheet opened. Call open_spreadsheet() first.")
            return None
        
        try:
            display_loading_message(f"Loading data from worksheet: {worksheet_name}...")
            
            # Get the worksheet
            worksheet = self.spreadsheet.worksheet(worksheet_name)
            
            # Get all values from the worksheet
            data = worksheet.get_all_values()
            
            if not data or len(data) < 2:
                display_error_message("Worksheet is empty or has no data")
                return None
            
            # Convert to DataFrame (first row as headers)
            df = pd.DataFrame(data[1:], columns=data[0])
            
            # Convert numeric columns
            numeric_columns = [
                'age', 'annual_income', 'monthly_savings', 
                'financial_literacy_score', 'emergency_fund_months'
            ]
            
            spending_cols = [col for col in df.columns if 'spending' in col.lower()]
            numeric_columns.extend(spending_cols)
            
            for col in numeric_columns:
                if col in df.columns:
                    df[col] = pd.to_numeric(df[col], errors='coerce')
            
            # Convert boolean columns
            boolean_columns = ['uses_mobile_banking', 'owns_crypto']
            for col in boolean_columns:
                if col in df.columns:
                    df[col] = df[col].str.lower().map({'yes': True, 'no': False})
            
            display_success_message(f"Loaded {len(df)} records from Google Sheets!")
            return df
            
        except gspread.exceptions.WorksheetNotFound:
            display_error_message(f"Worksheet '{worksheet_name}' not found")
            return None
        except Exception as e:
            display_error_message(f"Error loading data: {str(e)}")
            return None