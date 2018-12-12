import json


class TemplateJSON:

    def __init__(self, body="{}"):
        self._dictionary = json.loads(body)

    def __getitem__(self, name):
        names = name.split(':')
        tmp = self.__get_single_value_json(names.pop(0))
        while len(names) > 0:
            tmp = TemplateJSON(json.dumps(tmp)).__get_single_value_json(names.pop(0))
        return tmp

    def __setitem__(self, key, value):
        self._dictionary[key] = value

    def __delitem__(self, key):
        self._dictionary.pop(key)

    def set_body_from_file(self, path):
        with open(path, 'r') as file:
            self._dictionary = json.loads(file.read())

    def __get_single_value_json(self, name):
        return self._dictionary[name]

    @property
    def body(self):
        return json.dumps(self._dictionary)

    @body.setter
    def body(self, body):
        self._dictionary = json.loads(body)
