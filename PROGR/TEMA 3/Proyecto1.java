/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package proyecto1;

/**
 *
 * @author Gonzalo Carretero Peñalosa y Pablo Muiño Rodríguez
 */
import java.util.Scanner;

public class Proyecto1 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        //Se definen las variables y/o arrays que se van a utilizar
        int nivel = 0;
        boolean fallo = false;
        String respuesta,resultado;
        int s1,s2,p1,p2,n,p,primo,m,s;
        int sumatorio = 0,productorio = 1,factorial = 1,factorial1 = 1,factorial2 = 1,division = 0;
        
        //Se crea un objeto Scanner para recoger lo escrito por teclado
        Scanner sc = new Scanner(System.in);
        
        //Se realizan las condiciones y/o los bucles
        do {        //Mientras que la variable booleana fallo sea falsa (no se ha fallado en ningún nivel) y el nivel no sobrepase el sexto (el último nivel) el bucle seguirá iterando.
            switch (nivel) {        //  Switch para cada uno de los niveles
                case 0:
                    
                    System.out.println("\033[35m=== STAR WARS CÓDIGOS SECRETOS ===\n" +
                    "\033[30mHace mucho tiempo, en una galaxia muy, muy lejana...\033[34m La Princesa Leia\033[30m, \033[34mLuke\n" +
                    "\033[34mSkywalker\033[30m, \033[34mHan Solo\033[30m, \033[34mChewbacca\033[30m, \033[34mC3PO \033[30my \033[34mR2D2 \033[30mviajan en una nave imperial robada\n" +
                    "en una misión secreta para infiltrarse en otra \033[31mestrella de la muerte \033[30mque el imperio\n" +
                    "está construyendo para destruirla. (Presiona Intro para continuar)");
                    respuesta = sc.nextLine();
                    
                    if (respuesta.equals("")) {     //Condición para subir de nivel y pasar al siguiente caso del switch
                        nivel ++;
                    }//if
                    
                    break;
                case 1:
                    
                    s1 = (int)(Math.random()*10)+1;     //Se genera un número aleatorio entre 1 y 10
                    do {        //Se genera un número aleatorio entre 20 y 30 (el bucle se repetirá en caso de que s2 no esté en ese rango)
                        s2 = (int)(Math.random()*30)+1;
                    } while (s2<20 | s2>30);
                    
                    for (int i = s1; i <= s2; i++) {        //Se suman los valores comprendidos entre s1 y s2 ambos inclusive
                        sumatorio += i;
                    }//for
                    
                    resultado = String.valueOf(sumatorio);      //El resultado numérico se pasa a un string
                    System.out.println("Resultado del  nivel: "+resultado);     //Se imprime el resultado para que el programador no tenga que hacer los cálculos
                    
                    System.out.println("Los problemas empiezan cuando deben realizar un salto hiperespacial hasta al\n" +
                    "sistema \033[35m"+s1+" \033[30men el sector \033[35m"+s2+"\033[30m, pero el sistema de navegación está estropeado y el\n" +
                    "computador tiene problemas para calcular parte de las coordenadas de salto.\n" +
                    "\033[34mChewbacca\033[30m, piloto experto, se da cuenta que falta el cuarto número de la serie.\n" +
                    "Recuerda de sus tiempos en la academia de pilotos que para calcularlo hay que\n" +
                    "calcular \033[35mel sumatorio entre el nº del sistema y el nº del sector (ambos inclusive)\033[30m.\n" +
                    "¿Qué debe introducir?");
                    respuesta = sc.nextLine();
                    
                    if (respuesta.equals(resultado)) {      //Condición para pasar de nivel
                        nivel++;
                    }else{      //En caso de no acertar la respuesta la variable fallo pasa a ser verdadera, causando que se salga del bucle
                        fallo = true;
                    }//ifelse
                    
                    System.out.println("");
                    
                    break;
                case 2:
                    
                    p1 = (int)(Math.random()*7)+1;      //Se genera un número aleatorio entre 1 y 7
                    do {
                        p2 = (int)(Math.random()*12)+1;     //Se genera un número aleatorio entre 8 y 12 (el bucle se repetirá en caso de que p2 no esté en ese rango)
                    } while (p2<8 | p2>12);
                    
                    for (int i = p1; i <= p2; i++) {        //Se multiplican los valores comprendidos entre p1 y p2 ambos inclusive
                        productorio = productorio*i;
                    }//for
                    
                    resultado = String.valueOf(productorio);        //El resultado numérico se pasa a un string
                    System.out.println("Resultado del nivel: "+resultado);      //Se imprime el resultado para que el programador no tenga que hacer los cálculos
                    
                    System.out.println("Gracias a \033[34mChewbacca \033[30mconsiguen llegar al sistema correcto y ven a lo lejos la \033[31mestrella\n" +
                    "\033[31mde la muerte\033[30m. Como van en una nave imperial robada se aproximan lentamente con\n" +
                    "la intención de pasar desapercibidos. De repente suena el comunicador. \033[31m'Aquí\n" +
                    "\033[31magente de espaciopuerto \033[35m"+p1+" \033[31mcontactando con nave imperial \033[35m"+p2+"\033[31m. No están destinados\n" +
                    "\033[31men este sector. ¿Qué hacen aquí?'\033[30m. \033[34mHan Solo \033[30mcoge el comunicador e improvisa.\n" +
                    "\033[34m'Eh... tenemos un fallo en el... eh... condensador de fluzo... Solicitamos permiso\n" +
                    "\033[34mpara atracar y reparar la nave'\033[30m. El agente, que no se anda con tonterías, responde\n" +
                    "\033[31m'Proporcione código de acceso o abriremos fuego'\033[30m. \033[34mHan Solo \033[30mojea rápidamente el\n" +
                    "manual del piloto que estaba en la guantera y da con la página correcta. El código\n" +
                    "es \033[35mel productorio entre el nº del agente y el nº de la nave (ambos inclusive)\033[30m.\n" +
                    "¿Cuál es el código?");
                    respuesta = sc.nextLine();
                    
                    if (respuesta.equals(resultado)) {      //Condición para pasar de nivel
                        nivel++;
                    }else{      //En caso de no acertar la respuesta la variable fallo pasa a ser verdadera, causando que se salga del bucle
                        fallo = true;
                    }//ifelse
                    
                    System.out.println("");
                    
                    break;
                case 3:
                    
                    do {
                        n = (int)(Math.random()*100)+1;     //Se genera un número aleatorio entre 50 y 100 (el bucle se repetirá en caso de que n no esté en ese rango)
                    } while (n<50 | n>100);
                    
                    division = n/10;        //Se divide n entre 10 (dará un resultado entero)
                    
                    for (int i = 1; i <= division; i++) {       //Se multiplican los valores comprendidos entre 1 y n ambos inclusive
                        factorial = factorial*i;
                    }//for
                    
                    resultado = String.valueOf(factorial);      //El resultado numérico se pasa a un string
                    System.out.println("Resultado del nivel: "+resultado);      //Se imprime el resultado para que el programador no tenga que hacer los cálculos
                    
                    System.out.println("\033[34mHan Solo \033[30mproporciona el código correcto. Atracan en la \033[31mestrella de la muerte\033[30m, se\n" +
                    "equipan con trajes de soldados imperiales que encuentran en la nave para pasar\n" +
                    "desapercibidos y bajan. Ahora deben averiguar en qué nivel de los \033[35m"+n+" \033[30mexistentes se\n" +
                    "encuentra el reactor principal. Se dirigen al primer panel computerizado que\n" +
                    "encuentran y la \033[34mPrincesa Leia \033[30mintenta acceder a los planos de la nave pero necesita\n" +
                    "introducir una clave de acceso. Entonces recuerda la información que le proporcionó\n" +
                    "\033[34mLando Calrissian 'La clave de acceso a los planos de la nave es el factorial de N/10\n" +
                    "\033[34m(redondeando N hacia abajo)'\033[30m, \033[35mdonde N es el nº de niveles'\033[30m.\n" +
                    "¿Cual es el nivel correcto?");
                    respuesta = sc.nextLine();
                    
                    if (respuesta.equals(resultado)) {      //Condición para pasar de nivel
                        nivel++;
                    }else{      //En caso de no acertar la respuesta la variable fallo pasa a ser verdadera, causando que se salga del bucle
                        fallo = true;
                    }//ifelse
                    
                    System.out.println("");
                    
                    break;
                case 4:
                    
                    do {
                        p = (int)(Math.random()*100)+1;     //Se genera un número aleatorio entre 10 y 100 (el bucle se repetirá en caso de que p no esté en ese rango)
                    } while (p<10 | p>100);
                    
                    for (int i = 1; i <= p; i++) {
                        if (p%i==0) {       //Si la división entre p e i (de 1 hasta p) no da 0 como resto no se sumará 1 a división
                            division +=1;
                        }//if
                    }//for
                    
                    if (division==2) {      //Se división es igual a 2, es decir, solo hay dos divisiones donde el resto da 0 (entre 1 y entre el número propio)
                        primo = 1;      //En este caso el número es primo
                    }else{
                        primo = 0;      //Si no se da el caso, es decir, hay más de 2 divisiones donde el resto da 0, el número no es primo
                    }//ifelse
                    
                    resultado = String.valueOf(primo);      //El resultado numérico se pasa a un string
                    System.out.println("Resultado del nivel: "+resultado);      //Se imprime el resultado para que el programador no tenga que hacer los cálculos
                    
                    System.out.println("Gracias a la inteligencia de \033[34mLeia \033[30mllegan al nivel correcto y encuentran la puerta\n" +
                    "acorazada que da al reactor principal. \033[34mR2D2 \033[30mse conecta al panel de acceso para\n" +
                    "intentar hackear el sistema y abrir la puerta. Para desencriptar la clave necesita\n" +
                    "verificar si el número \033[35m"+p+" \033[30mes primo o no. Si es primo introduce un \033[35m1\033[30m, si no lo es\n" +
                    "introduce un \033[35m0\033[30m.");
                    respuesta = sc.nextLine();
                    
                    if (respuesta.equals(resultado)) {      //Condición para pasar de nivel
                        nivel++;
                    }else{      //En caso de no acertar la respuesta la variable fallo pasa a ser verdadera, causando que se salga del bucle
                        fallo = true;
                    }//ifelse
                    
                    System.out.println("");
                    
                    break;
                case 5:
                    
                    do {
                        m = (int)(Math.random()*10)+1;      //Se genera un número aleatorio entre 5 y 10
                    } while (m<5 | m>10);
                    do {
                        s = (int)(Math.random()*10)+1;      //Se genera un número aleatorio entre 5 y 10
                    } while (s<5 | s>10);
                    
                    for (int i = 1; i <= m; i++) {
                        factorial1 = factorial1*i;      //Se multiplican los valores comprendidos entre 1 y m ambos inclusive
                    }//for
                    for (int i = 1; i <= s; i++) {
                        factorial2 = factorial2*i;      //Se multiplican los valores comprendidos entre 1 y s ambos inclusive
                    }//for
                    
                    factorial = factorial1 + factorial2;        //Se suman los factoriales
                    resultado = String.valueOf(factorial);      //El resultado numérico se pasa a un string
                    System.out.println("Resultado del nivel: "+resultado);      //Se imprime el resultado para que el programador no tenga que hacer los cálculos
                    
                    System.out.println("Consiguen entrar al reactor. Ya solo queda que \033[34mLuke Skywalker \033[30mcoloque la bomba,\n" +
                    "programe el temporizador y salir de allí­ corriendo. Necesita programarlo para que\n" +
                    "explote en exactamente \033[35m"+m+" \033[30mminutos y \033[35m"+s+" \033[30msegundos, el tiempo suficiente para escapar\n" +
                    "antes de que explote pero sin que el sistema de seguridad anti-explosivos detecte y\n" +
                    "desactive la bomba. Pero el temporizador utiliza un reloj Zordgiano un tanto\n" +
                    "peculiar. Para convertir los minutos y segundos al sistema Zordgiano \033[35mhay que sumar\n" +
                    "\033[35mel factorial de los minutos y el factorial de los segundos\033[30m. ¿Qué valor debe introducir?");
                    respuesta = sc.nextLine();
                    
                    if (respuesta.equals(resultado)) {      //Condición para pasar de nivel
                        nivel++;
                    }else{      //En caso de no acertar la respuesta la variable fallo pasa a ser verdadera, causando que se salga del bucle
                        fallo = true;
                    }//ifelse
                    
                    System.out.println("");
                    
                    break;
                case 6:
                    
                    System.out.println("\033[34mLuke Skywalker \033[30mintroduce el tiempo correcto, activa el temporizador y empiezan a\n" +
                    "sonar las alarmas. Salen de allí­ corriendo, no hay tiempo que perder. La nave se\n" +
                    "convierte en un hervidero de soldados de arriba a abajo y entre el caos que les rodea\n" +
                    "consiguen llegar a la nave y salir de allí­ a toda prisa. A medida que se alejan\n" +
                    "observan por la ventana la imagen de la colosal \033[31mestrella de la muerte \033[30mexplotando en\n" +
                    "el silencio del espacio, desapareciendo para siempre junto a los restos del \033[31mmalvado\n" +
                    "\033[31mimperio.\n" +
                    "\033[35m¡Has salvado la galaxia gracias a la Fuerza Jedi de las matemáticas! \033[30mEnhorabuena ;D");
                    nivel++;
                    
                    break;
                default:
                    
            }//switch
        } while (fallo==false & nivel<=6);
        
        System.out.println("");
        
        if (fallo == true) {        //Si la variable fallo es verdadera, es decir, se ha fallado en algún nivel, devuelve el siguiente mensaje
            System.out.println("Ese no era el código correcto... La misión ha sido un fracaso... :( :( :(\n" +
            "Todaví­a no eres un Maestro Jedi de las Matemáticas. ¡Vuelve a intentarlo!");
        }else{      //Si no se da el caso anterior, o sea, no se ha falldo devuelve el siguiente mensaje
            System.out.println("Gracias por jugar :D");
        }//ifelse
    }//main
    
}//class
