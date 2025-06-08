import xml.etree.ElementTree as ET

def get_incoming_by_group_number(filename: str, group_number: int):
    tree = ET.parse(filename)
    root = tree.getroot()
    for group in root.findall('group'):
        number = group.find('number')
        if number is not None and int(number.text) == group_number:
            timing = group.find('timingExbytes')
            if timing is not None:
                incoming = timing.find('incoming')
                if incoming is not None:
                    print(f"incoming for group with number {group_number}: {incoming.text}")
                    return
                else:
                    print(f"In group with number {group_number} absent tag <incoming>")
                    return
            else:
                print(f"In group with number {group_number} absent tag <timingExbytes>")
                return
    print(f"Group with number={group_number} does not exist")


get_incoming_by_group_number('groups.xml', 0)
