import numpy as np
from numpy.core.fromnumeric import size
import pandas as pd
import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import time, os, sys
from tensorflow.keras.models import load_model

# Deprecation Warning.
st.set_option('deprecation.showPyplotGlobalUse', False)

logo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'CareerRecSys-logo.png')
st.sidebar.title("Colombia Carrer Recommender")
st.sidebar.image(logo_path, use_column_width=True)

# create containers
header_container = st.container()
stats_container = st.container()    
##################################

# Loading Model
model = load_model("model_career_RS.h5")

classes = { 0: 'BUSINESS', 
            1: 'SPORTS AND PHYSICAL TRAIN', 
            2: 'ENGINEERING',
            3: 'AGRONOMIC, LIVESTOCK ENGINEERING',
            4: 'HUMANITIES AND SOCIAL SCIENCE',
            5: 'MATH AND PHYSICAL SCIENCES', 
            6: 'NUTRITION AND DIETETICS',
            7: 'HEALTH & MEDICINE', 
            8: 'ARTS AND DESIGN', 
            9: 'BIOLOGICAL SCIENCE',
            10: 'AGRICULTURAL, FOREST ENGINEERING',  
            11: 'PLASTIC ARTS, VISUAL ARTS', 
            12: 'PHYSICS'
            }
    


st.markdown(
        f"""
        <style>
            .reportview-container .main .block-container{{
                max-width: 70%;
                padding-top: 2rem;
                padding-right: 5rem;
                padding-left: 5rem;
                padding-bottom: 3rem;
            }}
            img{{
                max-width:100%;
                margin-bottom:100px;
            }}
        </style>""", unsafe_allow_html=True)


# prediction functions
def get_model_preds(model, data):

    # get prediction probabilities from the model
    return model.predict([data])[0]


def plot_top5(probs):

    # plot the probabilities
    probs = [np.round(x,2) for x in probs]
    probas, class_lbs = zip(*sorted(zip(probs, class_labels), reverse=True)[:5])
    plt.figure(figsize=(10,8))
    ax = sns.barplot(x=list(probas), y=list(class_lbs),
                        palette="winter", orient='h')
    ax.set_yticklabels(class_lbs, rotation=0)
    plt.title(" Top 5 Recommendations & their probabilities", size=16)
    for index, value in enumerate(probas):
        plt.text(value, index, str(value))
    st.pyplot()


# You can place things (titles, images, text, plots, dataframes, columns etc.) inside a container
with header_container:
    # for example a logo or a image that looks like a website header
    st.image('CareerRecSys-logo.png', use_column_width=True)
    # different levels of text you can include in your app
    st.header("Colombia Career Recommender")


# Another container
with stats_container:
    class_labels = list(classes.values())
    st.markdown('**Welcome!** Please fill your scores in following areas to get top 5 recommended careers.')

    # score range
    st.markdown("** Score ranges limit: 1 to 100 **")
    # get Scores input
    score_mathematics    =  st.number_input('Mathematics Score:',min_value=1, max_value=100)
    score_physics        =  st.number_input("Physics Score:", min_value=1, max_value=100)
    score_chemistry      =  st.number_input('Chemistry Score:',min_value=1, max_value=100)

    score_biology        =  st.slider("Biology Score:", 1, 100,1)
    score_social_science =  st.slider('Social_science Score:',1, 100,1)
    score_language       =  st.slider("Language Score:", 1, 100,1)
    score_philosophy     =  st.slider("Philosophy Score:", 1, 100,1)
    score_english        =  st.slider('English Score:',1, 100,1)

    if st.button("Get Recommendations"):
        with st.spinner('Please Wait! Our engine is finding best possible recommendations for you...'):
            data = list(map(int,[score_language,score_mathematics,
                        score_biology,score_chemistry,score_physics,
                        score_social_science,score_philosophy,
                        score_english]))
            time.sleep(3)
            probs = get_model_preds(model, data)

            class_str = classes[np.argmax(probs)]
            # st.write("The predicted class is ",result)
            result = f'Your Top recommended career is: {class_str}'
            st.success(result)
            plot_top5(probs)










