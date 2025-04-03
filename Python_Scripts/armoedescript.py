import pandas as pd

# Define file paths
input_file = r"C:\Users\gebruiker\Downloads\kwb-2023.xlsx"
output_file = r"C:\Users\gebruiker\Downloads\kwb-2023-transformed.xlsx"

# List of required columns (green highlighted variables from the document)
required_columns = [
    'gwb_code_10',        # Codering
    'gm_naam',            # Gemeentenaam
    'a_inw',              # Aantal inwoners
    'a_ongeh',            # Ongehuwd
    'a_gehuwd',           # Gehuwd
    'a_gesch',            # Gescheiden
    'a_verwed',           # Verweduwd
    'a_nl_all',           # Nederland (herkomst)
    'a_eur_al',           # Europa (exclusief Nederland)
    'a_neu_al',           # Buiten Europa
    'a_hh',               # Huishoudens totaal
    'a_1p_hh',            # Eenpersoonshuishoudens
    'a_hh_z_k',           # Huishoudens zonder kinderen
    'a_hh_m_k',           # Huishoudens met kinderen
    'g_hhgro',            # Gemiddelde huishoudensgrootte
    'bev_dich',           # Bevolkingsdichtheid
    'g_wozbag',           # Gemiddelde WOZ-waarde
    'g_ink_pi',           # Gemiddeld inkomen per inwoner
    'p_ink_li',           # 40% personen met laagste inkomen
    'p_ink_hi',           # 20% personen met hoogste inkomen
    'g_hh_sti',           # Gem. gestandaardiseerd inkomen van huishouden
    'p_hh_li',            # 40% huishoudens met laagste inkomen
    'p_hh_hi',            # 20% huishoudens met hoogste inkomen
    'a_soz_wb',           # Personen per soort uitkering; Bijstand
    'a_soz_ao',           # Personen per soort uitkering; AO
    'a_soz_ww',           # Personen per soort uitkering; WW
    'a_soz_ow',           # Personen per soort uitkering; AOW
    'a_jz_tn',            # Jongeren met jeugdzorg in natura
    'p_jz_tn',            # Percentage jongeren met jeugdzorg
    'a_wmo_t',            # Wmo-cliënten
    'p_wmo_t',            # Wmo-cliënten relatief
    'a_pau',              # Personenauto's totaal
    'a_bst_b',            # Personenauto's; brandstof benzine
    'a_bst_nb',           # Personenauto's; overige brandstof
    'g_pau_hh',           # Personenauto's per huishouden
    'g_pau_km',           # Personenauto's naar oppervlakte
    'g_afs_hp',           # Afstand tot huisartsenpraktijk
    'g_afs_gs',           # Afstand tot grote supermarkt
    'g_afs_kv',           # Afstand tot kinderdagverblijf
    'g_afs_sc',           # Afstand tot school
    'g_3km_sc',           # Scholen binnen 3 km
    'ste_mvs',            # Mate van stedelijkheid
    'ste_oad'             # Omgevingsadressendichtheid
]

# Load the Excel file
df = pd.read_excel(input_file)

# Check which required columns exist in the dataframe
available_columns = [col for col in required_columns if col in df.columns]
missing_columns = [col for col in required_columns if col not in df.columns]

if available_columns:
    # Extract the available columns
    df_selected = df[available_columns]
    
    # Save to a new Excel file
    df_selected.to_excel(output_file, index=False)
    print(f"Successfully saved {len(available_columns)} columns to {output_file}")
    
    if missing_columns:
        print(f"\nWarning: The following columns were not found in the input file:")
        for col in missing_columns:
            print(f"- {col}")
else:
    print("None of the required columns were found in the input file.")