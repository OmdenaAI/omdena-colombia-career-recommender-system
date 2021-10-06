# Task 1 - EDA and Preprocessing

## Summary

The objective of __task 1__ folder is to share the Scrips and Jupyter Notebooks coded to present the [EDA](https://en.wikipedia.org/wiki/Exploratory_data_analysis) and preprocessing the data.  

In the main repository lives the `EDA.py` srcipt that cointains the main analysis taken from diverse Jupyter notebooks shared by the participants of this project, which are located in the `EDA_notebook` folder with the initial analysis. Also, you will find a script that translates the database of this project from Spanish to English (`Translate_data.py`) and a script that wrangle and clean the database (`data_cleaning.py`).


## Usage

In __Task 1__, three Python Scripts are included for the EDA and preprocessing raw dataset:

- `Translate_data.py`  

    After downloading the database `saber_combined_all_fields.csv` to a pandas data frame named as `df`, we could run the following code to translate data from Spanish to English:

    ```python
    # translates the database
    import Translate_data as td
    df_2 = td.translate_data(df)
    ```
    
    Output:  
    
    ```python
    	Unnamed: 0	your_type_of_document	your_nationality	your_gender	your_birthdate	your_foreigner	period	your_consecutive	your_marital_status	your_student	...	score_biology_saber_11	score_chemistry_saber_11	score_physics_saber_11	score_social_science_saber_11	score_philosophy_saber_11	score_english_saber_11	score_english_saber_11_category	optative_field_saber_11	score_optative_saber_11	optative_category_saber_11
    0	0	TI	COLOMBIA	M	30/07/1996	NaN	20134	EK201340233804	Single	STUDENT	...	39.0	42.0	33.0	33.0	29.0	38.0	A-	SCORE_INTERDISC_ENVIRONMENT	49.0	NaN
    1	1	CC	COLOMBIA	M	13/04/1994	NaN	20133	EK201330220754	Single	STUDENT	...	52.0	52.0	54.0	44.0	47.0	51.0	A1	SCORE_DEEPEN_LANGUAGE	6.0	II
    ...
    ```

- `EDA.py`  

    To run the EDA script to see the analysis, you could use the following code:

    ```python
    # Performs EDA
    import EDA
    EDA.eda(df_2)
    ```
    
    Output:  
    
    ```python
    Preview of data:
    Unnamed: 0	your_type_of_document	your_nationality	your_gender	your_birthdate	your_foreigner	period	your_consecutive	your_marital_status	your_student	...	score_biology_saber_11	score_chemistry_saber_11	score_physics_saber_11	score_social_science_saber_11	score_philosophy_saber_11	score_english_saber_11	score_english_saber_11_category	optative_field_saber_11	score_optative_saber_11	optative_category_saber_11
    0	0	TI	COLOMBIA	M	30/07/1996	NaN	20134	EK201340233804	Single	STUDENT	...	39.0	42.0	33.0	33.0	29.0	38.0	A-	SCORE_INTERDISC_ENVIRONMENT	49.0	NaN
    1	1	CC	COLOMBIA	M	13/04/1994	NaN	20133	EK201330220754	Single	STUDENT	...	52.0	52.0	54.0	44.0	47.0	51.0	A1	SCORE_DEEPEN_LANGUAGE	6.0	II
    2	2	CC	COLOMBIA	F	08/12/1991	NaN	20134	EK201340246502	Single	STUDENT	...	50.0	51.0	28.0	46.0	45.0	43.0	A-	SCORE_DEEPEN_BIOLOGY	5.0	I
    3 rows × 142 columns


    To check: 
     (1) Total number of entries 
     (2) Column types 
     (3) Any null values

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 5 entries, 0 to 4
    Columns: 142 entries, Unnamed: 0 to optative_category_saber_11
    dtypes: float64(28), int64(7), object(107)
    memory usage: 5.7+ KB
    None
    
    ...
    ```
    
- `data_cleaning.py`  

    👉 Pending for an explanation 👈


## TODO list and comments 

- I have observed that dataset has got missing values. 😒
- ~~language barier column has been written in Spanish. English will be better~~  
- we have to filter data so as to extract relevant information required to make final recommendation  
- dataset contain different type of data, numerical, categorical and non categorical, continous, etc.  
- there is a need for conversion of data types  
- let us remove missing value by filling with a mode value  
- convert categorical features to numerical by one-hot encoding method and label encoding  
- let us drop uniqueid variable  
- we have to standadize the (Scaling our data)  
- Next Step to Understand the relevant column  
- I didn't run the `data_cleaning.py` script, it would be great if the person in charge of this point could add how to use it in this README file  
