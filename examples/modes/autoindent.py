"""
Minimal example showing the use of the AutoIndentMode.
"""
import logging
logging.basicConfig(level=logging.DEBUG)
import sys
import os
os.environ['QT_API'] = 'pyside2'
# os.environ['QT_API'] = 'pyqt5'

from pyqode.qt import QtWidgets
from pyqode.core.api import CodeEdit
from pyqode.core.backend import server
from pyqode.core.modes import AutoIndentMode


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    editor = CodeEdit()
    editor.backend.start(server.__file__)
    editor.resize(800, 600)
    print(editor.modes.append(AutoIndentMode()))
    editor.show()
    editor.appendPlainText(
        '    Please press "RETURN"; the cursor should align with this line')
    app.exec_()
    editor.close()
    del editor
    del app
