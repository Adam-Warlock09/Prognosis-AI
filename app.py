from flask import Flask, render_template, redirect, request
import pickle
import pandas as pd
import numpy as np

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
                if(formData.get(i)):
                    if(float(formData.get(i)) == round(float(formData.get(i)))):
                        inputDict[i] = int(formData.get(i))
                    else:
                        inputDict[i] = float(formData.get(i))
                else:
                    inputDict[i] = 0
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

        temp = {}
        
        for i in inputDict:
            if i == "gender":
                inputDict[i] = int(inputDict[i].lower() == "male")
            elif i == "ccp":
                temp["ccp_lung"] = inputDict[i] + 1
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
            elif i == "sugar":
                if(inputDict[i] > 120):
                    inputDict[i] = 1
                else:
                    inputDict[i] = 0
            elif i == "thick-feet":
                if inputDict[i] == 1:
                    inputDict[i] = 40
                else:
                    inputDict[i] = 20
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
                temp["age_breast"] = y
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

        inputDict.update(temp)

        # List of features of each model
        # Heart disease feature list--------------
        heart_columns = ['age', 'sex', 'cp', 'trestbps', 'chol','fbs','restecg','thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
        heart_default = [0, 1.07, 1, 0, 2]
        heart_test_input = [inputDict["age"], inputDict["gender"], inputDict["ccp"], inputDict["bp"], inputDict["cholestrol"], inputDict["sugar"], inputDict["ecg"], inputDict["heart"]]
        heart_test = heart_test_input + heart_default
        heart_dict = dict(zip(heart_columns,heart_test))
        heart_input = pd.DataFrame([heart_dict])

        # -------------------------------------

        diabetes_columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
        diabetes_test_input = [inputDict["pregnancies"], inputDict["sugar"], inputDict["bp"], inputDict["thick-feet"], inputDict["insulin"], inputDict["bmi"], inputDict["fam-dia"], inputDict["age"]]
        diabetes_test = diabetes_test_input
        diabetes_dict = dict(zip(diabetes_columns,diabetes_test))
        diabetes_input = pd.DataFrame([diabetes_dict])
        
        # -------------------------------------

        lung_cancer_columns = ['GENDER', 'AGE', 'SMOKING', 'YELLOW_FINGERS', 'ANXIETY', 'ALLERGY ', 'ALCOHOL CONSUMING', 'COUGHING', 'SHORTNESS OF BREATH', 'SWALLOWING DIFFICULTY', 'CHEST PAIN', 'CHRONIC DISEASE', 'WHEEZING']
        lung_cancer_default = [2,1]
        lung_cancer_test_input = [inputDict["gender"], inputDict["age"], inputDict["smoke"], inputDict["yellowFingers"], inputDict["anxiety"], inputDict["allergies"], inputDict["alcohol"], inputDict["chronicCough"], inputDict["shortBreath"], inputDict["swallowing"], inputDict["ccp"]]
        lung_cancer_test = lung_cancer_test_input + lung_cancer_default
        lung_cancer_dict = dict(zip(lung_cancer_columns,lung_cancer_test))
        lung_cancer_input = pd.DataFrame([lung_cancer_dict])

        # -------------------------------------

        anaemia_columns = ['Sex', 'Hb']
        anaemia_test_input = [inputDict["gender"], inputDict["haemo"]]
        anaemia_test = anaemia_test_input
        anaemia_dict = dict(zip(anaemia_columns,anaemia_test))
        anaemia_input = pd.DataFrame([anaemia_dict])

        # -------------------------------------

        asthma_columns = ['Age', 'Gender', 'BMI', 'Smoking', 'PhysicalActivity', 'DietQuality', 'SleepQuality', 'PollutionExposure', 'PollenExposure', 'DustExposure', 'PetAllergy', 'FamilyHistoryAsthma', 'HistoryOfAllergies','ShortnessOfBreath','Coughing', 'Eczema','HayFever','GastroesophagealReflux','LungFunctionFEV1','LungFunctionFVC','Wheezing', 'ChestTightness','NighttimeSymptoms','ExerciseInduced']
        asthma_default = [0, 0, 0, 2.55, 3.74, 0, 1, 0, 1]
        asthma_test_input = [inputDict["age"], inputDict["gender"], inputDict["bmi"], inputDict["smoke"] - 1, inputDict["physical-activity"], inputDict["diet-quality"], inputDict["sleep-quality"], inputDict["pollution"],  inputDict["pollution"], inputDict["pollution"], inputDict["pollution"], inputDict["allergies"] - 1, inputDict["fam-asthma"], inputDict["allergies"] - 1, inputDict["shortBreath"] - 1, inputDict["chronicCough"] - 1]
        asthma_test = asthma_test_input + asthma_default
        asthma_dict = dict(zip(asthma_columns,asthma_test))
        asthma_input = pd.DataFrame([asthma_dict])

        # -------------------------------------

        breast_cancer_columns = ['Age_group', 'family_history', 'age_menarche' ,'age_first_birth', 'menopaus','bmi_group', 'Race' , 'current_hrt','biophx']
        breast_cancer_default = [1, 0, 0]
        breast_cancer_test_input = [inputDict["age_breast"], inputDict["fam-bc"], inputDict["firstPeriod"], inputDict["firstBaby"], inputDict["menopause"], inputDict["bmi_breast"]]
        breast_cancer_test = breast_cancer_test_input + breast_cancer_default
        breast_cancer_dict = dict(zip(breast_cancer_columns,breast_cancer_test))
        breast_cancer_input = pd.DataFrame([breast_cancer_dict])

        # --------------------------------------------------------

        with open('ML_Models/anaemia.pkl', 'rb') as file:
            anaemia_model = pickle.load(file)

        with open('ML_Models/asthma.pkl', 'rb') as file:
            asthma_model = pickle.load(file)

        with open('ML_Models/breast.pkl', 'rb') as file:
            breast_model = pickle.load(file)

        with open('ML_Models/diabetes.pkl', 'rb') as file:
            diabetes_model = pickle.load(file)

        with open('ML_Models/heart.pkl', 'rb') as file:
            heart_model = pickle.load(file)

        with open('ML_Models/lung.pkl', 'rb') as file:
            lung_model = pickle.load(file)

        output = { "Anemia" : (anaemia_model.predict(anaemia_input)[0]), "Asthma" : (asthma_model.predict(asthma_input)[0]), "Breast Cancer" : (breast_model.predict(breast_cancer_input)[0]), "Diabetes" : (diabetes_model.predict(diabetes_input)[0]), "Heart Disease" : (heart_model.predict(heart_input)[0]), "Lung Cancer" : (lung_model.predict(lung_cancer_input)[0])}
        
        data = {"BMI" : round(inputDict["bmi"], 1)}
        
        for i in output:
            number = output[i]
            if(number < 0.6):
                output[i] = "Low Risk"
            elif(number >= 0.6 and number < 0.80):
                output[i] = "Medium Risk"
            elif(number >= 0.8 and number <=1):
                output[i] = "High Risk"
            else:
                output[i] = "Sorry!"

            data[i] = output[i]

        if(inputDict["gender"] == 1):
            del data["Breast Cancer"]

        return render_template('./result.html', data = data)
    
    return redirect('/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)