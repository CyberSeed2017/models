import xml.etree.ElementTree as ET
root = ET.parse('/Users/michaeldimmitt/new_h/lets-parse-xml/SMIRKSampleDB.xml')
result = ''

for elem in root.findall('.//child/grandchild'):
    # How to make decisions based on attributes even in 2.6:
    if elem.attrib.get('LastName') == 'Cook':
        result = elem.text
        break
