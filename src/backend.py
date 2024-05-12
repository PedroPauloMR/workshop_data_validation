import pandas as pd 
import os 
from contrato import Vendas 
from dotenv import load_dotenv

load_dotenv()

POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DB = os.getenv('POSTGRES_DB')

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


def process_excel(uploaded_file):
    try:
        df = pd.read_excel(uploaded_file)

        extra_cols = set(df.columns) - set(Vendas.model_fields.keys())
        if extra_cols:
            return None,False, f"Colunas extras detectadas no Excel: {', '.join(extra_cols)}"
        
        for index, row in df.iterrows():
            try:
                _ = Vendas(**row.to_dict())
            except Exception as e:
                raise ValueError(f"Erro na linha {index + 2}: {e}")
            
        return df,True, None
    
    except ValueError as ve:
        return  None,False, str(ve)
    
    except Exception as e:
        return  None,False, f"Erro inesperado: {str(e)}"
    

def excel_to_sql(df):
    df.to_sql('vendas', con = DATABASE_URL, if_exists = 'replace', index = False)
