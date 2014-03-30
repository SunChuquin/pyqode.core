# -*- coding: utf-8 -*-
"""
This module contains the API classes used by the code completion mode and
worker.

This module basically defines the Provider interface and implements
a simple provider based ib the document words.
"""
from pyqode.core import settings


class Provider(object):
    """
    This class describes the expected interface for code completion providers.

    You can inherit from this class but this is not required as long as you
    implement a ``complete`` methods which returns the list of
    completions and have correct signature.
    """

    def complete(self, code, line, column, path, encoding, prefix):
        """
        Returns a list of completions.

        A completion is dictionary with the following keys:
            - 'name': name of the completion, this the text displayed and
            inserted when the user select a completion in the list
            - 'icon': an optional icon file name
            - 'tooltip': an optional tooltip string

        :param code: code string
        :param line: line number (1 based)
        :param column: column number (0 based)
        :param path: file path
        :param encoding: file encoding
        :param prefix: completion prefix (text before cursor)

        :returns: A list of completion dicts as described above.
        :rtype: list
        """
        raise NotImplementedError()


class DocumentWordsProvider(object):
    """
    Provides completions based on the document words
    """
    words = {}

    def __init__(self):
        Provider.__init__(self)

    @staticmethod
    def split(txt, seps):
        """
        Splits a text in a meaningful list of words based on a list of word
        separators.

        :param txt: Text to split
        :param seps: List of words separators
        :return: A **set** of words found in the document (excluding
            punctuations, numbers, ...)
        """
        # replace all possible separators with a default sep
        default_sep = seps[0]
        for sep in seps[1:]:
            if sep:
                txt = txt.replace(sep, default_sep)
        # now we can split using the default_sep
        raw_words = txt.split(default_sep)
        words = set()
        for w in raw_words:
            # w = w.strip()
            if w.isalpha():
                words.add(w)
        return sorted(words)

    def complete(self, code, line, column, path, encoding, prefix):
        completions = []
        for w in self.split(code, settings.word_separators):
            completions.append({'name': w})
        return completions