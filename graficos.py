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