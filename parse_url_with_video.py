from save_video import save
def parce(answer):
    import requests
    url = answer.split('"')[-2]
    print(url)
    response = requests.get(url)
    print(response)
    save(url)