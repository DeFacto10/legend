def tts(text):
    import requests
    import os
    from Access_token import get_access_token

    ACCESS_TOKEN = get_access_token()

    URL = "https://smartspeech.sber.ru/rest/v1/text:synthesize?format=wav16&voice=Pon_24000"
    payload = text
    headers = {
        'Content-Type': 'application/ssml',
        'Authorization': "Bearer " + ACCESS_TOKEN
    }

    response = requests.request("POST", URL, headers=headers, data=payload, verify=False, stream=True)
    #print(response.content)

    with open('audio4.wav', 'wb') as file:
        for chunk in response.iter_content(chunk_size=512):
            if chunk:
                file.write(chunk)

    response.close()
