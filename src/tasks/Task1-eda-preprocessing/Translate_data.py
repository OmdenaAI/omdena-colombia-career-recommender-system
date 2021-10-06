# Load libraries
# To download the data from Google Drive
# !pip install gdown
# import gdown
import numpy as np
import pandas as pd
import urllib.request as urllib2
import ast

def translate_data(df_in, lan_1="Spanish", lan_2="English"):
    """
    Function that translates the database for the Omdena challenge of Colombia's chapter
    related to a Career recommender system, which translates a pandas data rame from English 
    to Spanish, and vice versa.
    
    Parameters
    -------------
    df_in : (pandas data frame)
        data frame with variables and values of the main database from the Omdena challenge of 
        Colombia's chapter related to a Career recommender system.
    lan_1 : (str)
        language of the database, options "spanish" and "english".
    lan_2 : (str)
        language to translate, options "spanish" and "english".
        
    Returns
    -------------
    (pandas data frame) data frame with the translation of the data base.
    
    Example
    -------------
    # LIBRARIES
    from Translate_data import translate_data
    import pandas as pd

    # DATAFRAME WITH COLUMNS AND VARIABLES FROM OMDENA'S PROJECT
    data = {'estu_nacionalidad':['MÉXICO', 'ESTADOS UNIDOS', 'CANADÁ', 'PERÚ'],
            'estu_estadocivil':['Soltero', 'Casado', 'Viudo', 'Soltero'],
            'profundiza':['PUNT_PROFUNDIZA_BIOLOGIA', 'PUNT_PROFUNDIZA_MATEMATICA',
                        'PUNT_PROFUNDIZA_CSOCIALES', 'PUNT_PROFUNDIZA_CSOCIALES']}
    df_spanish = pd.DataFrame(data)

    # TRANSLATION
    df_english = translate_data(df_spanish, 'spanish', 'english')
    print(df_english)
    (output:)   your_nationality your_marital_status      optative_field_saber_11
              0           MEXICO              Single         SCORE_DEEPEN_BIOLOGY
              1              USA             Married     SCORE_DEEPEN_MATHEMATICS
              2           CANADA             Widowed  SCORE_DEEPEN_SOCIAL_SCIENCE
              3             PERU              Single  SCORE_DEEPEN_SOCIAL_SCIENCE
    """
    ##### LOADING DATA #####
    # Get lowercase language
    lan_1 = lan_1.lower()
    lan_2 = lan_2.lower()
    df_out = df_in.copy()

    # dictionary of headers
    contents = str("")
    for line in urllib2.urlopen("https://raw.githubusercontent.com/vcuspinera/Datasets/main/omdena/colombia-career-recommender-system/translate_headers.txt"):
        contents += str(line)[2:-5]
    contents += "}"
    dic_header = ast.literal_eval(contents.lower())

    # dictionary of categorical variables
    contents = str("")
    for line in urllib2.urlopen("https://raw.githubusercontent.com/vcuspinera/Datasets/main/omdena/colombia-career-recommender-system/translate_cat.txt"):
        contents += str(line)[2:-3]
    contents += "}"
    char_to_replace = {
        "\\r": "", "\\": "", # characters
        "xc3x81": "Á", "xc3x89": "É", "xc3x8d": "Í", "xc3x93": "Ó", "xc3x9a": "Ú", "xc3x9c": "Ü", "xc3x91": "Ñ", # capital letters
        "xc3xa1": "á", "xc3xa9": "é", "xc3xad": "í", "xc3xb3": "ó", "xc3xba": "ú", "xc3xb1": "ñ" # lowercase letters
    }
    for key, value in char_to_replace.items():
        contents = contents.replace(key, value)
    dic_cat = ast.literal_eval(contents)

    ##### TRANSLATE FROM SPANISH TO ENGLISH #####
    if ((lan_1 == "spanish") and (lan_2 == "english")):

    # Translate values
        # select categorical columns
        cat_col=df_out.select_dtypes(include='object').columns.to_list()

        # translates to English the values of the data frame
        for i in cat_col:
            try:
                df_out.replace({i: dic_cat[i]}, inplace=True)
            except:
                next
    
    # Translate header
        df_out = df_out.rename(columns=dic_header)
        
    ##### TRANSLATE FROM ENGLISH TO SPANISH #####
    elif ((lan_1 == "english") and (lan_2 == "spanish")):
    
    # Translate header
        try:
            my_col_num = list()
            my_col_nam = list()
            my_col_num = [list(dic_header.values()).index(i) for i in df_out.columns]
            my_col_nam = [list(dic_header.keys())[i] for i in np.asarray(my_col_num)]
            df_out.columns = my_col_nam
        except:
            next

    # Translate values
        # select categorical columns
        cat_col = df_out.select_dtypes(include='object').columns.to_list()

        # translates to English the values of the data frame
        for i in cat_col:
            try:
                reverse_dics = dict(zip(list(dic_cat[i].values()),
                                        list(dic_cat[i].keys())))
                df_out.replace({i: reverse_dics}, inplace=True)
            except:
                next
    
        
    ##### ERROR IF IT DOESN'T PASS ENGLIS OR SPANISH LANGUAGES #####
    else:
        print("Only translation of spanish to english and vice versa.")
        df_out=pd.DataFrame()
    
    return (df_out)
