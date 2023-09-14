import pandas as pd
import numpy as np
import datetime as dt
pd.DataFrame()

nombre_archivo = "Spotify 2010 - 2021 Top 100.csv"

def leer_archivo(nombre_archivo):
    data = pd.read_csv(nombre_archivo, sep=",")
    return data

data = leer_archivo(nombre_archivo)

class PlayList():
    def __init__(self,filtro, filtro1, filtro2, orden):
        self.filtro = filtro
        self.filtro1 = filtro1
        self.filtro2 = filtro2
        self.orden = orden
        
    def lista_generica():
        lista = data
        return lista
        
        
    def generador_de_listas(filtro, filtro1):
        lista = data[data[filtro] == filtro1]
        return lista
    
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
     
    
    def ordenar_lista(filtro, filtro1, filtro2, orden):
        ordenar = True
        if orden == "asendente":
            ordenar = False
        lista_ordenada = data[data[filtro]== filtro1].sort_values(by= filtro2, ascending=ordenar)
        return lista_ordenada
    
    def list_cant_item(filtro, filtro1):
        cantidad = len(data[data[filtro]== filtro1]["title"].to_list())
        return cantidad
    
class AnalicisArchivo():
    def __init__(self, columna ):
        self.columna = columna
        
    def generos(columna):
        cant_genero = data[columna].value_counts()
        return 
    
    def ordenar_lista (filtro):
       list_ord = data.sort_values(by=filtro)
       return list_ord
        
    
       
            
indie = PlayList.generador_de_listas("top genre", "indie rock")
indie_duracion = PlayList.calcula_duracion("top genre", "indie rock")
indie_ordenada = PlayList.ordenar_lista("top genre", "indie rock", "title", "desendente")
indie_ordenada1 = PlayList.ordenar_lista("top genre", "indie rock", "artist", "asendente")
indie_cantidad_temas = PlayList.list_cant_item("top genre", "indie rock")
lista_generica = PlayList.lista_generica()
lista_by_artista =PlayList.generador_de_listas("artist", "Eminem")
hip_hop_cant_temas = PlayList.list_cant_item("top genre", "hip hop")
genero_mas_usado = AnalicisArchivo.generos("top genre")
artista_mas_aparece= AnalicisArchivo.generos("artist")
tema_mayor_duracion = AnalicisArchivo.ordenar_lista("dur")
canciones_de_Imagine_Dragon = PlayList.generador_de_listas("artist", "Imagine Dragons")
cantidad_temas_Imagine_Dragons= PlayList.list_cant_item("artist", "Imagine Dragons")


    
#print(leer_archivo(nombre_archivo))  
  
#print(indie)   

#print(f"La lista dura {indie_duracion}")

#print(indie_ordenada)

#print(indie_ordenada1)

#print(f"la cantidad de temas es {indie_cantidad_temas}")

#print(lista_generica)

#print(lista_by_artista)

#print(f"la cantidad de temas hip hop son {hip_hop_cant_temas}")

#print(f"El genero que mas aparese en el archivo es {genero_mas_usado}")

#print(f"el tema de mayor duracion es {tema_mayor_duracion}")

#print(f"El artista que mas aparese es {artista_mas_aparece}")

#print(tema_mayor_duracion)

#print(AnalicisArchivo.ordenar_lista)

#print(canciones_de_Imagine_Dragon)

#print(f"la cantidad de temas de Imagine Dragons son {cantidad_temas_Imagine_Dragons}")