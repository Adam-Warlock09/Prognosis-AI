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
        
        # for i in inputDict:
        #     if i == "gender":
        #         inputDict[i] = (inputDict[i].lower() == "male")
        #     elif i == "ccp":
        #         if inputDict[i] == 1:
        #             inputDict[i] = 2
        #     elif i == "bp":


        return render_template('./result.html', s = str(inputDict))
    
    return render_template('./index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)