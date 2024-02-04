/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ejercicio1relaciond;

/**
 *
 * @author Pablo Muiño Rodríguez
 */

//Se desean guardar y representar las notas de 5 alumnos en 4 asignaturas (números aleatorios con decimales entre 0 y 10) en una matriz. 
//Además, tanto para cada asignatura como para cada alumno, se precisa obtener y almacenar la nota máxima, mínima y la media aritmética.
public class Ejercicio1RelacionD {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        //Se definen las variables y/o arrays que se van a utilizar en el ejercicio
        double m1[][]= new double[7][8];
        double max = 0.0;
        double min = 10.0;
        double suma = 0.0;
        
        //Se realizan las condiciones y/o los bucles
        for (int i = 0; i < m1.length-3; i++) {
            for (int j = 0; j < m1[0].length-3; j++) {
                m1[i][j] = Math.random()*11;
                suma = suma+m1[i][j];
                if (m1[i][j]>max) {
                    m1[i][m1[0].length-2] = m1[i][j];
                    max = m1[i][j];
                }
                if (m1[i][j]<min) {
                    m1[i][m1[0].length-1] = m1[i][j];
                    min = m1[i][j];
                }
            }
            m1[i][m1[0].length] = suma/(m1[0].length-3);
        }
        max = 0.0;
        min = 10.0;
        suma = 0.0;
        
        for (int j = 0; j < m1[0].length-3; j++) {
            for (int i = 0; i < m1.length-3; i++) {
                suma = suma+m1[j][i];
                if (m1[j][i]>max) {
                    m1[j][m1.length-2] = m1[j][i];
                    max = m1[j][i];
                }
                if (m1[j][i]<min) {
                    m1[j][m1.length-1] = m1[j][i];
                    min = m1[j][i];
                }
            }
            m1[j][m1.length] = suma/(m1.length-3);
        }
        
        for (int i = 0; i < m1.length; i++) {
            for (int j = 0; j < m1[0].length; j++) {
                System.out.printf("%.2f",m1[i][j]);
                System.out.print("\t");
            }
            System.out.println("");
        }
        
    }//main
}//class
