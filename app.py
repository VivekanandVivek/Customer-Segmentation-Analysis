import streamlit as st
import numpy as np
import pandas as pd
import pickle 

pickle_in = open('C:\\Users\\Dell\\OneDrive\\Desktop\\CUSTONALYSIS\\cluster.pkl', 'rb')


Km = pickle.load(pickle_in)

def Student_Segmentation (MonetoryValue , Frequency , Recency):

    MonetoryValue =float (MonetoryValue )
    Frequency     =float (Frequency     )
    Recency       =float (Recency       )

    prediction = Km.predict([[MonetoryValue , Frequency , Recency]])

    print(prediction[0])
    return prediction[0]

def main():
    st.title("Customer Analyser")   
    html_temp = """
    <div style = "background-color : tomato; padding : 10px">
    <h2 style = "color:white ; text-align:centre;> Customer Analyser ML App</h2>
    </div>
    """

    st.markdown(html_temp, unsafe_allow_html= True)

    MonetoryValue =st.text_input('MonetoryValue','')
    Frequency     =st.text_input('Frequency','')
    Recency       =st.text_input('Recency','')


    result = ""

    if st.button("predict"):
        result = Student_Segmentation (MonetoryValue , Frequency , Recency)
        if result == 0 :
            result = 'Targeted Customer'
        elif result ==1 : 
            result  ='This Customer is at Risk' 
        elif result == 2 :
            result  = 'New Customer'
        else :
            result = "Churned Customer"
       
    st.success("The Output is {}".format(result))    
    if st.button("About"):
        st.text("Let's Learn")

        st.text("Built With Streamlit")
 

if __name__ == '__main__' :
    main()