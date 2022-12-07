from typing import Dict, List
import xml.etree.ElementTree as ET
import xmltodict


def construct_tree(terminal_output: List[str]) -> ET:
    root = ET.Element("root")
    tree = ET.ElementTree(root)
    position = tree.getroot()
    for line in terminal_output:
        if line.startswith('$ cd'):
            directory = line[5::]
            match directory:
                case '/':
                    position = tree.getroot()
                case '..':
                    position = position.find('..')
                case other:
                    position = position.find(f'.{other}')
        elif line.startswith('$ ls'):
            pass
        elif line.startswith('dir'):
            new_dir = line[4::]
            ET.SubElement(position, new_dir)
        else:
            size, file = line.split()
            file_elem = ET.SubElement(position, file, size=size)

    tree_string = ET.tostring(tree.getroot(), encoding='unicode', method='xml')
    print(tree_string)
    return xmltodict.parse(tree_string, process_namespaces=True)["root"]


def find_all_dir(terminal_output: List[str], maxsize: int) -> Dict:
    directory_structure = construct_tree(terminal_output)
    pass
