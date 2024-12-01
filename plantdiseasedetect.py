import PIL.Image
import base64
import time
import google.generativeai as genai

def base64todisease(basestr):
    ts = time.time()
    #adding unique identity for the image
    with open(f"images/{ts}.png", "wb") as f:
        f.write(base64.urlsafe_b64decode(basestr))
    img = PIL.Image.open(f"images/{ts}.png")
    #Decoding and saving the image
    gemini_api_key = "<gemini-key>"
    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    #configuring gemini api
    disease_name_raw = model.generate_content(["What kind of plant diesase does the given image have. give only the diesease name dont give any other text in side. if there is no diesease just say no diesease found", img])
    disease_name = disease_name_raw.text
    #Sending Prompt to Gemini API
    #Fetching the disease name
    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_NONE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_NONE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_NONE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_NONE"
        }
    ]

    model_text = genai.GenerativeModel('gemini-pro')
    solution_raw = model_text.generate_content(f"Give the solution for one lines for the given disease - {disease_name}.",safety_settings=safety_settings)
    return f"Disease name: {disease_name}, Solution: {solution_raw.text}"
    # Fetching the disease solution