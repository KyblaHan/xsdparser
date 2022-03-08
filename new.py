import xml.etree.ElementTree as ET

tree = ET.parse(r'C:\Users\kybla\Desktop\test\Dac6XML_v4.04.xsd')
root = tree.getroot()
print(root)

# for child in root:
#    print(child.tag, child.attrib)


# parser = ET.XMLPullParser(['DAC6_Arrangement'])
# parser.feed('<mytag>DAC6_Arrangement')
# list(parser.read_events())
#
# parser.feed(' more text</mytag>')
# for event, elem in parser.read_events():
#    print(event)
#    print(elem.tag, 'text=', elem.text)


for child in root:
   if "name" in child.attrib:
      # if  child.attrib["name"]=="DAC6_Arrangement":
         # for c in child:
            print(child.tag, child.attrib)