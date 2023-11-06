import xml.etree.ElementTree as ET

def parse_xml(xml_file):
    test_results = []

    tree = ET.parse(xml_file)
    root = tree.getroot()

    for testcase in root.findall('.//testcase'):
        name = testcase.get('name')
        classname = testcase.get('classname')
        time = float(testcase.get('time'))
        status = testcase.get('status')

        test_results.append({
            'name': name,
            'classname': classname,
            'time': time,
            'status': status
        })

    return test_results

if __name__ == '__main__':
    xml_file = 'katalon.xml'
    results = parse_xml(xml_file)

    for result in results:
        print(result)