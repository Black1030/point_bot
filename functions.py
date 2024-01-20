from json import load, dump

filename = 'data.json'

def read_data(filename):
    with open(filename, 'r') as f:
        return load(f)


def load_to_base(login, password):
    a = {
        'username': login,
        'password': password
    }
    data = read_data(filename)
    data.append(a)
    with open(filename, 'w') as f:
        dump(data, f, indent=4, ensure_ascii=False)