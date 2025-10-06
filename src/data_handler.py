"""
Data Handler Module for Personal Finance Survey Analyzer.

This module handles CSV file loading, data validation, and preprocessing
for the personal finance survey analysis application.
"""

import pandas as pd
import os
from src.utils import handle_file_error, display_success_message, display_error_message