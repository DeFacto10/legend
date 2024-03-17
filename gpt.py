from parse_json_gpt import parse_json
def gpt(text):
    import requests
    from parse_json_gpt import parse_json
    prompt = {
        "modelUri": "gpt://b1g74fgn5ssbplh3e14d/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0,
            "maxTokens": "50"
        },
        "messages": [
            {
                'role': 'system',
                'text': 'Ты гид Петр Великий по Санкт-Петербургу с которым  жители города и туристы смогут общаться, узнавать  интересные факты, легенды, истории, как куда добраться и что посмотреть.'
            },
            {
                'role': 'user',
                'text': text,
            }
        ]
    }
    url = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Api-Key AQVN1sKVXQdLWNpYJ_udaAY16khT3zKc9L2ZyJ1B'
    }

    response = requests.post(url, headers=headers,json=prompt)
    result = response.text
    #print(result)
    parse_json(result)


if __name__ == "__main__":
    gpt("")