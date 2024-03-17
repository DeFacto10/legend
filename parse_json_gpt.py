from d_id import d_id
def parse_json(data):
    data = data.split('"')[13]
    data.replace('\n', '')
    print(f'{data}')
    d_id(data)



if __name__ == "__main__":
    parse_json('')