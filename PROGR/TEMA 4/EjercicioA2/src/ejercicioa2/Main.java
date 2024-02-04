/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ejercicioa2;

/**
 *
 * @author Pablo Muiño Rodríguez
 */
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        //Creamos dos Personas
        Persona p1 = new Persona();
        Persona p2 = new Persona();
        
        //Creamos una clase Scanner para recoger lo esccrito por teclado por el usuario
        Scanner sc1 = new Scanner(System.in);
        Scanner sc2 = new Scanner(System.in);
        
        //Les damos valores
        System.out.println("====Persona 1====");
        System.out.println("Escriba su nombre");
        p1.nombre = sc1.nextLine();
        System.out.println("Escriba sus apellidos");
        p1.apellidos = sc1.nextLine();
        System.out.println("Escriba su DNI");
        p1.dni = sc1.nextLine();
        System.out.println("Escriba su edad");
        p1.edad = sc1.nextInt();
        
        System.out.println("");
        
        System.out.println("====Persona 2====");
        System.out.println("Escriba su nombre");
        p2.nombre = sc2.nextLine();
        System.out.println("Escriba sus apellidos");
        p2.apellidos = sc2.nextLine();
        System.out.println("Escriba su DNI");
        p2.dni = sc2.nextLine();
        System.out.println("Escriba su edad");
        p2.edad = sc2.nextInt();
        
        //Se escribe los mensajes
        System.out.print(p1.nombre+" "+p1.apellidos+" con DNI "+p1.dni);
        if (p1.edad>=18) {
            System.out.println(" es mayor de edad");
        }else{
            System.out.println(" no es mayor de edad");
        }
        System.out.print(p2.nombre+" "+p2.apellidos+" con DNI "+p2.dni);
        if (p2.edad>=18) {
            System.out.println(" es mayor de edad");
        }else{
            System.out.println(" no es mayor de edad");
        }
    }
    
}
