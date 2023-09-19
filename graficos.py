import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


nombre_archivo = "Spotify 2010 - 2021 Top 100.csv"

def leer_archivo(nombre_archivo):
    data = pd.read_csv(nombre_archivo, sep=",")
    return data
data = leer_archivo(nombre_archivo)
ejex = list(data["year released"].unique())
ejey = []
for genero in ejex:
    ejey.append(len(data[data["year released"]== genero]))
fig, ax = plt.subplots()   
ax.bar(ejex, ejey)    




def calcula_duracion(filtro, filtro1):
        duracion = data[data[filtro] == filtro1]["dur"].sum()  
        horas = duracion//3600
        sobrante1 =duracion%3600
        minutos = sobrante1//60
        sobrante2 = sobrante1%60
        horas = horas 
        minutos = minutos 
        segundos = sobrante2
        return horas, minutos, segundos
    
subtotal = calcula_duracion("top genre", "dance pop")    
    
    
def calcula_duracion_2():
        hora1 = subtotal // 360
        sobra = hora1%360
        minutos1 = sobra // 60
        sobra1 = sobra%60
        
        return hora1, minutos1, sobra1
    
    
print(calcula_duracion_2)         
        