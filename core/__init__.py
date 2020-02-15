def parse(qml_str):
    import xml.etree.ElementTree as ET
    root = ET.fromstring(qml_str)
    symbol = {}
    layer = {}
    props = {}
    for child in root.getiterator():
        if child.tag == 'symbol': 
            symbol = child.attrib
        if child.tag == 'layer':
            layer = child.attrib
        if child.tag == 'prop':
            props[child.attrib['k']] = child.attrib['v']

    return {'symbol':symbol, 'layer':layer, 'props':props}