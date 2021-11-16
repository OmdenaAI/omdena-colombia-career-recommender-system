import numpy as np
import pandas as pd
import streamlit as st


import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import time

from tensorflow.keras.models import load_model


st.markdown(
        f"""
<style>
    .reportview-container .main .block-container{{
        max-width: 60%;
        padding-top: 5rem;
        padding-right: 5rem;
        padding-left: 5rem;
        padding-bottom: 5rem;
    }}
    img{{
        max-width:100%;
        margin-bottom:100px;
    }}
</style>
""",
        unsafe_allow_html=True,
    )




# Deprecation Warning.
st.set_option('deprecation.showPyplotGlobalUse', False)

# here is how to create containers
header_container = st.container()
stats_container = st.container()    
#######################################


### Prediction function
def predict(arr):
    
    # Loading Model
    model = load_model("model_career_RS.h5")
    classes = { 0: 'BUSINESS', 1: 'SPORTS AND PHYSICAL TRAIN', 2: 'ENGINEERING',3: 'AGRONOMIC, LIVESTOCK ENGINEERING',
                4: 'HUMANITIES AND SOCIAL SCIENCE', 5: 'MATH AND PHYSICAL SCIENCES', 6: 'NUTRITION AND DIETETICS',
                7: 'HEALTH & MEDICINE', 8: 'ARTS AND DESIGN', 9: 'BIOLOGICAL SCIENCE',
                10: 'AGRICULTURAL, FOREST ENGINEERING',  11: 'PLASTIC ARTS, VISUAL ARTS', 12: 'PHISICS'
                }
    # return prediction as well as class probabilities
    preds = model.predict([arr])[0]
    
    return (classes[np.argmax(preds)], preds)






# You can place things (titles, images, text, plots, dataframes, columns etc.) inside a container
with header_container:

    # for example a logo or a image that looks like a website header
    st.image('logo_recsys.png')

    # different levels of text you can include in your app
    st.title("Colombia - Career Recommendation System.")
    st.header("Welcome!")


# Another container
with stats_container:



    classes = {0: 'BUSINESS',1: 'SPORTS AND PHYSICAL TRAIN',2: 'ENGINEERING',3: 'AGRONOMIC, LIVESTOCK ENGINEERING',
                4: 'HUMANITIES AND SOCIAL SCIENCE',5: 'MATH AND PHYSICAL SCIENCES',6: 'NUTRITION AND DIETETICS',
                7: 'HEALTH & MEDICINE',8: 'ARTS AND DESIGN',9: 'BIOLOGICAL SCIENCE',10: 'AGRICULTURAL, FOREST ENGINEERING',
                11: 'PLASTIC ARTS, VISUAL ARTS',12: 'PHISICS'}
    class_labels = list(classes.values())

    st.markdown('**Objective** : Given details about the scores we try to recommend top 5 careers to student.')
    

    def predict_class():
        data = list(map(int,[score_language,score_mathematics,score_biology,score_chemistry,score_physics,score_social_science,score_philosophy,score_english]))
        result, probs = predict(data)
        #st.write("The predicted class is ",result)
        res= f'"The predicted class is: {result}'
        st.success(res)
        probs = [np.round(x,6) for x in probs]
        
        plt.figure(figsize=(20,10))
        ax = sns.barplot(x= probs ,y= class_labels, palette="winter", orient='h')#,order=probs.sort(reverse=True))
        ax.set_yticklabels(class_labels,rotation=0)
        plt.title("Probabilities of the Data belonging to each class")
        for index, value in enumerate(probs):
            plt.text(value, index,str(value))
        st.pyplot()


    st.markdown("**Please enter the details of the Score ranging from 1 to 100 **")
    

    #get Scores input
        
    score_language       =  st.slider("Language Score", 1, 100,1)
    score_mathematics    =  st.number_input('Mathematic Score',min_value=1, max_value=100)
    score_biology        =  st.slider("Biology Score", 1, 100,1)
    score_chemistry      =  st.number_input('Chemistry Score',min_value=1, max_value=100)
    score_physics        =  st.slider("Physics Score", 1, 100,1)
    score_social_science =  st.number_input('Social_science Score',min_value=1, max_value=100)
    score_philosophy     =  st.slider("Philosophy Score", 1, 100,1)
    score_english        =  st.number_input('English Score',min_value=1, max_value=100)

    if st.button("Recommend"):
        with st.spinner('Please Wait! The Recommendation Engine is working...'):
            time.sleep(5)
            predict_class()













