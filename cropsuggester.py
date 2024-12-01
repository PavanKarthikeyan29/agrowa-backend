import openai
openai.api_key = '<openai-key>'

def CropSuggester(soil_ph, soil_n, soil_p, soil_k, soil_type,language,temperature, light_intensity,place,crop_numbers, water_availability):
    prompt = f"Give me one {crop_numbers} crop names seperated by commas that can grow using the given factors of soil. Nitrogen = {soil_n}, phosphorus = {soil_p}, Pottasium = {soil_k}, PH = {soil_ph} and Soil type = {soil_type} temperature = {temperature} light intensity = {light_intensity} and in {place} and mainly give the result in pure {language} and please dont add any languages and dont leave spaces between the lists and dont give any gramatical errors and spelling mistakes, And make sure that you recommend crops which the farmers water level like if the water level is high give crops like rice and when the water availablity is low give crops accordingly now the water availability = {water_availability}, in anycost never tell anything just recommend 5 crops with that i said before, there will be totally 4 values. in high means there is unlimited water so give crops like rice, sugar cane and crops 'note that rice and sugar cane should only be in high catogory'. in normal suggest like corn wheat and stuff and for low and no water recommend that poor farmer with ur curtesey as i said earlier never give other words instead of that crops in low water give crops okra, potatoes and vegetables for no watergive like mustard, peppers, potatoes and stuff remember that rice and sugarcane needed high water so be careful please dont give rice and sugarcane for normal low and no water "

    messages = [{"role": "user", "content": prompt}]
    chat = openai.ChatCompletion.create(
        model="gpt-4", messages=messages
    )

    reply = chat.choices[0].message.content
    return reply