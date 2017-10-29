#!/usr/bin/python3

import sys
import zipfile
import xml.etree.ElementTree as ET

def merge_xml(filenames, outfilename):
    xmldata = None
    for filename in filenames:
        root = ET.parse(filename).getroot()
        if xmldata == None:
            xmldata = ET.ElementTree()
            xmldata._setroot(root)
        else:
            entries = root[1].findall('LexicalEntry')
            for e in entries:
                xmldata.getroot()[1].append(e)
    xmldata.write(outfilename, encoding='UTF-8')

if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.stderr.write('Usage: %s outfile.xml infile.xml...' % sys.argv[0])
        sys.exit(1)
    outfilename = sys.argv[1]
    filenames = sys.argv[2:]
    merge_xml(filenames, outfilename)
