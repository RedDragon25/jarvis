import google.generativeai as genai

def ai(command):

    genai.configure(api_key="AIzaSyAZW8hwaJjF1PFWhXnPENjvMb5x8YMgt1A")
    # Create the model
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 50,
    "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
    )

    chat_session = model.start_chat(history=[])

    response = chat_session.send_message(command)
    return (response.text)
