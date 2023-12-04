from xml.etree.ElementTree import parse

root = parse("example.xml").getroot()
print(root.tag)
print(len(root))
for child in root:
    print(child.tag, child.attrib)
