from flask import Flask,request
from cropsuggester import CropSuggester
from chatbot import ChatBot
import plantdiseasedetect
from fertilizersuggester import FertilizerSuggester
from cropsteps import CropPlantingSteps
app = Flask(__name__)

@app.route("/api/crop/suggester",methods = ["POST"])
def cropsuggester():
    content = request.json

    nitrogen = content["nitrogen"]
    phosphorus = content["phosphorus"]
    potassium = content["potassium"]
    ph = content["ph"]
    type = content["type"]
    lang = content["lang"]
    temperature = content["temperature"]
    light_intensity = content["light_intensity"]
    place = content["place"]
    crop_numbers = content["crop_numbers"]
    water_availability = content["water_availability"]

    return {"body":CropSuggester(ph, nitrogen, phosphorus, potassium, type, lang, temperature, light_intensity, place,crop_numbers,water_availability)}

@app.route("/api/chat", methods= ['POST'])
def chatbot():
    content = request.json
    message = content["message"]
    lang = content["lang"]
    return {"body":ChatBot(message, lang)}


@app.route("/api/fertilizer/suggester",methods=['POST'])
def fertilzersuggester():
    content = request.json

    nitrogen = content["nitrogen"]
    phosphorus = content["phosphorus"]
    potassium = content["potassium"]
    ph = content["ph"]
    type = content["type"]
    lang = content["lang"]
    place = content["place"]
    crop = content["crop"]
    base64 = content["base64"]
    value = FertilizerSuggester(ph, nitrogen, phosphorus, potassium, type, place, lang, crop,base64)
    return {"body":value.get("data"), "url":value.get("url"), "crop_name":value.get("crop_name")}

@app.route("/api/growa/diseasedetector",methods=['POST'])
def plantdiseasedetector():
    content = request.json
    imageBase64 = content["base64"]
    # Fetching the base64 property of the image data
    return {"body":plantdiseasedetect.base64todisease(imageBase64)}

@app.route("/api/crop/steps",methods=['POST'])
def cropsteps():
    content = request.json
    crop_name = content["crop_name"]
    values = CropPlantingSteps(crop_name)
    return {"body": values.get("data"), "url":values.get("image_url")}
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)