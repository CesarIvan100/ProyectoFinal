import pandas as pd
import os

# ruta absoluta de la carpeta donde esta el script (.../scripts/)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# construir la ruta del archivo csv
DATA_PATH = os.path.join(SCRIPT_DIR, "..", "data", "games_clean.csv")


# crear de funcion

def cargar_datos(path):
    print(f"Cargando datos desde el {path}...")
    
    try:
        df = pd.read_csv(path)
        print("Datos cargados!!!")
        return df
    except FileNotFoundError:
        print("Error: no se encontro el archivo en {path}")
        print("Asegurate de tener el archivo en la carpeta 'data'.")
        return None
    except Exception as e:
        print("Ocurrio un erro inesperado {e}")
        return None
    
# Este archivo se esta ejecutando por el usuario o esta ejecutando por otro script

if __name__ == "__main__":
    #indica donde esta en scrip actual
    print(f"Ejecutando script desde: {os.path.abspath(__file__)}")
    
    # llama a la funcion de arriba para cargar el csv
    dataframe_juegos = cargar_datos(DATA_PATH)
    
    if dataframe_juegos is not None:
        print("\n --- primeras 5 filas ---")
        print(dataframe_juegos.head())
        
        print("\n --- Informacion del Dataframe---")
        dataframe_juegos.info(show_counts=True)
