"""
Utility functions for the Personal Finance Survey Analyzer.

This module contains helper functions used across the application
for input validation, screen management, and common operations.
"""

import os
import sys


def clear_screen():
    """Clear the terminal screen for better user experience."""
    os.system('cls' if os.name == 'nt' else 'clear')
    
    def validate_choice(choice, min_val, max_val):
  
     """
    Validate user menu choice.
    
    Args:
        choice (str): User input choice
        min_val (int): Minimum valid value
        max_val (int): Maximum valid value
        
    Returns:
        bool: True if choice is valid, False otherwise
    """
    try:
        choice_int = int(choice)
        return min_val <= choice_int <= max_val
    except ValueError:
        return False


def validate_yes_no(user_input):
    """
    Validate yes/no user input.
    
    Args:
        user_input (str): User input string
        
    Returns:
        bool or None: True for yes, False for no, None for invalid
    """
    user_input = user_input.strip().lower()
    if user_input in ['yes', 'y', '1']:
        return True
    elif user_input in ['no', 'n', '0']:
        return False
    else:
        return None