import re
import pep8
__version__ = '0.0.1'

JSON_IMPORT_REGEX = re.compile(r'(import json\b)|(from json\s)', re.IGNORECASE)
U_LITERAL = re.compile(r'(u[\(\[\'\"])', re.IGNORECASE)
RANGE_LITERAL = re.compile(r'(\srange\()', re.IGNORECASE)
CLASS_DEFINITION = re.compile(r'\s*class\b')
METHOD_DEFINITION = re.compile(r'\s*(def|@\w+)\b')

def check_no_json_import(logical_line, physical_line, line_number, filename):
    '''
    This function enforces that we are not importing the json default library but the simplejson library.
    '''
    match = JSON_IMPORT_REGEX.search(logical_line)
    if match:
        return match.start(), 'SC01 import json found, use import simplejson instead.'


def detect_u_literal(logical_line, physical_line, line_number, filename):
    '''
    This function enforces that we are not using u'str' but instead from __future__ import unicode_literals
    '''
    match = U_LITERAL.search(logical_line)
    if match:
        return match.start(), "SC02 found u'str', please use __future__ import unicode_literals instead."


def detect_range_instead_of_xrange(logical_line, physical_line, line_number, filename):
    '''
    This function enforces that people are using xrange instead of range as xrange is an iterator which
    is more memory efficient.
    '''
    match = RANGE_LITERAL.search(logical_line)
    if match:
        return match.start(), 'SC03 found range method, use xrange instead as xrange is an iterator.'


def detect_missing_blank_line_after_class_definition(logical_line, previous_logical, blank_lines):
    '''
    This function enforces that there is a blank line after a class definition line.
    '''
    match = CLASS_DEFINITION.search(previous_logical)
    if match and blank_lines < 1:
        method_match = METHOD_DEFINITION.search(logical_line)
        if method_match:
            return method_match.start(), 'E309 expected 1 blank lines between class and method definitions, found 0'


def main(logical_line, physical_line, line_number, filename, previous_logical, blank_lines):
    results = []
    if pep8.noqa(physical_line):
        return

    result = check_no_json_import(logical_line, physical_line, line_number, filename)
    if result:
        results.append(result)

    result = detect_u_literal(logical_line, physical_line, line_number, filename)
    if result:
        results.append(result)

    result = detect_range_instead_of_xrange(logical_line, physical_line, line_number, filename)
    if result:
        results.append(result)

    result = detect_missing_blank_line_after_class_definition(logical_line, previous_logical, blank_lines)
    if result:
        results.append(result)

    return results

main.name = 'starscream-flake8-plugin'
main.version = __version__
