import requests


def get_access_token():
    payload = 'scope=SALUTE_SPEECH_PERS'
    url_at = 'https://ngw.devices.sberbank.ru:9443/api/v2/oauth'
    headers = {
        'RqUID': '6f0b1291-c7f3-43c6-bb2e-9f3efb2dc98e',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer MDQ4ODcwMWUtYjM5Ny00Zjg2LTg1ZWItMDg0ZDMzYjJlNjQ3Ojc1NzYyYTQ2LWQ4ZTgtNDMxNi05ZjkxLTc5ODNjMmJjOGVjNw==' #авторизационные данные от моего аккаунта
    }

    response = requests.request("POST", url_at, headers=headers, data=payload, verify=False)
    raw = response.text.split(":")
    raw_2 = raw[1].split(",")
    return raw_2[0].replace('"','') #Распарсит строку и оставит только access_token