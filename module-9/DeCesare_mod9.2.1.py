import json
import requests

def astros(obj):
    obj = json.dumps(obj, sort_keys=True, indent=4)
    print(obj)


def main():
    r = requests.get('http://api.open-notify.org/astros.json')
    obj = r.json()
    print(astros(obj))


if __name__ == '__main__':
    main()
