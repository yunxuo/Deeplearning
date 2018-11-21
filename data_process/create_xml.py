import xml.etree.ElementTree as ET
from xml.dom import minidom
from PIL import Image


def get_image_size(file1):
	img = Image.open(file1)
	w, h = img.size
	return w, h

def subElement(root, tag, text):
    ele = ET.SubElement(root, tag)
    ele.text = text

def saveXML(root, filename, indent="\t", newl="\n", encoding="utf-8"):
    '''
    :param root:
    :param filename:
    :param indent:
    :param newl:
    :param encoding:
    :return:
    '''
    rawText = ET.tostring(root)
    dom = minidom.parseString(rawText)
    with open(filename, 'w') as f:
        dom.writexml(f, "", indent, newl, encoding)

def create_xml(filename, width, heigth ,class_name, position, output):
    '''

    :param filename:  <filename>
    :param class_name:   <list of class to a image>
    :param position:   <list of x y to a class>
    :param output:   <save name>
    :return:
    '''

    root = ET.Element("annotation")

    subElement(root, "folder", "AllImage")
    subElement(root, "filename", filename)
    subElement(root, "path", '')
    subElement(root, "source", '')
    source = root.find('source')
    subElement(source, 'database', 'Unknown')
    subElement(root, 'size', '')
    size = root.find('size')
    subElement(size, 'width', str(width))
    subElement(size, 'height', str(heigth))
    subElement(size, 'depth', '3')
    subElement(root, 'segmented', '0')
    for a in range(len(class_name)):   # set <object> label according to len(class_name)
        subElement(root, 'object', '')
    x = 0
    j = 0
    for object in root.findall('object'):    # set each <object> by position and class_name
        subElement(object, 'name', class_name[j])
        subElement(object, 'pose', 'Unspecified')
        subElement(object, 'truncated', '0')
        subElement(object, 'difficult', '0')
        subElement(object, 'bndbox', '')
        bndbox = object.find('bndbox')
        subElement(bndbox, 'xmin', str(position[x]))
        subElement(bndbox, 'ymin', str(position[x + 1]))
        subElement(bndbox, 'xmax', str(position[x + 2]))
        subElement(bndbox, 'ymax', str(position[x + 3]))
        x += 4
        j += 1

    # save xml file
    saveXML(root, output)