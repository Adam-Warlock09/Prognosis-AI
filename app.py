from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/result', methods = ['GET', 'POST'])
def result():
    if request.method == 'POST':
        formData = request.form
        keysDict = {
            "age" : "Number",
            "gender" : "String",
            "height" : "Number",
            "weight" : "Number",
            "physical-activity" : "Number",
            "sleep-quality" : "Number",
            "diet-quality" : "Number",
            "cholestrol" : "Number",
            "haemo" : "Number",
            "bp" : "Number",
            "heart" : "Number",
            "ecg" : "CheckBox",
            "ccp" : "CheckBox",
            "anxiety" : "CheckBox",
            "sugar" : "Number",
            "insulin" : "Number",
            "smoke" : "CheckBox",
            "thick-feet" : "CheckBox",
            "fam-dia" : "CheckBox",
            "alcohol" : "CheckBox",
            "firstPeriod" : "Number",
            "pregnancies" : "Number",
            "firstBaby" : "Number",
            "menopause" : "CheckBox",
            "fam-bc" : "CheckBox",
            "chronicCough" : "CheckBox",
            "allergies" : "CheckBox",
            "yellowFingers" : "CheckBox",
            "shortBreath" : "CheckBox",
            "swallowing" : "CheckBox",
            "fam-asthma" : "CheckBox",
            "pollution" : "Number"
        }

        inputDict = {}

        for i in keysDict:
            if(keysDict[i] == "Number"):
                inputDict[i] = formData.get(i)
            elif(keysDict[i] == "String"):
                inputDict[i] = formData.get(i).strip()
            elif(keysDict[i] == "CheckBox"):
                if(formData.getlist(i)):
                    inputDict[i] = 1
                else:
                    inputDict[i] = 0

        inputDict["bmi"] = inputDict["weight"] / ((inputDict["height"] / 100) * (inputDict["height"] / 100))
        z = inputDict["bmi"]
        if (z >= 0 and z < 25):
            val = 1
        elif (z >= 25 and z < 30):
            val = 2
        elif (z >= 30 and z < 35):
            val = 3
        elif (z >= 35):
            val = 4
        
        inputDict["bmi_breast"] = val
        
        for i in inputDict:
            if i == "gender":
                inputDict[i] = (inputDict[i].lower() == "male")
            elif i == "ccp":
                inputDict["ccp_lung"] = inputDict[i] + 1
                if inputDict[i] == 1:
                    inputDict[i] = 2
            elif i == "smoke":
                inputDict[i] += 1
            elif i == "yellowFingers":
                inputDict[i] += 1
            elif i == "anxiety":
                inputDict[i] += 1
            elif i == "allergies":
                inputDict[i] += 1
            elif i == "alcohol":
                inputDict[i] += 1
            elif i == "chronicCough":
                inputDict[i] += 1
            elif i == "shortBreath":
                inputDict[i] += 1
            elif i == "swallowing":
                inputDict[i] += 1
            elif i == "age":
                x = inputDict[i]
                if(x>0 and x<=29):
                    y = 1
                elif(x>=30 and x<=34):
                    y = 2
                elif(x>=35 and x<=39):
                    y = 3
                elif(x>=40 and x<=44):
                    y = 4
                elif(x>=45 and x<=49):
                    y = 5
                elif(x>=50 and x<=54):
                    y = 6
                elif(x>=55 and x<=59):
                    y = 7
                elif(x>=60 and x<=64):
                    y = 8
                elif(x>=65 and x<=69):
                    y = 9
                elif(x>=70 and x<=74):
                    y = 10
                elif(x>=75 and x<=79):
                    y = 11
                elif(x>=80 and x<=84):
                    y = 12
                elif(x>=85):
                    y = 13
                inputDict["age_breast"] = y
            elif i == "firstPeriod":
                if inputDict[i] >= 14:
                    y = 0
                elif (inputDict[i] == 12 or inputDict[i] == 13):
                    y = 1
                elif inputDict[i] < 12:
                    y = 2
                inputDict[i] = y
            elif i == "firstBaby":
                if inputDict[i] == 0:
                    y = 4
                elif inputDict[i] < 20:
                    y = 0
                elif (inputDict[i] >= 20 and inputDict[i] <= 24):
                    y = 1
                elif (inputDict[i] >= 25 and inputDict[i] <= 29):
                    y = 2
                elif (inputDict[i] > 30):
                    y = 3
                inputDict[i] = y
            elif i == "menopause":
                inputDict[i] += 1

        return render_template('./result.html', s = str(inputDict))
    
    return render_template('./index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)