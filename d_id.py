from get_video_d_id import idd

def d_id(text):
    import requests

    url = "https://api.d-id.com/talks"

    payload = {
        "script": {
            "type": "text",
            "subtitles": "false",
            "provider": {
                "type": "elevenlabs",
                "voice_id": "2EiwWnXFnvU5JabPnv8n",
                "model_id": "eleven_multilingual_v2"
            },
            "input": text
        },
        "config": {
            "stitch": True,
            "fluent": "false",
            "pad_audio": "0.0"
        },
        "source_url": "https://i.postimg.cc/TYFnxRbC/2.png"
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik53ek53TmV1R3ptcFZTQjNVZ0J4ZyJ9.eyJodHRwczovL2QtaWQuY29tL2ZlYXR1cmVzIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9zdHJpcGVfcHJvZHVjdF9pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vc3RyaXBlX2N1c3RvbWVyX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9zdHJpcGVfcHJvZHVjdF9uYW1lIjoidHJpYWwiLCJodHRwczovL2QtaWQuY29tL3N0cmlwZV9zdWJzY3JpcHRpb25faWQiOiIiLCJodHRwczovL2QtaWQuY29tL3N0cmlwZV9iaWxsaW5nX2ludGVydmFsIjoibW9udGgiLCJodHRwczovL2QtaWQuY29tL3N0cmlwZV9wbGFuX2dyb3VwIjoiZGVpZC10cmlhbCIsImh0dHBzOi8vZC1pZC5jb20vc3RyaXBlX3ByaWNlX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9zdHJpcGVfcHJpY2VfY3JlZGl0cyI6IiIsImh0dHBzOi8vZC1pZC5jb20vY2hhdF9zdHJpcGVfc3Vic2NyaXB0aW9uX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9jaGF0X3N0cmlwZV9wcmljZV9jcmVkaXRzIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9jaGF0X3N0cmlwZV9wcmljZV9pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vcHJvdmlkZXIiOiJhdXRoMCIsImh0dHBzOi8vZC1pZC5jb20vaXNfbmV3IjpmYWxzZSwiaHR0cHM6Ly9kLWlkLmNvbS9hcGlfa2V5X21vZGlmaWVkX2F0IjoiMjAyNC0wMy0xN1QwMDo0MzoyNC4zODNaIiwiaHR0cHM6Ly9kLWlkLmNvbS9vcmdfaWQiOiIiLCJodHRwczovL2QtaWQuY29tL2FwcHNfdmlzaXRlZCI6WyJTdHVkaW8iXSwiaHR0cHM6Ly9kLWlkLmNvbS9jeF9sb2dpY19pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vY3JlYXRpb25fdGltZXN0YW1wIjoiMjAyNC0wMy0xN1QwMDo0MjoyMi4yMjlaIiwiaHR0cHM6Ly9kLWlkLmNvbS9hcGlfZ2F0ZXdheV9rZXlfaWQiOiJzcHNsejdmc3I5IiwiaHR0cHM6Ly9kLWlkLmNvbS91c2FnZV9pZGVudGlmaWVyX2tleSI6InJGck5OUmxrclduTDN1UjRacmZwNSIsImh0dHBzOi8vZC1pZC5jb20vaGFzaF9rZXkiOiJxem5kZ3Rva1ZxRi1vMmt0T1VjZHMiLCJodHRwczovL2QtaWQuY29tL3ByaW1hcnkiOnRydWUsImh0dHBzOi8vZC1pZC5jb20vZW1haWwiOiJjeWJlcnB1dXV1bmtAbWFpbC5ydSIsImh0dHBzOi8vZC1pZC5jb20vcGF5bWVudF9wcm92aWRlciI6InN0cmlwZSIsImlzcyI6Imh0dHBzOi8vYXV0aC5kLWlkLmNvbS8iLCJzdWIiOiJhdXRoMHw2NWY2M2M2ZTAyNjI1NDU4MjAwMGQ2ZmMiLCJhdWQiOlsiaHR0cHM6Ly9kLWlkLnVzLmF1dGgwLmNvbS9hcGkvdjIvIiwiaHR0cHM6Ly9kLWlkLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE3MTA2MzYyMjMsImV4cCI6MTcxMDcyMjYyMywic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCByZWFkOmN1cnJlbnRfdXNlciB1cGRhdGU6Y3VycmVudF91c2VyX21ldGFkYXRhIG9mZmxpbmVfYWNjZXNzIiwiYXpwIjoiR3pyTkkxT3JlOUZNM0VlRFJmM20zejNUU3cwSmxSWXEifQ.ia8ffyVosZKwq9NHmLfzmqFkBh3kUP7vjkmHYESVKUiY66uW2NstMg5YNNA4LBzT-8_TTUJpmxtcPukjeFVsXJ7ThpcWs-DUlunBXbyAKXKOEz3oBEK_k6EWX28wyQF73umgRBpV3AiGR2E_rx0T1o8pj-P8rVYqnq9xblqJwaWZp225OMXy3l0zmZMI-fWK7sBNFRHgnosrc0arEi647hhVuoMMdoeFj-6Ex2YJFzsxpgCfhsGgn6hGNzsP6RB82V-wXZyYmmlJs9ngfpnTQR12Geqsk2OFol_BJ1b1j9F1s2ESY-pM2q9lSynxJ39CX59M8oAgFwW6ieBEdkojXw"
    }

    response = requests.post(url, json=payload, headers=headers)
    id = response.text.split('"')[3]
    print(id)
    idd(id)

if __name__ == "__main__":
    d_id('')