"""
Data Handler Module for Personal Finance Survey Analyzer.

This module handles CSV file loading, data validation, and preprocessing
for the personal finance survey analysis application.
"""

import pandas as pd
import os
from src.utils import handle_file_error, display_success_message, display_error_message

class DataHandler:
    """Handles data loading, validation, and preprocessing operations."""
    
    def __init__(self):
        """Initialize the DataHandler."""
        self.data = None
        self.original_data = None
        self.data_info = {}
        
def load_csv(self, file_path):
        """
        Load CSV file and perform initial validation.
        
        Args:
            file_path (str): Path to the CSV file
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Check if file exists
            if not os.path.exists(file_path):
                display_error_message(f"File not found: {file_path}")
                return False
                
            # Load the CSV file
            self.data = pd.read_csv(file_path)
            self.original_data = self.data.copy()
            
            # Validate the loaded data
            if self._validate_data_structure():
                self._generate_data_info()
                display_success_message(f"Successfully loaded {len(self.data)} records")
                return True
            else:
                return False
                
        except Exception as e:
            handle_file_error(e, file_path)
            return False
        
def _validate_data_structure(self):
        """
        Validate that the CSV has required columns.
        
        Returns:
            bool: True if data structure is valid
        """
        required_columns = [
            'respondent_id', 'age', 'annual_income', 'monthly_savings',
            'uses_mobile_banking', 'owns_crypto', 'primary_investment'
        ]
        
        missing_columns = [col for col in required_columns if col not in self.data.columns]
        
        if missing_columns:
            display_error_message(f"Missing required columns: {missing_columns}")
            return False
            
        # Check if data is not empty
        if len(self.data) == 0:
            display_error_message("CSV file is empty")
            return False
            
        # Validate data types and clean data
        self._clean_data()
        
        return True