from toolkit import data_provision as dp


def test_convert_data_from_xml_to_json():
    file = 'data/Badges.xml'
    element = 'row'
    res = dp.convert_data_from_xml_to_dict(file, element)
    assert (res['rows'][0]['Name'] == "Autobiographer")
