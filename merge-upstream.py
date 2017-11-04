#!/usr/bin/python3

import sys

def merge_xml(filenames, outfilename):
    xmldata = None
    header = ''
    footer = ''
    entries = []
    for filename in filenames:
        content = open(filename, encoding='UTF-8').read()
        a = content.find('<LexicalEntry')
        b = content.rfind('</LexicalEntry>')
        if a < 0 or b < 0:
            raise Exception("LexicalEntry not found")
        b += len('</LexicalEntry>')

        if header == '':
            header = content[:a]
            footer = content[b:]

        entries.append(content[a:b])

    with open(outfilename, 'w', encoding='UTF-8') as fp:
        fp.write(header)
        for e in entries:
            fp.write(e)
        fp.write(footer)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.stderr.write('Usage: %s outfile.xml infile.xml...' % sys.argv[0])
        sys.exit(1)
    outfilename = sys.argv[1]
    filenames = sys.argv[2:]
    merge_xml(filenames, outfilename)
