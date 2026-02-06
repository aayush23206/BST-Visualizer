#!/usr/bin/env python
"""
Simple launcher script for BST Visualizer.
Usage: python run.py
"""

import sys
import os

# Add project to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from src.ui.main_window import MainWindow
    from PyQt5.QtWidgets import QApplication
    
    # Create and run application
    app = QApplication(sys.argv)
    app.setApplicationName("BST Visualizer")
    app.setApplicationVersion("2.0")
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())
    
except ImportError as e:
    print(f"Error: Missing dependency - {e}")
    print("\nPlease install dependencies with:")
    print("  pip install -r requirements.txt")
    sys.exit(1)
except Exception as e:
    print(f"Error: Failed to start application - {e}")
    sys.exit(1)
