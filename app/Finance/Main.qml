import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material
import QtQuick.Layouts

import Finance

ApplicationWindow {
  id: window
  Material.theme: Material.Dark
  Material.accent: Material.Gray
  width: Screen.width * 0.3
  height: Screen.height * 0.5
  visible: true
  title: qsTr("Finance Manager")

  header: ToolBar {
    Material.primary: "#5c8540"
    RowLayout {
      anchors.fill: parent
      Label {
        text: qsTr("Finance Manager")
        font.pixelSize: 20
        Layout.alignment: Qt.AlignCenter
      }
    }
  }

  ColumnLayout {
    anchors.fill: parent
    TabBar {
      id: tabBar
      Layout.fillWidth: true

      TabButton {
        text: qsTr("Expenses")
        font.pixelSize: Qt.platform.os == "android" ?
          Math.min(window.width, window.height) * 0.04 :
          Math.min(window.width, window.height) * 0.02
        onClicked: stackView.currentIndex = 0
      }

      TabButton {
        text: qsTr("Charts")
        font.pixelSize: Qt.platform.os == "android" ?
          Math.min(window.width, window.height) * 0.04 :
          Math.min(window.width, window.height) * 0.02
        onClicked: stackView.currentIndex = 1
      }
    }
    
    StackLayout {
      id: stackView
      Layout.fillWidth: true
      Layout.fillHeight: true

      Item {
        id: expenseView
        Layout.fillWidth: true
        Layout.fillHeight: true

        FinanceView {
          id: financeView
          anchors.fill: parent
          financeModel: finance_model
        }
      }

      Item {
        id: chartView
        Layout.fillWidth: true
        Layout.fillHeight: true
      }
    }
  }

  FinanceModel {
    id: finance_model
  }
}
