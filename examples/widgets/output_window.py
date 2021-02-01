"""
This example show how to use the OutputWindow widget.
"""
import sys
import os
os.environ['QT_API'] = 'pyside2'
# os.environ['QT_API'] = 'pyqt5'
from pyqode.qt import QtWidgets

from pyqode.core.widgets import OutputWindow


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    win = OutputWindow()
    win.resize(800, 600)
    win.start_process(sys.executable, ['interactive_process.py'])
    win.show()
    app.exec_()
