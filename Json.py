import json


nuevoUsuario = [

               {'Nombre': 'Josuevd', 'Contraseña': 'pruebapass', },
               {'Nombre': 'Carlos', 'Contraseña': '4321', },
               ]
  #Vamos a escribir la lógica para poder abrir un  Json             
               
with open("demo.json"  ,    'w') as json_file:
    json.dump(nuevoUsuario, json_file)

#Vamos a escribir la lógica para poder Leer un Json

with open ("demo.json") as json_file:
    data = json.load(json_file)


print(data)



