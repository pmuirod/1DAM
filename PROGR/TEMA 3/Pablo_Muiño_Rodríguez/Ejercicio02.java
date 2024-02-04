/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ejercicio02;

/**
 *
 * @author Pablo Muiño Rodríguez
 */
import java.util.Scanner;

//Para realizar este ejercicio primero pido los datos al usuario y los almaceno en la matriz por filas. A la vez, voy
//sumando los valores de la fila y saber cuanto suma esa fila. La primera fila la guardo en una variable aparte para comparar su suma
//con la del resto y saber si son iguales. Así mismo, lo hago con las columnas en un bucle aparte. Si en alguna comparación las sumas
//no son iguales una variable booleana pasa a ser verdadera cuando estaba inicializada a falso. Por último, apoyandonos en esta variable escribimos
//si es un cuadrado mágico o no.
public class Ejercicio02 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        //Se definen las variables que se van a utilizar en el ejercicio
        int m1[][]= new int[4][4];
        int muiñoNum;
        int muiñoSumaFilas;
        int muiñoSumaColumnas;
        int muiñoApoyo = 0;
        boolean muiñoFallo = false;
        
        //Se crea un objeto Scanner para recoger lo escrito por teclado
        Scanner sc = new Scanner(System.in);
        
        //Se realizan las condiciones y/bucles
        for (int i = 0; i < m1.length; i++) {
            muiñoSumaFilas = 0;
            System.out.println("Escriba los valores de la "+(i+1)+" fila:");
            for (int j = 0; j < m1[0].length; j++) {
                muiñoNum = sc.nextInt();
                muiñoSumaFilas += muiñoNum;
                m1[i][j] = muiñoNum;
            }
            if (i==0) {
                muiñoApoyo = muiñoSumaFilas;
            } else {
                if (muiñoApoyo!=muiñoSumaFilas) {
                    muiñoFallo = true;
                }
            }
        }
        muiñoApoyo = 0;
        
        for (int j = 0; j < m1[0].length; j++) {
            muiñoSumaColumnas = 0;
            for (int i = 0; i < m1.length; i++) {
                muiñoSumaColumnas += m1[j][i];
            }
            if (j==0) {
                muiñoApoyo = muiñoSumaColumnas;
            } else {
                if (muiñoApoyo!=muiñoSumaColumnas) {
                    muiñoFallo = true;
                }
            }
        }
        
        if (muiñoFallo == true) {
            System.out.println("La matriz no corresponde con un cuadrado mágico");
        } else {
            System.out.println("La matriz corresponde con un cuadrado mágico");
        }
    }
    
}
