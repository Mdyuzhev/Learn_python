import lxml.etree as et
import json


class TemplateXML:

    def __init__(self, body=""):
        self._body = body
        self._xpath = {}

    def __getitem__(self, name):
        xpath = self.get_xpath(name)
        return self.get_value_xpath(xpath)

    def __setitem__(self, key, value):
        xpath = self.get_xpath(key)
        self.set_value_xpath(xpath, value)


    def set_body_from_file(self, path):
        with open(path, 'r') as file:
            self._body = file.read()

    @property
    def body(self):
        return self._body

    def get_value_xpath(self, xpath):
        root = et.fromstring(self._body.encode())
        return root.xpath(xpath)[0].text

    def get_attribute_xpath(self, xpath, attr_name):
        root = et.fromstring(self._body.encode())
        return root.xpath(xpath)[0].attrib[attr_name]

    def set_value_xpath(self, xpath, value):
        root = et.fromstring(self._body.encode())
        root.xpath(xpath)[0].text = str(value)
        self._body = et.tostring(root, method="xml").decode()

    def set_xpath_mask(self, path):
        with open(path, 'r') as file:
            self._xpath = json.load(file)

    def get_xpath(self, key):
        return self._xpath[key]

    # def __generate_xpath(self, xml):
    #     if xml != "":
    #         xpath = {}
    #         root = et.fromstring(xml.encode())
    #         tree = et.ElementTree(root)
    #         for e in root.iter():
    #             item = tree.getelementpath(e)
    #             xpath[item.split('}')[-1].split('/')[-1]] = item
    #         return xpath
