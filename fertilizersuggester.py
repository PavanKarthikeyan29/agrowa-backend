import openai
import PIL.Image
import base64
import time
import google.generativeai as genai
openai.api_key = '<openai-key>'
import random

def FertilizerSuggester(soil_ph, soil_n, soil_p, soil_k, soil_type,place,language,crop,base641):
    if base641 != "":
        ts = time.time()
        with open(f"images/{ts}.png", "wb") as f:
            f.write(base64.urlsafe_b64decode(base641))
        img = PIL.Image.open(f"images/{ts}.png")
        gemini_api_key = "AIzaSyDy66pZcAT-XzHNZdD0MgdwAmTjJF3TGzg"
        genai.configure(api_key=gemini_api_key)
        model = genai.GenerativeModel('gemini-pro-vision')
        cropnameraw = model.generate_content([
            "Please say the crop planted in the image.... Only one word dont give any other thing",
            img])
        crop = cropnameraw.text
    prompt = f"Suggest one fertilizer names in  a list dont give anything exepct that for the following factors of soil. If fertilizers are not needed just give the reply as 'fertilizers not needed'. factors are ph={soil_ph}, nitrogen = {soil_n}, phrophrous = {soil_p}, potassium = {soil_k}, type = {soil_type}, place = {place} and mainly give the result in pure {language} language and dont include any other languages and dont give too much give the fertilizer name alone or else just say what i said. give one fertilizer and say  why they need to use it, give one fertilizer name followed by comma and why why need to use this particuallar fertilizer as small as possible, enhance the why start with caps leter and make it more good and gramatical,  also suggest fertilizer that needed for {crop} crop. all in one fertilizer. in the reason also say how this fertilizer supports that crop and include the crop name in the reason and give it small"
    messages = [{"role": "user", "content": prompt}]
    chat = openai.ChatCompletion.create(
        model="gpt-4", messages=messages
    )

    reply = chat.choices[0].message.content

    links = {"sugarcane":"https://www.netafimindia.com/bynder/689FFBA0-D431-4D9A-8BFB1805602316FC-sugarcane-with-driperline.jpg",
             "rice":"https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/20201102.Hengnan.Hybrid_rice_Sanyou-1.6.jpg/800px-20201102.Hengnan.Hybrid_rice_Sanyou-1.6.jpg",
             "wheat":"https://eng.ruralvoice.in/uploads/images/2023/02/image_750x_63f4493d63c11.jpg",
             "okra":"https://www.thespruce.com/thmb/ZUyMVJFsZYC4LLt-0a6mC_JK_Tk=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/companion-plants-for-okra-5074423-08-2a6393954bfd42ae8b67449fb35094e5.jpg",
             "potato":"https://www.agrifarming.in/wp-content/uploads/2015/03/potato-farming.jpg"}
    link = ""
    try:
        link = links.get(crop.lower().replace(" ","").strip())
        print("link - "+link)
    except:
            response = openai.Image.create(
                prompt=f"Realistic image of a {crop} crop, give only the crop or tree dont give any other objects into it make sure that the crop is plant or a tree and its commerical so make it professional",
                n=1,
                size="1024x1024"
            )
            image_url = response['data'][0]['url']
            link = image_url
            print("link1 - " + link)
    return {"data":reply,"url":link, "crop_name": crop}