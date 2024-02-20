import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

public class Core {
    private static Datos objDatos = new Datos();
    private static Cypher objCypher = new Cypher();
    private static ManejadorCliente prueba = new ManejadorCliente(null);
    public static void main(String[] args) {
        final int puerto = 7000; // Puerto en el que escucha el servidor
        
        try { 
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");     
               System.out.println("Driver funciona correctamente."); 
            } catch (ClassNotFoundException e) {
               System.out.println("Error: " + e.getMessage()); 
        }

        try {
            ServerSocket servidorSocket = new ServerSocket(puerto);
            System.out.println("Servidor en línea, esperando conexiones...");
            
            while (true) {
                Socket clienteSocket = servidorSocket.accept(); // Esperar a que un cliente se conecte
                System.out.println("Cliente conectado desde " + clienteSocket.getInetAddress());
                
                // Procesar la conexión en un hilo separado
                Thread hilo = new Thread(new ManejadorCliente(clienteSocket));
                hilo.start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        

    }

    private static class ManejadorCliente implements Runnable {
        private Socket clienteSocket;
        
        public ManejadorCliente(Socket clienteSocket) {
            this.clienteSocket = clienteSocket;
        }
        
        @Override
        public void run() {
            try {
                BufferedReader entrada = new BufferedReader(new InputStreamReader(clienteSocket.getInputStream()));
                PrintWriter salida = new PrintWriter(clienteSocket.getOutputStream(), true);
                
                // Leer trama enviada por el cliente
                String trama = entrada.readLine();
                String desencriptado = objCypher.desencriptar(trama);
                System.out.println("Trama encriptada recibida: " + trama);
                System.out.println("Trama desencriptada recibida: " + desencriptado);
                // Procesar la trama
                String resultado = procesarTrama(desencriptado);

                String respuesta = objCypher.encriptar(resultado);
                System.out.println("Trama desencriptada: " + resultado);
                System.out.println("Trama encriptada enviada: " + respuesta);
                // Enviar respuesta al cliente
                salida.println(respuesta);
                
                clienteSocket.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        
        public String procesarTrama(String trama) {
            String[] partes = trama.split(":");
            String respuesta = null;
            if(partes[0].equals("1")){
               respuesta = retiro(partes[1],Integer.valueOf(partes[2]),partes[3],partes[4]);
            }
            else if(partes[0].equals("2"))
            {
                respuesta = consulta(partes[1]);
            }
            return respuesta; 
        }

        private String consulta(String nroCuenta){
            String respuesta = null;
            respuesta = objDatos.consultarSaldo(nroCuenta);
            return respuesta;
        }

        private String retiro(String nroCuenta, int montoRetiro, String nroTarjeta, String codAut){
            String respuesta = null;
            int saldo = 0;
            saldo = Integer.valueOf(objDatos.consultarSaldo(nroCuenta));
            if (saldo>=montoRetiro){
                respuesta="OK";
                saldo -= montoRetiro;
                objDatos.registrarRetiro(nroCuenta, Integer.toString(montoRetiro), nroTarjeta, codAut);
                objDatos.actualizarSaldo(nroCuenta, Integer.toString(saldo));
                return respuesta;
            } else if (montoRetiro>saldo){
                respuesta = "INSUF";
                return respuesta;
            } else {
                respuesta = "ERROR";
                return respuesta;
            }
        }
    }
}
