import java.util.*;


public class Puzzle8 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String objetivo = "12345678_";
        Nodo raiz = new Nodo("12578_346");
        ArbolBusqueda arbolBusqueda = new ArbolBusqueda(raiz, objetivo);
     
        int opcion = 0;
        
            System.out.println("Elige una opción:");
            System.out.println("1. Búsqueda por anchura");
            System.out.println("2. Búsqueda por profundidad");
            System.out.println("3. Búsqueda con heurística 1");
            System.out.println("4. Búsqueda con heurística 2");
            System.out.println("5. Búsqueda con heurística 3");
            System.out.println("6. Salir");
            opcion = scanner.nextInt();

            switch (opcion) {
                case 1:
                    arbolBusqueda.busquedaPorAnchura();
                    break;
                case 2:
                	arbolBusqueda.busquedaPorProfundidad();
                    break;
                case 3:
                	arbolBusqueda.busquedaHeuristica(arbolBusqueda.new Heuristica1());
                    break;
                case 4:
                    arbolBusqueda.busquedaHeuristica(arbolBusqueda.new Heuristica2());
                    break;
                case 5:            
                    arbolBusqueda.busquedaHeuristica(arbolBusqueda.new Heuristica3());
                    break;
                case 6:
                    System.out.println("Programa Cerrado");
                    break;
                default:
                    System.out.println("Opción inválida");
                    break;
            }

         
    }
}
    