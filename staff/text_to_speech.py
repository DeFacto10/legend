from speech_to_text import wait_answer
def text(text):
    import elevenlabs
    elevenlabs.set_api_key("bbcb8462d0028c58ff1e58d091e99f24")
    audio = elevenlabs.generate(
        text=text,
        voice="Grace",
        model="eleven_multilingual_v2"
    )
    elevenlabs.play(audio)
    wait_answer = True

if __name__ == "__main__":
    text(1)