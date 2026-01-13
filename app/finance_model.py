from datetime import datetime
from dataclasses import dataclass
from enum import IntEnum
from collections import defaultdict

from PySide6.QtCore import (QAbstractListModel, QEnum, Qt, QModelIndex, Slot, 
                            QByteArray)
from PySide6.QtQml import QmlElement

QML_IMPORT_NAME = "Finance"
QML_IMPORT_MAJOR_VERSION = 1


@QmlElement
class FinanceModel(QAbstractListModel):

  @QEnum
  class FinanceRole(IntEnum):
    ItemNameRole = Qt.ItemDataRole.DisplayRole

  def __init__(self, parent=None) -> None:
    super().__init__(parent)
    self.m_finances = []
