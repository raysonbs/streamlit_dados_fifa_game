import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime, date

if "data" not in st.session_state:
    df_data = pd.read_csv(r"C:\Users\RAYSON\3_Streamlit_Game_Dados_Fifa\datasets\CLEAN_FIFA23_official_data.csv",index_col=0)
    df_data = df_data[df_data['Contract Valid Until'] >= datetime.today().year]
    df_data = df_data[df_data['Value(£)'] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data




st.markdown('# FIFA 2023 OFICIAL DATASET ⚽')

st.sidebar.markdown("Desenvolvido por Rayson")

btn = st.button("Acesso os dados no Kaggle")
if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/code/stefanoleone992/ea-sports-fc-24-players-lineup-visualizations")
    
st.markdown(
    """
    FIFA is one of the most popular videogames that get released every year, and from the season 2023/24 it has been officially renamed to EA Sports FC 24 due to lack of FIFA license. 
    
    The purpose of this notebook is to analyse the FIFA players dataset available at this Kaggle link, which provide information regarding players such as age, overall and potential attributes, club and league name, positions, and many others from the latest 10 editions of FIFA (from the 15th to the 24th). 
    
    Once the dataset is read with pandas and the missing data gets displayed with the missingno library, some customized Python functions allow to draw the match-up against the best lineups of two teams on a football pitch. 
    
    The next step is the analysis of the players dataset, looking for insights about clubs, leagues and players.
    
    """
)

