"""Image export functionality for tree visualization."""
from typing import Optional
from pathlib import Path


class TreeExporter:
    """
    Handles exporting tree visualization as images.
    Supports multiple formats and quality settings.
    """
    
    def __init__(self):
        """Initialize the tree exporter."""
        self.last_export_path = None
    
    def export_to_image(
        self,
        canvas,
        file_path: str,
        format: str = "PNG",
        scale: float = 2.0
    ) -> bool:
        """
        Export the canvas to an image file.
        
        Args:
            canvas: The canvas object to export (PyQt5 QGraphicsView)
            file_path: Path where to save the image
            format: Image format (PNG, JPG, etc.)
            scale: Scale factor for the exported image
        
        Returns:
            True if export was successful, False otherwise
        """
        try:
            from PyQt5.QtCore import QSize, Qt
            from PyQt5.QtGui import QPixmap, QPainter
            from PyQt5.QtWidgets import QApplication
            
            # Get canvas scene and rect
            scene = canvas.scene()
            if not scene:
                return False
            
            scene_rect = scene.itemsBoundingRect()
            
            # Create pixmap with scale
            size = QSize(
                int(scene_rect.width() * scale),
                int(scene_rect.height() * scale)
            )
            pixmap = QPixmap(size)
            pixmap.fill(Qt.white)
            
            # Render scene to pixmap
            painter = QPainter(pixmap)
            scene.render(painter, source=scene_rect)
            painter.end()
            
            # Save to file
            success = pixmap.save(file_path, format=format.upper())
            
            if success:
                self.last_export_path = file_path
            
            return success
        except Exception as e:
            print(f"Error exporting image: {e}")
            return False
    
    def get_export_formats(self) -> list:
        """
        Get list of supported export formats.
        
        Returns:
            List of format strings
        """
        return ["PNG", "JPG", "BMP", "GIF", "TIFF"]
    
    def validate_path(self, file_path: str) -> bool:
        """
        Validate if the export path is valid.
        
        Args:
            file_path: Path to validate
        
        Returns:
            True if path is valid and writable
        """
        try:
            path = Path(file_path)
            # Check if directory exists or can be created
            path.parent.mkdir(parents=True, exist_ok=True)
            return True
        except Exception:
            return False
    
    def get_last_export_path(self) -> Optional[str]:
        """Get the path of the last successful export."""
        return self.last_export_path
