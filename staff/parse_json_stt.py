from gpt import gpt
def parse_json(data):
    data = data.split(':')[1]
    data = data.split('[')[1]
    data = data.split(']')[0]
    data = data[1:-1]
    print(data)
    gpt(data)


if __name__ == "__main__":
    parse_json('')