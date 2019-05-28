#!/usr/bin/python3

import os
import sys
import zipfile

def do_extract(filename, outdir):
    zf = zipfile.ZipFile(filename)
    members = zf.namelist()
    members.sort()
    found_xml_invalid_ind = False
    for member, i in zip(members, range(0, len(members))):
        s = zf.open(member).read().decode('UTF-8')
        if '</hanafoda/>' in s:
            print('Found XML format bug in %s. Correcting...' % member)
            s = s.replace('</hanafoda/>', 'hanafuda')
            found_xml_invalid_ind = True
        if '</trump/>' in s:
            print('Found XML format bug in %s. Correcting...' % member)
            s = s.replace('</trump/>', 'trump')
            found_xml_invalid_ind = True
        if '</Platycodon grandiflorus/>' in s:
            print('Found XML format bug in %s. Correcting...' % member)
            s = s.replace('</Platycodon grandiflorus/>',
                          'Platycodon grandiflorus')
            found_xml_invalid_ind = True
        if '</bellflower/>' in s:
            print('Found XML format bug in %s. Correcting...' % member)
            s = s.replace('</bellflower/>', 'bellflower')
            found_xml_invalid_ind = True
        if '</sailfin sandfish/>' in s:
            print('Found XML format bug in %s. Correcting...' % member)
            s = s.replace('</sailfin sandfish/>', 'sailfin sandfish')
            found_xml_invalid_ind = True
        if 'val="<i>perilla</i>, biji <i>perilla</i>"' in s:
            print('Found XML format bug in %s. Correcting...' % member)
            s = s.replace('val="<i>perilla</i>, biji <i>perilla</i>"',
                          'val="perilla, biji perilla"')
            found_xml_invalid_ind = True
        if 'val="Их хаан<BR/>' in s:
            print('Found XML format bug in %s. Correcting...' % member)
            s = s.replace('val="Их хаан<BR/>', 'val="Их хаан&#xA;')
            found_xml_invalid_mon = True
        with open(os.path.join(outdir, str(i) + '.xml'), 'w') as fp:
            fp.write(s)
    if not found_xml_invalid_ind:
        print('WARNING: XML invalid on indonesian not found. ' +
              'Check if upstream fixed it.')
    if not found_xml_invalid_mon:
        print('WARNING: XML invalid on mongolian not found. ' +
              'Check if upstream fixed it.')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write('Usage: %s filename.zip' % sys.argv[0])
        sys.exit(1)
    filename = sys.argv[1]
    outdir = './upstream'
    do_extract(filename, outdir)
