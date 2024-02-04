/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ejercicioa1;

/**
 *
 * @author Pablo Muiño Rodríguez
 */
public class Main {

    public static void main(String[] args) {
        //Creamos tres Puntos
        Punto p1 = new Punto();
        Punto p2 = new Punto();
        Punto p3 = new Punto();
        
        //Les damos valores
        p1.x=5; p1.y=0;
        p2.x=10; p2.y=10;
        p3.x=-3; p3.y=7;
        
        //Usamos los métodos
        System.out.println("El primero punto tiene las coordenadas: "+p1.x+":"+p1.y);
        System.out.println("El primero punto tiene las coordenadas: "+p2.x+":"+p2.y);
        System.out.println("El primero punto tiene las coordenadas: "+p3.x+":"+p3.y);
    }//main
    
}//Main
