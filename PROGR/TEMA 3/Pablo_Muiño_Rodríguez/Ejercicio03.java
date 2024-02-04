/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ejercicio03;

/**
 *
 * @author Pablo Muiño Rdoríguez
 */

//Para realizar este ejercicio primero relleno el array Numero con números aleatorios. Una vez tengo este array relleno
//el array Cuadrado multiplicando los valores del array Numero por sí mismos. Hago lo mismo con el array Raiz pero usando la función
//Math.sqrt que permite hacer la raiz cuadrada de los valores de Numero. Por último, para escribir los valores en columnas hago un for donde
//la primera columna pertenece a el array Numero, la segunda a Cuadrado y la tercera Raiz; también, añado las sumas de las columnas en una última fila.
public class Ejercicio03 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        //Se definen las variables que se van a utilizar en el ejercicio
        int muiñoNumero[]= new int[10];
        int muiñoCuadrado[]= new int[10];
        int muiñoRaiz[]= new int[10];
        int muiñoSumaNumero = 0;
        int muiñoSumaCuadrado = 0;
        int muiñoSumaRaiz = 0;
        
        //Se realizan las condiciones y/bucles
        for (int i = 0; i < muiñoNumero.length; i++) {
            muiñoNumero[i]= (int)(Math.random()*101);
            muiñoSumaNumero += muiñoNumero[i];
        }//for numero
        for (int i = 0; i < muiñoCuadrado.length; i++) {
            muiñoCuadrado[i]= muiñoNumero[i]*muiñoNumero[i];
            muiñoSumaCuadrado += muiñoCuadrado[i];
        }//for cuadrado
        for (int i = 0; i < muiñoRaiz.length; i++) {
            muiñoRaiz[i]= (int)(Math.sqrt(muiñoNumero[i]));
            muiñoSumaRaiz += muiñoRaiz[i];
        }//for raiz
        for (int i = 0; i < 11; i++) {
            if (i==10) {
                for (int j = 0; j < 3; j++) {
                    if (j==0) {
                        System.out.print("Suma:  "+muiñoSumaNumero+"   ");
                    }//if
                    if (j==1) {
                        System.out.print("   "+muiñoSumaCuadrado+"   ");
                    }//if
                    if (j==2) {
                        System.out.print("   "+muiñoSumaRaiz+"   ");
                    }//if
                }//for
            }else{
                for (int j = 0; j < 3; j++) {
                    if (j==0) {
                        System.out.print("       "+muiñoNumero[i]+"   ");
                    }//if
                    if (j==1) {
                        System.out.print(muiñoCuadrado[i]+"       ");
                    }//if
                    if (j==2) {
                        System.out.print(muiñoRaiz[i]+"       ");
                    }//if
                }//for interior
            }
            System.out.println("");
        }//for exterior
        
    }//main
    
}//class
