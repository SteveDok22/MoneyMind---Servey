"""
Finance Analyzer Module for Personal Finance Survey Analyzer.

This module contains core analysis functions for examining personal finance
survey data including spending patterns, savings behavior, and investment preferences.
"""

import pandas as pd
import numpy as np
from src.utils import format_currency, format_percentage, safe_divide


class FinanceAnalyzer:
    """Core analysis class for personal finance survey data."""
    
    def __init__(self, data):
        """
        Initialize the analyzer with survey data.
        
        Args:
            data (pd.DataFrame): Survey data to analyze
        """
        self.data = data.copy() if data is not None else pd.DataFrame()