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