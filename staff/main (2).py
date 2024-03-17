import requests




def get_access_token():
    payload = 'scope=SALUTE_SPEECH_PERS'
    url_at = 'https://ngw.devices.sberbank.ru:9443/api/v2/oauth'
    headers = {
        'RqUID': '6f0b1291-c7f3-43c6-bb2e-9f3efb2dc98e',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer MDQ4ODcwMWUtYjM5Ny00Zjg2LTg1ZWItMDg0ZDMzYjJlNjQ3Ojc1NzYyYTQ2LWQ4ZTgtNDMxNi05ZjkxLTc5ODNjMmJjOGVjNw=='
    }

    response = requests.request("POST", url_at, headers=headers, data=payload, verify=False)
    raw = response.text.split(":")
    raw_2 = raw[1].split(",")
    return raw_2[0].replace('"','')

ACCESS_TOKEN = get_access_token()



def text_to_speech(text,a_t):
    URL = "https://smartspeech.sber.ru/rest/v1/text:synthesize?format=wav16&voice=Pon_24000"
    payload = text
    headers = {
        'Content-Type': 'application/ssml',
        'Authorization': "Bearer "+ACCESS_TOKEN
    }

    response = requests.request("POST", URL, headers=headers, data=payload,verify=False)

    return response.content

response = text_to_speech('Привет',ACCESS_TOKEN)

#with open('myfile3.wav', mode='bx') as f:
   # f.write(response)

# import io
# import wave
#
# import numpy as np
# import scipy.io.wavfile
# import soundfile as sf
# from scipy.io.wavfile import write
#
# def convert_bytearray_to_wav_ndarray(input_bytearray: bytes, sampling_rate=16000):
#     bytes_wav = bytes()
#     byte_io = io.BytesIO(bytes_wav)
#     write(byte_io, sampling_rate, np.frombuffer(input_bytearray, dtype=np.int16))
#     output_wav = byte_io.read()
#     output, samplerate = sf.read(io.BytesIO(output_wav))
#     return output
#
#
# output = convert_bytearray_to_wav_ndarray(input_bytearray=response)
#
# scipy.io.wavfile.write("output1.wav", 16000, output)