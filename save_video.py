def save(save_url):
    import requests
    import os
    response = requests.get(save_url)
    # print(response.content)
    with open('avatar.mp4', 'wb') as file:
        for chunk in response.iter_content(chunk_size=512):
            if chunk:
                file.write(chunk)
    os.startfile('avatar.mp4')