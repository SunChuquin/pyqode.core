# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editor.ui'
#
# Created: Sun Mar 10 19:23:09 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1153, 840)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtGui.QFrame(Form)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.layoutTop = QtGui.QVBoxLayout()
        self.layoutTop.setObjectName("layoutTop")
        self.verticalLayout.addLayout(self.layoutTop)
        self.layoutCenter = QtGui.QHBoxLayout()
        self.layoutCenter.setSpacing(0)
        self.layoutCenter.setContentsMargins(-1, 0, 0, -1)
        self.layoutCenter.setObjectName("layoutCenter")
        self.layoutLeft = QtGui.QHBoxLayout()
        self.layoutLeft.setContentsMargins(0, -1, -1, -1)
        self.layoutLeft.setObjectName("layoutLeft")
        self.layoutCenter.addLayout(self.layoutLeft)
        self.codeEdit = CodeEdit(self.frame)
        self.codeEdit.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.codeEdit.setFrameShape(QtGui.QFrame.NoFrame)
        self.codeEdit.setFrameShadow(QtGui.QFrame.Plain)
        self.codeEdit.setObjectName("codeEdit")
        self.layoutCenter.addWidget(self.codeEdit)
        self.layoutRight = QtGui.QHBoxLayout()
        self.layoutRight.setObjectName("layoutRight")
        self.layoutCenter.addLayout(self.layoutRight)
        self.verticalLayout.addLayout(self.layoutCenter)
        self.layoutBottom = QtGui.QVBoxLayout()
        self.layoutBottom.setObjectName("layoutBottom")
        self.verticalLayout.addLayout(self.layoutBottom)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.actionUndo = QtGui.QAction(Form)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/rc/edit-undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon)
        self.actionUndo.setIconVisibleInMenu(True)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtGui.QAction(Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/rc/edit-redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo.setIcon(icon1)
        self.actionRedo.setIconVisibleInMenu(True)
        self.actionRedo.setObjectName("actionRedo")
        self.actionCopy = QtGui.QAction(Form)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/rc/edit-copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon2)
        self.actionCopy.setIconVisibleInMenu(True)
        self.actionCopy.setObjectName("actionCopy")
        self.actionCut = QtGui.QAction(Form)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/rc/edit-cut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon3)
        self.actionCut.setIconVisibleInMenu(True)
        self.actionCut.setObjectName("actionCut")
        self.actionPaste = QtGui.QAction(Form)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/rc/edit-paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon4)
        self.actionPaste.setIconVisibleInMenu(True)
        self.actionPaste.setObjectName("actionPaste")
        self.actionDelete = QtGui.QAction(Form)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/rc/edit-delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete.setIcon(icon5)
        self.actionDelete.setIconVisibleInMenu(True)
        self.actionDelete.setObjectName("actionDelete")
        self.actionSelectAll = QtGui.QAction(Form)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/rc/edit-select-all.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSelectAll.setIcon(icon6)
        self.actionSelectAll.setIconVisibleInMenu(True)
        self.actionSelectAll.setObjectName("actionSelectAll")
        self.actionFind = QtGui.QAction(Form)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/rc/edit-find.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFind.setIcon(icon7)
        self.actionFind.setIconVisibleInMenu(True)
        self.actionFind.setObjectName("actionFind")
        self.actionFind_and_replace = QtGui.QAction(Form)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/rc/edit-find-replace.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFind_and_replace.setIcon(icon8)
        self.actionFind_and_replace.setIconVisibleInMenu(True)
        self.actionFind_and_replace.setObjectName("actionFind_and_replace")
        self.actionFindPrevious = QtGui.QAction(Form)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/rc/go-up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFindPrevious.setIcon(icon9)
        self.actionFindPrevious.setIconVisibleInMenu(True)
        self.actionFindPrevious.setObjectName("actionFindPrevious")
        self.actionFindNext = QtGui.QAction(Form)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/rc/go-down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFindNext.setIcon(icon10)
        self.actionFindNext.setIconVisibleInMenu(True)
        self.actionFindNext.setObjectName("actionFindNext")
        self.actionIndent = QtGui.QAction(Form)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/rc/format-indent-more.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionIndent.setIcon(icon11)
        self.actionIndent.setIconVisibleInMenu(True)
        self.actionIndent.setObjectName("actionIndent")
        self.actionUnindent = QtGui.QAction(Form)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/rc/format-indent-less.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUnindent.setIcon(icon12)
        self.actionUnindent.setIconVisibleInMenu(True)
        self.actionUnindent.setObjectName("actionUnindent")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUndo.setText(QtGui.QApplication.translate("Form", "Undo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUndo.setToolTip(QtGui.QApplication.translate("Form", "undo last change", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUndo.setShortcut(QtGui.QApplication.translate("Form", "Ctrl+Z", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedo.setText(QtGui.QApplication.translate("Form", "Redo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedo.setToolTip(QtGui.QApplication.translate("Form", "redo the last undo change", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedo.setShortcut(QtGui.QApplication.translate("Form", "Ctrl+Y", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setText(QtGui.QApplication.translate("Form", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setToolTip(QtGui.QApplication.translate("Form", "Copy selection", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setShortcut(QtGui.QApplication.translate("Form", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut.setText(QtGui.QApplication.translate("Form", "Cut", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut.setToolTip(QtGui.QApplication.translate("Form", "Cut the selection", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut.setShortcut(QtGui.QApplication.translate("Form", "Ctrl+X", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setText(QtGui.QApplication.translate("Form", "Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setToolTip(QtGui.QApplication.translate("Form", "Paste text at cursor position", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setShortcut(QtGui.QApplication.translate("Form", "Ctrl+V", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete.setText(QtGui.QApplication.translate("Form", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete.setToolTip(QtGui.QApplication.translate("Form", "Delete selected text", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete.setShortcut(QtGui.QApplication.translate("Form", "Del", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelectAll.setText(QtGui.QApplication.translate("Form", "Select all", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelectAll.setShortcut(QtGui.QApplication.translate("Form", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFind.setText(QtGui.QApplication.translate("Form", "Find", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFind.setToolTip(QtGui.QApplication.translate("Form", "Find text in the document", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFind.setShortcut(QtGui.QApplication.translate("Form", "Ctrl+F", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFind_and_replace.setText(QtGui.QApplication.translate("Form", "Find and replace", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFind_and_replace.setToolTip(QtGui.QApplication.translate("Form", "Find and replace text in document", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFind_and_replace.setShortcut(QtGui.QApplication.translate("Form", "Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFindPrevious.setText(QtGui.QApplication.translate("Form", "Find previous", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFindPrevious.setToolTip(QtGui.QApplication.translate("Form", "Find previous text in document", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFindPrevious.setShortcut(QtGui.QApplication.translate("Form", "Shift+F3", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFindNext.setText(QtGui.QApplication.translate("Form", "Find next", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFindNext.setToolTip(QtGui.QApplication.translate("Form", "Find next text in document", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFindNext.setShortcut(QtGui.QApplication.translate("Form", "F3", None, QtGui.QApplication.UnicodeUTF8))
        self.actionIndent.setText(QtGui.QApplication.translate("Form", "Indent", None, QtGui.QApplication.UnicodeUTF8))
        self.actionIndent.setToolTip(QtGui.QApplication.translate("Form", "Indent selection", None, QtGui.QApplication.UnicodeUTF8))
        self.actionIndent.setShortcut(QtGui.QApplication.translate("Form", "Ctrl+I", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUnindent.setText(QtGui.QApplication.translate("Form", "Unindent", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUnindent.setToolTip(QtGui.QApplication.translate("Form", "Unindent selction", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUnindent.setShortcut(QtGui.QApplication.translate("Form", "Ctrl+Shift+I", None, QtGui.QApplication.UnicodeUTF8))

from pcef.code_edit import CodeEdit
import editor_rc