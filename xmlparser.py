import xml.etree.ElementTree as ET
import sys

tree = ET.parse(sys.argv[1])
root = tree.getroot()
for child,baby in zip(root.iter("address"), root.iter("port")):
    portid = baby.get('portid')
    if portid == '443':
        print('https://' + child.get('addr'))
    elif portid == '80':
        print('http://' + child.get('addr'))
    else:
        print(child.get('addr') + ':' + portid)
#output to-do
#for now >
