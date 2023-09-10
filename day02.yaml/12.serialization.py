import yaml


class Person(yaml.YAMLObject):
    yaml_tag = "!PersonPythonClass"

    # class Person:
    def __init__(self, _name: str, _id: int, _age: int) -> None:
        self._name = _name
        self._id = _id
        self._age = _age

    def __repr__(self) -> str:
        return f"({self._id}){self._name}<{self._age}-yo>"

    def inc_age(self) -> None:
        self._age += 1

    def dump_to_yaml_file(self, filename: str) -> None:
        with open(filename, "w") as _file:
            _file.write(yaml.dump(self))


tom = Person("tom", 4, 33)

tom.inc_age()

tom.dump_to_yaml_file("./12.tom.yaml")
