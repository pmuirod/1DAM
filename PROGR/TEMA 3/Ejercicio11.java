/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ejercicio11;

/**
 *
 * @author Pablo Mui√±o Rodr√≠guez
 */
import java.util.Scanner;

public class Ejercicio11 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        //Se definen las variables y/o arrays que se van a utilizar
        
        //La profundidad ser· 3 ya que hay 3 meses
        //Las filas ser·n 4 ya que hay 4 comidas
        //Las columnas ser·n 3 ya que hay 3 establecimientos
        double m1[][][]= new double[3][4][3];
        int respuesta;
        double suma1 = 0;
        double suma2 = 0;
        double suma3 = 0;
        double suma4 = 0;
        
        //Se crea un objeto Scanner para recoger lo escrito por teclado
        Scanner sc = new Scanner(System.in);
        
        //Se realizan las condiciones y/o los bucles
        
        //Relleno la tabla de 3 dimensiones con valores aleatorios double entre 5000 y 9000
        for (int i = 0; i < m1.length; i++) {
            for (int j = 0; j < m1[0].length; j++) {
                for (int k = 0; k < m1[0][0].length; k++) {
                    m1[i][j][k] = (Math.random()*9000)+1;
                }//for k
            }//for j
        }//for i
        
        do {
            System.out.println("\033[34m=========================MEN⁄=========================");
            System.out.println("\033[35m1. \033[30mListado de todas las ventas por establecimiento en cada mes");
            System.out.println("\033[35m2. \033[30mMostrar el total de ventas de cada establecimiento en cada mes");
            System.out.println("\033[35m3. \033[30mMostrar la media de cada establecimiento en cada mes");
            System.out.println("\033[35m4. \033[30mMostrar el total de ventas de la empresa en cada mes");
            System.out.println("\033[35m5. \033[30mMostrar las ventas del mes de diciembre");
            System.out.println("\033[35m6. \033[30mMostrar el total de ventas de los productos en cada mes");
            System.out.println("\033[35m7. \033[30mSalir");
            respuesta = sc.nextInt();
            System.out.println("");
            
            switch (respuesta) {        //Dependiendo de la respuesta se har· una cosa u otra
                case 1:
                    for (int i = 0; i < m1.length; i++) {
                        if (i==0) {
                            System.out.println("Mes de \033[34mOctubre\033[30m:");
                        }
                        if (i==1) {
                            System.out.println("Mes de \033[34mNoviembre\033[30m:");
                        }
                        if (i==2) {
                            System.out.println("Mes de \033[34mDiciembre\033[30m:");
                        }
                        for (int j = 0; j < m1[0].length; j++) {
                            if (j==0) {
                                System.out.println("\t"+"- Arranque :");
                            }
                            if (j==1) {
                                System.out.println("\t"+"- Tortilla con patatas :");
                            }
                            if (j==2) {
                                System.out.println("\t"+"- Tortilla sin cebolla :");
                            }
                            if (j==3) {
                                System.out.println("\t"+"- Pescaito frito :");
                            }
                            for (int k = 0; k < m1[0][0].length; k++) {
                                if (k==0) {
                                    System.out.print("\t"+"\t"+"Establecimiento "+(k+1)+" = ");
                                    System.out.printf("%.2f",m1[i][j][k]);
                                    System.out.println("");
                                }
                                if (k==1) {
                                    System.out.print("\t"+"\t"+"Establecimiento "+(k+1)+" = ");
                                    System.out.printf("%.2f",m1[i][j][k]);
                                    System.out.println("");
                                }
                                if (k==2) {
                                    System.out.print("\t"+"\t"+"Establecimiento "+(k+1)+" = ");
                                    System.out.printf("%.2f",m1[i][j][k]);
                                    System.out.println("");
                                }
                            }//for k
                        }//for j
                    }//for i
                    System.out.println("");
                    
                    break;
                case 2:
                    for (int i = 0; i < m1.length; i++) {
                        if (i==0) {
                            System.out.println("Mes de \033[34mOctubre\033[30m:");
                        }
                        if (i==1) {
                            System.out.println("Mes de \033[34mNoviembre\033[30m:");
                        }
                        if (i==2) {
                            System.out.println("Mes de \033[34mDiciembre\033[30m:");
                        }
                        for (int j = 0; j < m1[0].length; j++) {
                            for (int k = 0; k < m1[0][0].length; k++) {
                                if (k==0) {
                                    suma1 += m1[i][j][k];           //Dependiendo del establecimiento se guardar· 
                                }                                   //la suma de la venta de los productos
                                if (k==1) {                         //en ese establecimiento durante los 3 meses
                                    suma2 += m1[i][j][k];
                                }
                                if (k==2) {
                                    suma3 += m1[i][j][k];
                                }
                            }//for k
                        }//for j
                        
                        System.out.print("\t"+"- Establecimiento 1 = ");
                        System.out.printf("%.2f",suma1);
                        System.out.println("");
                        System.out.print("\t"+"- Establecimiento 2 = ");
                        System.out.printf("%.2f",suma2);
                        System.out.println("");
                        System.out.print("\t"+"- Establecimiento 3 = ");
                        System.out.printf("%.2f",suma3);
                        System.out.println("");
                    }//for i
                    System.out.println("");
                    suma1 = 0;
                    suma2 = 0;      //Se reinician las variables para que se de lugar a ning˙n error
                    suma3 = 0;
                    
                    break;
                case 3:
                    for (int i = 0; i < m1.length; i++) {
                        if (i==0) {
                            System.out.println("Mes de \033[34mOctubre\033[30m:");
                        }
                        if (i==1) {
                            System.out.println("Mes de \033[34mNoviembre\033[30m:");
                        }
                        if (i==2) {
                            System.out.println("Mes de \033[34mDiciembre\033[30m:");
                        }
                        for (int j = 0; j < m1[0].length; j++) {
                            for (int k = 0; k < m1[0][0].length; k++) {
                                if (k==0) {
                                    suma1 += m1[i][j][k];           
                                }
                                if (k==1) {
                                    suma2 += m1[i][j][k];
                                }
                                if (k==2) {
                                    suma3 += m1[i][j][k];
                                }
                            }//for k
                        }//for j
                        
                        suma1 = suma1 / m1[0].length;          //Las sumas de las ventas de cada establecimiento
                        suma2 = suma2 / m1[0].length;          //se dividen por la cantidad de comida que hay para hacer la media
                        suma3 = suma3 / m1[0].length;
                        
                        System.out.print("\t"+"- Establecimiento 1 = ");
                        System.out.printf("%.2f",suma1);
                        System.out.println("");
                        System.out.print("\t"+"- Establecimiento 2 = ");
                        System.out.printf("%.2f",suma2);
                        System.out.println("");
                        System.out.print("\t"+"- Establecimiento 3 = ");
                        System.out.printf("%.2f",suma3);
                        System.out.println("");
                    }//for i
                    System.out.println("");
                    suma1 = 0;
                    suma2 = 0;
                    suma3 = 0;
                    
                    break;
                case 4:
                    for (int i = 0; i < m1.length; i++) {
                        if (i==0) {
                            System.out.print("Mes de \033[34mOctubre \033[30m= ");
                        }
                        if (i==1) {
                            System.out.print("Mes de \033[34mNoviembre \033[30m= ");
                        }
                        if (i==2) {
                            System.out.print("Mes de \033[34mDiciembre \033[30m= ");
                        }
                        for (int j = 0; j < m1[0].length; j++) {
                            for (int k = 0; k < m1[0][0].length; k++) {
                                if (i==0) {
                                    suma1 += m1[i][j][k];           //Dependiendo del mes se guardar·
                                }                                   //la suma total de ventas de comida
                                if (i==1) {                         //de cada mes
                                    suma2 += m1[i][j][k];
                                }
                                if (i==2) {
                                    suma3 += m1[i][j][k];
                                }
                            }//for k
                        }//for j
                        
                        if (i==0) {
                            System.out.printf("%.2f",suma1);
                            System.out.println("");
                        }
                        if (i==1) {
                            System.out.printf("%.2f",suma2);
                            System.out.println("");
                        }
                        if (i==2) {
                            System.out.printf("%.2f",suma3);
                            System.out.println("");
                        }
                    }//for i
                    
                    suma1 = 0;
                    suma2 = 0;
                    suma3 = 0;
                    
                    System.out.println("");
                    break;
                case 5:
                    for (int i = 0; i < m1.length; i++) {
                        if (i==2) {         //If para asegurarnos de que solo queremos el mes de Diciembre
                            System.out.println("Mes de \033[34mDiciembre\033[30m:");
                        }
                        for (int j = 0; j < m1[0].length; j++) {
                            if (i==2) {         //If para asegurarnos de que solo queremos el mes de Diciembre
                                if (j==0) {
                                    System.out.println("\t"+"- Arranque :");
                                }
                                if (j==1) {
                                    System.out.println("\t"+"- Tortilla con patatas :");
                                }
                                if (j==2) {
                                    System.out.println("\t"+"- Tortilla sin cebolla :");
                                }
                                if (j==3) {
                                    System.out.println("\t"+"- Pescaito frito :");
                                }
                            }
                            for (int k = 0; k < m1[0][0].length; k++) {
                                if (i==2) {         //If para asegurarnos de que solo queremos el mes de Diciembre
                                    if (k==0) {
                                        System.out.print("\t"+"\t"+"Establecimiento "+(k+1)+" = ");
                                        System.out.printf("%.2f",m1[i][j][k]);
                                        System.out.println("");
                                    }
                                    if (k==1) {
                                        System.out.print("\t"+"\t"+"Establecimiento "+(k+1)+" = ");
                                        System.out.printf("%.2f",m1[i][j][k]);
                                        System.out.println("");
                                    }
                                    if (k==2) {
                                        System.out.print("\t"+"\t"+"Establecimiento "+(k+1)+" = ");
                                        System.out.printf("%.2f",m1[i][j][k]);
                                        System.out.println("");
                                    }
                                }
                            }//for k
                        }//for j
                    }//for i
                    System.out.println("");
                    
                    break;
                case 6:
                    for (int i = 0; i < m1.length; i++) {
                        if (i==0) {
                            System.out.println("Mes de \033[34mOctubre\033[30m:");
                        }
                        if (i==1) {
                            System.out.println("Mes de \033[34mNoviembre\033[30m:");
                        }
                        if (i==2) {
                            System.out.println("Mes de \033[34mDiciembre\033[30m:");
                        }
                        for (int j = 0; j < m1[0].length; j++) {
                            for (int k = 0; k < m1[0][0].length; k++) {
                                if (j==0) {
                                    suma1 += m1[i][j][k];
                                }                                   //Dependiendo de la comida se asignar·
                                if (j==1) {                         //a la variable la suma de la cantidad vendida
                                    suma2 += m1[i][j][k];           //de esa comida entre los tres establecimientos
                                }
                                if (j==2) {
                                    suma3 += m1[i][j][k];
                                }
                                if (j==3) {
                                    suma4 += m1[i][j][k];
                                }
                            }//for k
                        }//for j
                        
                        System.out.print("\t"+"- Arranque = ");
                        System.out.printf("%.2f",suma1);
                        System.out.println("");
                        System.out.print("\t"+"- Tortilla con cebolla = ");
                        System.out.printf("%.2f",suma2);
                        System.out.println("");
                        System.out.print("\t"+"- Tortilla sin cebolla = ");
                        System.out.printf("%.2f",suma3);
                        System.out.println("");
                        System.out.print("\t"+"- Pescaito frito = ");
                        System.out.printf("%.2f",suma4);
                        System.out.println("");
                    }//for i
                    System.out.println("");
                    suma1 = 0;
                    suma2 = 0;
                    suma3 = 0;
                    suma4 = 0;
                    
                    break;
            }//switch respuesta
        } while (respuesta!=7);
        System.out.println("......¬°¬°Hasta luego!!......");
    }
    
}
