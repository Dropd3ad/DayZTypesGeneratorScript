'''
XML Generation Script for Missing Types
=======================================

This Python script generates an XML file containing type information based on a list of class names provided. It is particularly useful for generating XML files for items or objects in a game, application, or database. The script ensures that the XML output follows a specified structure with placeholders for various attributes.

Features:
- Takes a list of class names as input, removing exact duplicates.
- Generates an XML file with type information for each class name.
- Customizable attributes within the generated XML content.
- Saves the XML file in the's "Downloads" folder (creates the folder if it doesn't exist).

Usage:
1. Modify the `input_class_names` variable with the list of class names separated by newlines.
2. Run the script to generate the XML content based on the input.
3. The script removes exact duplicate class names from the input.
4. The generated XML file is saved as "types_missing.xml" in the "Downloads/Export" folder.

''' 
__author__ = "naps"
__copyright__ = "Copyright (C) 2023 Nick Shepherd"
__license__ = "General Public License v3.0"
__version__ = "1.0"

import os
def generate_xml(class_names):
    xml_content = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
    xml_content += '<types>\n'
    
    for class_name in class_names:
        class_name = class_name.strip()
        xml_content += f'\t<type name="{class_name}">\n'
        xml_content += '\t\t<nominal>NOMINAL-CHANGE-ME</nominal>\n'
        xml_content += '\t\t<lifetime>LIFETIME-CHANGE-ME</lifetime>\n'
        xml_content += '\t\t<restock>RESTOCK-CHANGE-ME</restock>\n'
        xml_content += '\t\t<min>MIN-CHANGE-ME</min>\n'
        xml_content += '\t\t<quantmin>-1</quantmin>\n'
        xml_content += '\t\t<quantmax>-1</quantmax>\n'
        xml_content += '\t\t<cost>100</cost>\n'
        xml_content += '\t\t<flags count_in_cargo="0" count_in_hoarder="0" count_in_map="1" count_in_player="0" crafted="0" deloot="0" />\n'
        xml_content += '\t\t<category name="CAT-CHANGE-ME" />\n'
        xml_content += '\t\t<usage name="USAGE-CHANGE-ME" />\n'
        xml_content += '\t</type>\n'
    
    xml_content += '</types>'
    return xml_content

# Input a list of classnames you want to add to types.
input_class_names = """
Classname_01
Classname_01
Classname_04
Classname_03
Classname_05
"""

#Remove duplicate classname(s)
class_names = list(set(input_class_names.strip().split('\n')))
xml_content = generate_xml(class_names)

downloads_folder = os.path.expanduser("Downloads\\Export")
if not os.path.exists(downloads_folder):
    os.makedirs(downloads_folder)
output_file_path = os.path.join(downloads_folder, "types_missing.xml")

with open(output_file_path, 'w') as output_file:
    output_file.write(xml_content)

print("XML content generated and saved to:", output_file_path)
