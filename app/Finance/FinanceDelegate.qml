import QtQuick
import QtQuick.Layouts
import QtQuick.Controls
import QtQuick.Controls.Material

ItemDelegate {
  id: delegate
  checkable: true
  width: parent.width
  height: Qt.platform.os == "android" ?
    Math.min(window.width, window.height) * 0.15 :
    Math.min(window.width, window.height) * 0.1

  contentItem:
  RowLayout {
    Label {
      id: dateLabel
      font.pixelSize: Qt.platform.os == "android" ?
        Math.min(window.width, window.height) * 0.03 :
        Math.min(window.width, window.height) * 0.02
      text: date
      elide: Text.ElideRight
      Layout.fillWidth: true
      Layout.preferredWidth: 1
      color: Material.primaryTextColor
    }
  }
}
