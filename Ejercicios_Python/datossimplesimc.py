""" Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
calcule el índice de masa corporal y lo almacene en una variable, y muestre por
pantalla la frase Tu índice de masa corporal es <imc> donde <imc> 
es el índice de masa corporal calculado redondeado con dos decimales.  """


print('PROGRAMA PARA \nDETERMINAR IMC \n')
peso=int(input('Ingresar peso en kilogramos: \n'))
estatura=float(input('Ingresar estatura en metros: \n'))
imc=(peso/estatura**2)
print('\n su indice de masa coporal IMC es:\n',imc)