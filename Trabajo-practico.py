import pandas as pd
import numpy as np
import datetime as dt
pd.DataFrame()

data = pd.read_csv("D:\RUBEN\Downloads\Spotify 2010 - 2021 Top 100.csv", sep=",")

#indie_dur = df[df["top genre"]== "indie rock"]["dur"].sum()

#print(indie_dur)
class PlayList():
    def __init__(self,filtro, filtro1):
        self.filtro = filtro
        self.filtro1 = filtro1
        
    def generador_de_listas(filtro, filtro1):
        lista = data[data[filtro] == filtro1]
        return lista
    
    def calcula_duracion(filtro, filtro1):
        duracion = data[data[filtro] == filtro1]["dur"].sum()  
        horas = duracion//3600
        sobrante1 =duracion%3600
        minutos = sobrante1//60
        sobrante2 = sobrante1%60
        duracion_total = horas, minutos, sobrante2
        return duracion_total
    
    
indie = PlayList.generador_de_listas("top genre", "indie rock")
indie_duracion = PlayList.calcula_duracion("top genre", "indie rock")
    
    
print(indie)   

print(indie_duracion) 