import pandas as pd

#Gebruik deze functie om excel bestanden samen te voegen. Voordat je dit gebruikt comment wel de df_merged.loc regel uit
#Je zou ook de regel aan kunnen passen om op lege velden punten te plaatsen
def bestanden_samenvoegen(main_excel_bestand, excel_bestand_2, gemerged_bestand, merge_on_column1, merge_on_column2):
    df1 = pd.read_excel(main_excel_bestand, dtype=str)
    df2 = pd.read_excel(excel_bestand_2, dtype=str)

    #Verwijder mogelijke spaties in de columns waarmee je merged
    df1[merge_on_column1] = df1[merge_on_column1].astype(str).str.strip()
    df2[merge_on_column2] = df2[merge_on_column2].astype(str).str.strip()

    #Merge de bestanden
    df_merged = pd.merge(df1, df2, left_on=merge_on_column1, right_on=merge_on_column2, how='left')

    #Plaatst punten waar lege cellen zitten in de rijen met de GM codes
    df_merged.loc[df1[merge_on_column1].str.startswith("GM", na=False), :] = df_merged.fillna('.')

    #Sla het resultaat op
    df_merged.to_excel(gemerged_bestand, index=False)

    return gemerged_bestand

#V1 van de toevoeging van PC4 codes, deze functie voegt rijen toe op basis van unieke combinaties van de columns
#Dit kan er wel voor zorgen dat je veel en veel meer rijen krijgt dan je orgineel had
def add_pc4_to_dataset_as_rows (dataset, locatie_dataset, locatie_code_column, locatie_code_column_locatie_dataset):
    dataframe = pd.read_excel(dataset)

    ld_frame = pd.read_excel(locatie_dataset)
    ld_frame = ld_frame[[locatie_code_column_locatie_dataset, "PC4"]]

    dataframe = pd.merge(dataframe, ld_frame, left_on=[locatie_code_column], right_on=[locatie_code_column_locatie_dataset], how ='left')
    
    dataframe.drop(columns=[locatie_code_column_locatie_dataset], inplace=True)
    dataframe = dataframe.drop_duplicates()
    dataframe.to_excel(dataset, index=False)
    
    return dataframe

#V2 van de toevoeging van PC4 codes, deze functie voegt sets van PC4 codes toe per Buurtcode/rij
#Dit kan zorgt er wel voor dat de data lastiger te koppelen zal zijn met andere data met behulp van pc4
def add_pc4_to_dataset_as_sets (dataset, locatie_dataset, locatie_code_column, locatie_code_column_locatie_dataset):
    dataframe = pd.read_excel(dataset)

    ld_frame = pd.read_excel(locatie_dataset)
    ld_frame = ld_frame[[locatie_code_column_locatie_dataset, "PC4"]]

    ld_frame = ld_frame.groupby(locatie_code_column_locatie_dataset)["PC4"].apply(lambda x: ', '.join(map(str, sorted(set(x))))).reset_index()
    dataframe = pd.merge(dataframe, ld_frame, left_on=locatie_code_column, right_on=locatie_code_column_locatie_dataset, how='left')

    dataframe.drop(columns=[locatie_code_column_locatie_dataset], inplace=True)
    dataframe.to_excel(dataset, index=False)
    
    return dataframe

#Gebruik deze functie om een column genaamd PC4 toe te voegen, waarin PC4 codes zitten, aan een dataset waarin PC6 codes zitten
def add_pc4_to_pc6 (dataset, PC6_column, file_name):
    dataframe = pd.read_excel(dataset)
    dataframe['PC4'] = dataframe[PC6_column].str[:-2]
    dataframe.to_excel(file_name, index=False) #Dit slaat de aanpassingen op in de echte dataset
    return dataframe

#Gebruik deze functie om een csv bestand te converten naar een excel bestand
def convert_csv_to_excel (dataset, excel_file_path):
    dataframe = pd.read_csv(dataset)
    dataframe.to_excel(excel_file_path, index=False)
    return excel_file_path

#Gebruik deze functie om columns te verwijderen. Je geeft een lijst mee aan de functie, waarin de namen van de columns staan die je wilt verwijderen
def drop_columns (dataset, column_names):
    dataframe = pd.read_excel(dataset)
    dataframe.drop(columns=column_names, inplace=True)
    dataframe.to_excel(dataset, index=False)

# drop_columns("Python_Scripts/Bewerkte_datasets/Leefbaarometer-scores.xlsx" , ["afw", "fys", "onv", "soc", "vrz", "won"])

# bestanden_samenvoegen("Python_Scripts/Ruwe_datasets/NED_2019.xlsx", "Python_Scripts/Ruwe_datasets/Huisartsenaanbod in 2019 - Kaart op gemeenteniveau.xlsx", 
#                             "Python_Scripts/Bewerkte_datasets/zorgaanbod_2019.xlsx", "Codering_3", "geo_id")

# add_pc4_to_dataset_as_rows("Python_Scripts/Ruwe_datasets/NED_2019.csv", "Python_Scripts\Ruwe_datasets\Huisartsenaanbod in 2019 - Kaart op gemeenteniveau.csv", 
#                    "bu_code", "BuurtCode")

# file_name = "Python_Scripts/Bewerkte_datasets/2b-GWB2023_PC6.xlsx"

# locatie_dataframe = pd.read_excel(file_name)

# unique_buurtcodes = pd.DataFrame(locatie_dataframe["BuurtCode"].unique(), columns=["Buurtcode"])
# unique_buurtcodes.to_excel("Python_Scripts/Bewerkte_datasets/Afstand_tot_huisartsenpraktijk.xlsx", index=False)

# Deze code heb ik gebruikt om aan de locatie dataset de regio codes toe te voegen
# df2 = pd.read_csv("Datasets/Gebieden_in_Nederland_2023_25032025_175459.csv", sep=";")
# df2 = df2[["Codes en namen van gemeenten/Code (code)","Lokaliseringen van gemeenten/GGD-regio's/Code (code)"]]
# df2['Codes en namen van gemeenten/Code (code)'] = df2['Codes en namen van gemeenten/Code (code)'].astype(str).str.strip()
# print(df2.head(8))
# df = pd.merge(df, df2, left_on=['GemCode'], right_on=['Codes en namen van gemeenten/Code (code)'], how ='left')
# df.drop(columns=['Codes en namen van gemeenten/Code (code)'], inplace=True)
# df.to_excel(file_name, index=False)