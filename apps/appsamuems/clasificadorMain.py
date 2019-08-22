# coding=utf-8
"""
Uso sencillo de "StringTagger" para el etiquetado (clasificación) de texto.
"""
import pickle
import time

__author__ = "ProyectoIntegrador"

#clf = Classifier() # Instancia del clasificador

'''for category, urls in DataH.items(): # Entrenamos al clasificador con el contenido de cada pagina
	for url in urls:
		time.sleep(1)
		clf.train(getTextPage(url),category) # El metodo "getTextPage", recibe como argumento una url para extraer su texto

# Iniciamos el proceso de clasificación con el metodo "String"
# Solo le pasamos como argumento el texto que deseamos etiquetar (clasificar)
print('#######Entrenamiento completo######')
'''
"""
Crear el archivo con la informacion del entrenamiento
"""
#with open('clf','wb') as picklefile:
#	pickle.dump(clf,picklefile)

"""
Usar el archivo creado con la informacion del entrenamiento
"""
with open('clf', 'rb') as clasificador:
	modelo = pickle.load(clasificador)

string = "sangrado en las muelas del juicio final 2"
#clas = modelo.String(string)
clas = modelo.String(string)
print('\n')
print("Texto: %s " % string)
print("Etiqueta del Texto: %s" % clas)
