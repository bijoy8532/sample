import numpy as np
import pickle
import streamlit as st

loaded_model=pickle.load(open("C:/Users/bijoyroy/OneDrive/Desktop/ML/Tensorflow/NewStreamlit/DiabeticePredictionStreamlit/trained_model.sav","rb"))

st.title("Diabetes Prediction Web App")
name = st.text_input('What is your name?').upper()
#gender=st.text("Please Enter Your Gender")


Gender=["Male","Female","Transgender"]
A=st.selectbox("Please Enter Your Gender", Gender)


def diabetes_prediction(input_data):

    # Changing the input_data to numpy array
    input_data_as_numpy_array=np.asarray(input_data)

    #reshape the array as we are predicting for one instance.
    input_data_reshape=input_data_as_numpy_array.reshape(1,-1)

    #Sdandardize the input data.
    #std_data=std.transform(input_data_reshape)
    print(input_data_reshape)
    prediction=loaded_model.predict(input_data_reshape)
    print(prediction)
    
    if (prediction[0]==0):
        st.write('Hurray!', name, ',You are diabetes FREE.❤️')
        return "Congratulation !!"
    else:
        st.write("Dear",name,", you either have diabetes or are likely to have it. Please visit the doctor as soon as possible.😢")
        return "Tip: Do More Physical Exercise."

        
def main():
    
    #getting the input data from the user
    #if gender=="male":
    if A==Gender[0]:
        Pregnancies=0
        Glucose=st.text_input("Glucose Level")
        BloodPressure=st.text_input("BloodPressure Value")
        SkinThickness=st.text_input("SkinThickness Value")
        Insulin=st.text_input("Insulin Level")
        BMI=st.text_input("BMI Value")
        DiabetesPedigreeFunction=st.text_input("Diabetes Pedigree Function Value")    
        Age=st.text_input("Age Of The Person")
        
    elif A==Gender[2]:
        Pregnancies=0
        Glucose=st.text_input("Glucose Level")
        BloodPressure=st.text_input("BloodPressure Value")
        SkinThickness=st.text_input("SkinThickness Value")
        Insulin=st.text_input("Insulin Level")
        BMI=st.text_input("BMI Value")
        DiabetesPedigreeFunction=st.text_input("Diabetes Pedigree Function Value")    
        Age=st.text_input("Age Of The Person")
        
    else:
        Pregnancies=st.text_input("Number of Pregnancies")
        Glucose=st.text_input("Glucose Level")
        BloodPressure=st.text_input("BloodPressure Value")
        SkinThickness=st.text_input("SkinThickness Value")
        Insulin=st.text_input("Insulin Level")
        BMI=st.text_input("BMI Value")
        DiabetesPedigreeFunction=st.text_input("Diabetes Pedigree Function Value")    
        Age=st.text_input("Age Of The Person")
    
    
    #Code For Prediction
    diagnosis=""
    
    #Creating a button for prediction
    if (st.button("predict")):
        diagnosis=diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
    
    st.success(diagnosis)
    
    
if __name__=="__main__":
    main()

    
    
    
    
    
    
    
    
    