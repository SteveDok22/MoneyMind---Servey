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