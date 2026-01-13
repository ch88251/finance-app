import sys
from pathlib import Path
import pytest
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtQuick import QQuickWindow


@pytest.fixture(scope="module")
def qapp():
    """Create QApplication instance for tests."""
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    yield app


@pytest.fixture
def engine(qapp, qtbot):
    """Create and load QML engine with Finance module."""
    from app.finance_model import FinanceModel
    
    engine = QQmlApplicationEngine()
    app_path = Path(__file__).parent.parent / "app"
    engine.addImportPath(str(app_path))
    engine.loadFromModule("Finance", "Main")
    
    assert engine.rootObjects(), "Failed to load QML"
    
    yield engine
    
    # Cleanup
    del engine


def test_finance_manager_title_in_window(engine, qtbot):
    """Test that 'Finance Manager' appears as the window title."""
    root_objects = engine.rootObjects()
    assert len(root_objects) > 0, "No root objects found"
    
    window = root_objects[0]
    assert isinstance(window, QQuickWindow), "Root object is not a QQuickWindow"
    
    # Check window title
    assert window.title() == "Finance Manager", f"Expected 'Finance Manager', got '{window.title()}'"


def test_finance_manager_text_in_header(engine, qtbot):
    """Test that 'Finance Manager' text appears in the header label."""
    root_objects = engine.rootObjects()
    window = root_objects[0]
    
    # Find the Label in the header ToolBar
    label = window.findChild(object, "", Qt.FindChildrenRecursively)
    
    # Search for an object with the text property set to "Finance Manager"
    def find_text_in_children(obj, target_text):
        """Recursively search for object with specific text property."""
        try:
            if hasattr(obj, 'text') and callable(obj.text):
                if obj.text() == target_text:
                    return True
        except:
            pass
        
        # Check if it's a QML object with property
        try:
            text_prop = obj.property("text")
            if text_prop == target_text:
                return True
        except:
            pass
        
        # Recursively check children
        for child in obj.children():
            if find_text_in_children(child, target_text):
                return True
        
        return False
    
    assert find_text_in_children(window, "Finance Manager"), \
        "Text 'Finance Manager' not found in window children"
