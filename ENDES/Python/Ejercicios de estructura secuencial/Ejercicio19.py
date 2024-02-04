# Escribir un algoritmo para calcular la nota final de un estudiante, considerando que: por cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en blanco 0.

print("Escriba las respuestas de su examen en el siguiente orden: respuestas correctas, respuestas incorrectas y respuestas en blanco")
correcta = input()
incorrecta = input()
blanco = input()

nota = (correcta*5)-(incorrecta*-1)

print("Tiene un",nota" sobre 100")