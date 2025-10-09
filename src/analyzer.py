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
        
def get_spending_analysis(self):
        """
        Analyze spending patterns across different categories.
        
        Returns:
            dict: Comprehensive spending analysis
        """
        if self.data.empty:
            return {"error": "No data available"}
        
        # Find spending columns (any column with 'spending' in the name)
        spending_cols = [col for col in self.data.columns if 'spending' in col.lower()]
        
        if not spending_cols:
            return {"error": "No spending data found"}
        
        # Create empty analysis dictionary
        analysis = {
            "Spending Overview": {},
            "Category Breakdown": {},
            "Insights": []
        }
        
        # Calculate total spending per person
        self.data['total_spending'] = self.data[spending_cols].sum(axis=1)
        
        # Overall spending statistics
        analysis["Spending Overview"] = {
            "Average Total Spending": format_currency(self.data['total_spending'].mean()),
            "Median Total Spending": format_currency(self.data['total_spending'].median()),
            "Spending Range": f"{format_currency(self.data['total_spending'].min())} - {format_currency(self.data['total_spending'].max())}"
        }
        
        return analysis
    
# Category breakdown
        for col in spending_cols:
            category_name = col.replace('monthly_spending_', '').replace('_', ' ').title()
            analysis["Category Breakdown"][category_name] = {
                "Average": format_currency(self.data[col].mean()),
                "Percentage of Total": format_percentage(
                    self.data[col].sum() / self.data['total_spending'].sum()
                )
            }
        
        # Generate insights
        if spending_cols:
            # Find highest spending category
            category_totals = {
                col.replace('monthly_spending_', '').title(): self.data[col].sum() 
                for col in spending_cols
            }
            highest_category = max(category_totals, key=category_totals.get)
            analysis["Insights"].append(f"Highest spending category: {highest_category}")
            
            # Spending vs income ratio
            if 'annual_income' in self.data.columns:
                monthly_income = self.data['annual_income'] / 12
                spending_ratio = (self.data['total_spending'] / monthly_income).mean()
                analysis["Insights"].append(
                    f"Average spending-to-income ratio: {format_percentage(spending_ratio)}"
                )