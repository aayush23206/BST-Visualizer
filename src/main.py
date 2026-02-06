"""Main entry point for BST Visualizer application."""
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

from src.ui.main_window import MainWindow


def main():
    """
    Main entry point for the application.
    Creates and displays the main window.
    """
    # Create Qt application
    app = QApplication(sys.argv)
    
    # Set application metadata
    app.setApplicationName("BST Visualizer")
    app.setApplicationVersion("2.0")
    app.setApplicationDisplayName("BST Visualizer - Professional Edition")
    
    # Create and show main window
    window = MainWindow()
    window.show()
    
    # Run application event loop
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
