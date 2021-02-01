#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Simple server which adds a DocumentWordsProvider to the CodeCompletion worker.

"""
import os
os.environ['QT_API'] = 'pyside2'
# os.environ['QT_API'] = 'pyqt5'
from pyqode.core import backend

if __name__ == '__main__':
    backend.CodeCompletionWorker.providers.append(
        backend.DocumentWordsProvider())
    backend.serve_forever()
