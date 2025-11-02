from sheets import connect_sheet
from google import genai
from flask import Flask, jsonify, render_template

app = Flask(__name__)

def calculate():
    sheet =  connect_sheet("My Spreadsheet")   
    records = sheet.get_all_records()
    rows = sheet.get_all_values()
    lastRecord = records[-1]

    twins = False
    married = False
    rich = True
    moveCountries = False

    if(lastRecord["Gender"] == "F" and lastRecord["Height"] > 164):
        twins = True
    elif(lastRecord["Height"] > 180):
        married = True

    careers = {"january": "an athlete", "february":"an artist", "march":"a pilot", "april":"a dictator", "may":"a politian", "june":"a CEO", "july":"a bricklayer","august":"a hairdresser", "september":"an academic", "october":"a lawyer", "november":"a serial killer","december":"a dentist"}

    career = careers[lastRecord["BirthMonth"].lower()]

    if(lastRecord["Drive"] == "No" or lastRecord["Glasses"] == "Yes"):
        rich = True

    if(lastRecord["Tongue"] == "Yes"):
        moveCountries = True

    rememberedFor = ""
    firstInitial = ord(lastRecord["FirstName"][0].lower()) - ord('a') +1
    if(firstInitial<5):
        rememberedFor = "winning an award"
    elif(firstInitial<9):
        rememberedFor = "doing something embarrassing"
    elif(firstInitial<13):
        rememberedFor = "always being kind"
        
    elif(firstInitial < 17):
        rememberedFor = "being the best at your job"
    elif(firstInitial <21):
        rememberedFor ="being intelligent"
    elif(firstInitial < 25):
        rememberedFor = "being forgetful"
    else:
        rememberedFor = "that one thing you did in Vegas"


    client = genai.Client(api_key="AIzaSyA_uNBKypl3XyXb3DMVy5G1QgV9WujDDWU")

    request = "Create a short paragraph detailing the legacy of a person based on: name: " + lastRecord["FirstName"] + lastRecord["LastName"] + "career" + career +" likely to get married: " + str(married) +" likely to have twins: "+ str(twins) + "likely to be rich" + str(rich) + "being remembred for" + rememberedFor
    message = client.models.generate_content(
        model="gemini-2.5-flash", contents= request
    )

    paragraph = message.candidates[0].content.parts[0].text

    return paragraph

@app.route('/results', methods = ['GET'])
def main():
    # print("hello")
    # paragraph = calculate()
    # return jsonify({"paragraph": paragraph})

    try:
        paragraph = calculate
        return jsonify({"paragraph": paragraph})
    except Exception as e:
        print("error in /results:", e)
        return jsonify({"error": str(e)}), 500
    

if __name__ == "main":
    app.run(debug=True)
    





