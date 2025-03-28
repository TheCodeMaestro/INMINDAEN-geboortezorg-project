import pandas as pd
import geopandas as gpd

file_name = "Bewerkte_datasets/2b-GWB2023_PC6.xlsx"

df = pd.read_excel(file_name)



#Gebruik deze functie om een column genaamd PC4 toe te voegen, waarin PC4 codes zitten, aan een dataset waarin PC6 codes zitten
def add_pc4_to_pc6 (dataframe, PC6_column):
    dataframe['PC4'] = dataframe[PC6_column].str[:-2]
    dataframe.to_excel(file_name, index=False) #Dit slaat de aanpassingen op in de echte dataset
    return dataframe

#Gebruik deze functie om columns te verwijderen. Je geeft een lijst mee aan de functie, waarin de namen van de columns staan die je wilt verwijderen
def drop_columns (column_names):
    df.drop(columns=column_names, inplace=True)
    df.to_excel(file_name, index=False)


# Deze code heb ik gebruikt om aan de locatie dataset de regio codes toe te voegen
# df2 = pd.read_csv("Datasets/Gebieden_in_Nederland_2023_25032025_175459.csv", sep=";")
# df2 = df2[["Codes en namen van gemeenten/Code (code)","Lokaliseringen van gemeenten/GGD-regio's/Code (code)"]]
# df2['Codes en namen van gemeenten/Code (code)'] = df2['Codes en namen van gemeenten/Code (code)'].astype(str).str.strip()
# print(df2.head(8))
# df = pd.merge(df, df2, left_on=['GemCode'], right_on=['Codes en namen van gemeenten/Code (code)'], how ='left')
# df.drop(columns=['Codes en namen van gemeenten/Code (code)'], inplace=True)
# df.to_excel(file_name, index=False)