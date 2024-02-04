# Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.

print("Escriba dos valores (A y B)")
A = input()
B = input()

A, B = B, A

print("Los valores ahora son: A ->",A", B ->",B)