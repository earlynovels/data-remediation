#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 11:36:29 2018

Standardized Fields Report:
    -For purposes of data remediation and quality control
    -Uses Beautiful Soup to generate a .txt report on an xml file of END data 
    -Checks all END-cataloger fields that are supposed to contain control terms
    -Returns sorted set of responses so it's easy to identify duplicates, typos, and outliers
       
To do:
    -include separate reports for fields (710, 246) that require special indicators
    -consider creating dictionary of standard terms 
    
@author: Alice McGrath
"""

from bs4 import BeautifulSoup


# =============================================================================
# functions
# =============================================================================
# returns a sorted list of every value in a given field and subfield
def get_list(tag, code):
    content_list = []
    fields = soup.find_all(tag="%s" % tag)
    for field in fields:
        subfield = field.find_all(code="%s" % code)
        for s in subfield:
            text = s.get_text()
            content_list.append(text)
    content_list = sorted(set(content_list))
    return(content_list)

# =============================================================================
# script
# =============================================================================

current_date = "6 November 2018"

infile = "~/data-remediation/new-records-09072018.xml"

outfile = "!/Desktop/Soup/control-rept.txt"

with open(infile) as fp:
    soup = BeautifulSoup (fp, "xml")

# fields and subfields in END dataset with limited or controlled terms
st_fields = {'246': ['d', 'g'],
             '250': ['b', 'c'],
             '260': ['a', 'c'],
             '300': ['x'],
             '520': ['a', 'c'],
             '592': ['a', 'b', 'c'],
             '594': ['b'],
             '595': ['a', 'b'],
             '596': ['a', 'c', 'd'],
             '599': ['a', 'b', '3', '5', '6'],
             '656': ['a', 'b'],
             '700': ['4', '5'],
             '710': ['4', '5'],
             '999': ['a', 'b', 'c', 'd']
             }

with open(outfile, 'w') as f:
    f.write("Standardized field report\n%s\n%s\n\n" % (infile, current_date))
    for key in st_fields:
        f.write("\nField: %s\n" % key)
        for value in st_fields[key]:
            contents = get_list(key, value)
            f.write("\n  %s-%s \n" % (key, value))
            for c in contents:
                f.write("     %s\n" % c)          

f.close()
