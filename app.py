import numpy as np
import pickle

loaded_model=pickle.load(open("C:/Users/bijoyroy/OneDrive/Desktop/ML/Tensorflow/NewStreamlit/DiabeticePredictionStreamlit/trained_model.sav","rb"))

input_data=(3,74,68,28,45,29.7,0.293,23)

# Changing the input_data to numpy array
input_data_as_numpy_array=np.asarray(input_data)

#reshape the array as we are predicting for one instance.
input_data_reshape=input_data_as_numpy_array.reshape(1,-1)

#Sdandardize the input data.
#std_data=std.transform(input_data_reshape)
print(input_data_reshape)
prediction=loaded_model.predict(input_data_reshape)
print(prediction)
if (prediction==0):
    print("The Person is not Diabetic.")
else:
    print("The Person is Diabetic.")