import re
import pep8

__version__ = '0.0.1'

JSON_IMPORT_REGEX = re.compile(r'(import json\b)|(from json\s)', re.IGNORECASE)
U_LITERAL = re.compile(r'(u[\(\[\'\"])', re.IGNORECASE)
RANGE_LITERAL = re.compile(r'(\srange\()', re.IGNORECASE)


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


def main(logical_line, physical_line, line_number, filename):
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
    return results

main.name = 'main'
main.version = __version__
