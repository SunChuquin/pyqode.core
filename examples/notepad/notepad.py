#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
logging.basicConfig(level=logging.INFO)
import os
os.environ['QT_API'] = 'pyside2'
# os.environ['QT_API'] = 'pyqt5'
from notepad import main

if __name__ == '__main__':
    main()
