"""
This example show you how to use the Terminal widget
"""
import os
os.environ['QT_API'] = 'pyside2'
# os.environ['QT_API'] = 'pyqt5'
from pyqode.qt import QtWidgets

from pyqode.core.widgets import Terminal


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    win = Terminal()
    win.resize(800, 600)
    win.show()
    app.exec_()
