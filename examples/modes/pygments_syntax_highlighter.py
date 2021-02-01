"""
Minimal example showing the use of the AutoCompleteMode.
"""
import logging
logging.basicConfig(level=logging.DEBUG)
import sys
import os
os.environ['QT_API'] = 'pyside2'
# os.environ['QT_API'] = 'pyqt5'

from pyqode.qt import QtWidgets
from pyqode.core.api import CodeEdit, ColorScheme
from pyqode.core.backend import server
from pyqode.core.modes import PygmentsSH


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    editor = CodeEdit()
    editor.backend.start(server.__file__)
    editor.resize(800, 600)
    sh = editor.modes.append(PygmentsSH(editor.document()))
    sh.color_scheme = 'monokai'
    editor.file.open(__file__)
    editor.show()
    app.exec_()
    editor.close()
    del editor
    del app
