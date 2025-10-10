"""
Data Visualizer Module for Personal Finance Survey Analyzer.

This module handles creating charts and visualizations for the analysis results
using matplotlib and seaborn libraries.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os
from src.utils import create_directory_if_not_exists, display_success_message, display_error_message


class DataVisualizer:
    """Handles data visualization and chart generation."""
    
    def __init__(self, data):
        """
        Initialize the visualizer with survey data.
        
        Args:
            data (pd.DataFrame): Survey data to visualize
        """
        self.data = data.copy() if data is not None else pd.DataFrame()
        self.setup_style()
        
    def setup_style(self):
        """Set up matplotlib and seaborn styling."""
        plt.style.use('default')
        sns.set_palette("husl")
        plt.rcParams['figure.figsize'] = (10, 6)
        plt.rcParams['font.size'] = 10