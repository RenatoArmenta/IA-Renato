import java.util.*;

/**
 * Clase que representa un árbol de búsqueda para el problema del 8-puzzle
 */
public class ArbolBusqueda {
    private Nodo raiz;
    private static String objetivo;
    private Set<String> visitados;

    public ArbolBusqueda(Nodo raiz, String objetivo) {
        this.raiz = raiz;
        this.objetivo = objetivo;
        this.visitados = new HashSet<>();
    }

    public void busquedaPorAnchura() {
        System.out.println("Búsqueda por Anchura:");
        Queue<Nodo> cola = new LinkedList<>();
        cola.offer(raiz);
        visitados.add(raiz.getEstado());
    
        while (!cola.isEmpty()) {
            Nodo actual = cola.poll();
            if (actual.getEstado().equals(objetivo)) {
                Solucion(actual); // Usar el método Solucion para imprimir los movimientos.
                return;
            }
            for (String sucesor : actual.generaHijos()) {
                Nodo nodoSucesor = new Nodo(sucesor);
                if (!visitados.contains(sucesor)) {
                    nodoSucesor.setPadre(actual);
                    cola.offer(nodoSucesor);
                    visitados.add(sucesor);
                }
            }
        }
        System.out.println("No se encontró solución.");
    }

    /**
     * Realiza la búsqueda por profundidad del estado objetivo
     */
    public void busquedaPorProfundidad() {
        System.out.println("\nBúsqueda por Profundidad:");
        Stack<Nodo> pila = new Stack<>();
        pila.push(raiz);
        visitados.add(raiz.getEstado());
        while (!pila.isEmpty()) {
            Nodo actual = pila.pop();
            if (actual.getEstado().equals(objetivo)) {
                Solucion(actual);
                return;
            }
            for (String sucesor : actual.generaHijos()) {
                Nodo nodoSucesor = new Nodo(sucesor);
                if (!visitados.contains(sucesor)) {
                    nodoSucesor.setPadre(actual);
                    pila.push(nodoSucesor);
                    visitados.add(sucesor);
                }
            }
        }
        System.out.println("No se encontró solución.");
    }

    public void Solucion(Nodo nodo) {
        System.out.println("Solución encontrada:");
        Stack<Nodo> pila = new Stack<>();
        while (nodo != null) {
            pila.push(nodo);
            nodo = nodo.getPadre();
        }
        int profundidad = 0;
        while (!pila.isEmpty()) {
            Nodo actual = pila.pop();
            System.out.println("Movimiento #" + profundidad + ":");
            System.out.println(actual);
            profundidad++;
        }
    }


    }