import xml.etree.ElementTree as ET
import pandas as pd

# tree = ET.parse(r'C:\Users\kybla\Desktop\test\instance1.xml')
# to_del =22
tree = ET.parse(r'C:\Users\kybla\Desktop\test\Dac6XML_v4.04.xsd')
to_del = 0

main = "DAC6_Arrangement"
root = tree.getroot()
# print(root.attrib)
# for child in root:
#     print(child.tag, child.attrib)

n = 0
list_elems = []


def get_next_xml(root, n):
    for child in root:
        print(" " * n, child.tag[to_del:])
        if len(child.attrib) != 0:
            print(" " * (n + 1), child.attrib)
        get_next_xml(child, n + 1)


def get_next_xsd(root, n):
    for child in root:
        if len(child.attrib) != 0:
            # list_elems.append((" " * n,child.attrib))
            tmp = child.attrib
            tmp['level'] = n
            tmp['tag'] = child.tag[34:]
            tmp['description'] = child.text
            list_elems.append(tmp)
        get_next_xsd(child, n + 1)


def find_elem(elem_name):
    output_elems = []
    find = False
    level = -1
    c = 0

    for elem in list_elems:
        if 'name' in elem:
            if elem['name'] == elem_name:
                find = True
                level = elem['level']

        if elem['level'] == level:
            c = c + 1
        if find == True:
            output_elems.append(elem)
        if c == 2:
            find = False
            output_elems = output_elems[:-1]
            break
        # if find:
        #     output_elems.append(elem)
    return output_elems


def razbor(root_elem="DAC6_Arrangement", n=0, output_elems=[]):
    base_elems = find_elem(root_elem)
    for elem in base_elems:
        # print(" "*n,elem)
        tmp = elem
        tmp['level2'] = n
        output_elems.append(tmp)
        if "type" in elem:
            razbor(drop_schema_from_name(elem["type"]), n + 1, output_elems)
    return output_elems


def detect_uniq_keys(elems):
    keys = []
    for elem in elems:
        for key in elem.keys():
            if not key in keys:
                keys.append(key)
    # print(keys)
    return keys


def list_to_csv(elems):
    # test = []
    # for elem in elems:
    #     if "name" in elem and not elem["tag"]=="complexType":
    #         elem["name"] = "_"*elem["level2"]+elem["name"]
            # print(" "*elem["level2"]+elem["name"],elem["tag"])

    frame = pd.DataFrame(elems)

    frame.to_csv("output.csv",sep='&')
    return frame

def drop_schema_from_name(name):
    if ":" in name:
        pos = name.find(":")
        # print(name[pos+1:],pos)
        return name[pos+1:]
    return name

# razbor()
# for x in find_elem("Intermediary_Type"): print(x)
get_next_xsd(root, n)
df = list_to_csv(razbor())
for d in df:
    print(d)

# df = df.loc[(df['tag'] == 'element') | (df['tag'] == 'attribute')]
# print(df)


