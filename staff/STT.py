def sst():
    import requests
    from Access_token import get_access_token
    from parse_json_stt import parse_json

    ACCESS_TOKEN = get_access_token()
    URL = 'https://smartspeech.sber.ru/rest/v1/speech:recognize'
    headers = {
        'Content-Type': 'audio/mpeg',
        'Authorization': 'Bearer ' + ACCESS_TOKEN
    }
    with open('audio.mp3', 'rb') as f:  # для теста записал аудио, где говорю "привет, меня зовут Матвей"
        r = requests.request("POST", URL, headers=headers, files={'audio.mp3': f}, verify=False)

    print(r.content.decode())  # вернет string в формате json, где будут : расшифровка, вероятности подходящей эмоции
    parse_json(r.content.decode())
if __name__ == "__main__":
    sst()