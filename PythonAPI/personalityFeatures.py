from flask import Flask, jsonify
from sheets import connect_sheet

app = Flask(__name__)

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

careers = {"january": "an athlete", "febuary":"an artist", "march":"a pilot", "april":"a dictator", "may":"a politian", "june":"a CEO", "july":"a bricklayer","august":"a hairdresser", "september":"an academic", "october":"a lawyer", "november":"a serial killer","december":"a dentist"}

career = careers[lastRecord["BirthMonth"].lower()]

if(lastRecord["Drive"] == "No" or lastRecord["Glasses"] == "Yes"):
    rich = True

if(lastRecord["Tounge"] == "Yes"):
    moveCountries = True

firstInitial = ord(lastRecord["FirstName"])[0].lower() - ord('a') +1
#if(firstInitial<5):
    


def get_results():
    return jsonify(
    {
        'twins': twins,
        'married': married,
        'career': career,
        'rich': rich,
        'moveCountries': moveCountries
    }
)

if __name__ == '__main__':
    app.run(debug=True)
