from encriptor import ocultar_texto
from decriptor import leer



texto = input("ingreso:	")
print(texto)
ocultar_texto(texto, "/home/kali/Desktop/IMG_E2702.JPG")
print("el mensaje oculto es: "+leer('/home/kali/Desktop/kivy_app/encripted.png'))