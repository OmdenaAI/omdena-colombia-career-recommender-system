# Task 1 - EDA and Preprocessing

## Summary

The objective of __task 1__ folder is to share the Scrips and Jupyter Notebooks coded to present the [EDA](https://en.wikipedia.org/wiki/Exploratory_data_analysis) and preprocessing the data.  

In the main repository lives the `EDA.py` srcipt that cointains the main analysis taken from diverse Jupyter notebooks shared by the participants of this project, which are located in the `EDA_notebook` folder with the initial analysis. Also, you will find a script that translates the database of this project from Spanish to English (`Translate_data.py`) and a script that wrangle and clean the database (`data_cleaning.py`).


## Usage

In __Task 1__, three functions are included for the EDA and preprocessing:

- `Translate_data.py`

    After downloading the database `saber_combined_all_fields.csv` to a pandas data frame named as `df`, we could run the following code to translate data from Spanish to English:

    ```python
    # translates the database
    import Translate_data as td
    df_2 = td.translate_data(df)
    ```

- `EDA.py`
    To run the EDA script to see the analysis, you could use the following code:

    ```python
    # Performs EDA
    import EDA
    EDA.eda(df_2)
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
