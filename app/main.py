import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine

from finance_model import FinanceModel

if __name__ == '__main__':
  app = QApplication(sys.argv)
  QApplication.setOrganizationName("QtProject")
  QApplication.setApplicationName("Finance Manager")
  engine = QQmlApplicationEngine()
  engine.addImportPath(Path(__file__).parent)
  engine.loadFromModule("Finance", "Main")

  if not engine.rootObjects():
    sys.exit(-1)

  exit_code = app.exec()
  del engine
  sys.exit(exit_code)
