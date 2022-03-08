

from xsd2xml import XmlGenerator
from xsd2xml import XmlValidator


xmlgenerator = XmlGenerator('Dac6XML_v4.04.xsd', True)
xmlgenerator.generate()
xmlgenerator.write("temp")

