import yaml
from pprint import pprint



if __name__ == '__main__':
    print('start')
    with open("test.yaml", "r") as _file: 
        person = yaml.unsafe_load(_file)
    pprint(type(person))
    pprint(person)



