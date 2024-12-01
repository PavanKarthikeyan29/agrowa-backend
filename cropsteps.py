import openai
import os
import pandas as pd
import time

openai.api_key = '<openai-key>'

def CropPlantingSteps(crop_name):
    prompt = f"Give me 5 steps to grow {crop_name} seperated by commas and make it as small as possible and target the given crop name and give the data only regarding the crop. Small in the sense give the disired content in the smallest form possible and include the crop name in the result and make it lively like if it says rice change it to paddy and stuff"
    messages = [{"role": "user", "content": prompt}]
    chat = openai.ChatCompletion.create(
        model="gpt-4", messages=messages
    )
    links = {
        "sugarcane": "https://www.netafimindia.com/bynder/689FFBA0-D431-4D9A-8BFB1805602316FC-sugarcane-with-driperline.jpg",
        "rice": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/20201102.Hengnan.Hybrid_rice_Sanyou-1.6.jpg/800px-20201102.Hengnan.Hybrid_rice_Sanyou-1.6.jpg",
        "wheat": "https://eng.ruralvoice.in/uploads/images/2023/02/image_750x_63f4493d63c11.jpg",
        "okra": "https://www.thespruce.com/thmb/ZUyMVJFsZYC4LLt-0a6mC_JK_Tk=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/companion-plants-for-okra-5074423-08-2a6393954bfd42ae8b67449fb35094e5.jpg",
        "potato": "https://www.agrifarming.in/wp-content/uploads/2015/03/potato-farming.jpg"}
    link = ""
    try:
        link = links.get(crop_name.lower().replace(" ", "").strip())
        print("link - " + link)
    except:
        response = openai.Image.create(
            prompt=f"Realistic image of a {crop_name} crop, give only the crop or tree dont give any other objects into it make sure that the crop is plant or a tree and its commerical so make it professional",
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']
        link = image_url
        print("link1 - " + link)
    reply = chat.choices[0].message.content
    return {"data":reply, "image_url":link}


