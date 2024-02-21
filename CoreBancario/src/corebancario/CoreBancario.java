/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package corebancario;

/**
 *
 * @author gmili
 */
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

public class CoreBancario {
    private static Datos objDatos = new Datos();
    private static Cypher objCypher = new Cypher();
   

    public static void main(String[] args) {
        final int puerto = 4528; // Puerto en /el que escucha el servidor
        String trama = "1:b0/AZOnt1uU8H7mWMxBzm2dgA==:250:5Mhs//9neLU86UypRmAk+Zml+2zl+X94rPsYjkNJyY0=:24589358";
        String resultado = procesarTrama(trama);
        
        System.out.println(resultado);
        
        
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
    
    public static String procesarTrama(String trama) {
            String[] partes = trama.split(":");
            String respuesta = null;
            String tipoMov = partes[0];
            /*String nroCuenta = objCypher.desencriptar(partes[1]);*/
            int monto = Integer.parseInt(partes[2]);
            /*String nroTarjeta = objCypher.desencriptar(partes[3]);*/
            if (tipoMov.equals("1")) {
                respuesta = retiro("85485536", monto, "15875323975289", partes[4]);
            } else if (tipoMov.equals("2")) {
                respuesta = consulta("85485536");
            }
            return respuesta;
        }

        private static String consulta(String nroCuenta) {
            String respuesta = null;
            String saldo = objDatos.consultarSaldo(nroCuenta);
            if (saldo != null && saldo.matches("\\d+(\\.\\d{1,2})?")) {
                respuesta = String.format("OK%019.2f", Double.parseDouble(saldo));
            } else {
                respuesta = "ERROR";
            }
           return respuesta;
        }

        private static String retiro(String nroCuenta, int montoRetiro, String nroTarjeta, String codAut) {
            String respuesta = null;
            double saldo = 0;
            System.out.println(objDatos.consultarSaldo(nroCuenta));
            saldo = Double.valueOf(objDatos.consultarSaldo(nroCuenta));
            if (saldo >= montoRetiro) {
                respuesta = "OK";
                saldo -= montoRetiro;
                objDatos.registrarRetiro(nroCuenta, Integer.toString(montoRetiro), nroTarjeta, codAut);
                objDatos.actualizarSaldo(nroCuenta, saldo);
                return respuesta;
            } else if (montoRetiro > saldo) {
                respuesta = "INSUF";
                return respuesta;
            } else {
                respuesta = "ERROR";
                return respuesta;
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

                // Procesar la trama
                String resultado = procesarTrama(trama);

                // Enviar respuesta al cliente
                salida.println(resultado);

                clienteSocket.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

        public String procesarTrama(String trama) {
            String[] partes = trama.split(":");
            String respuesta = null;
            String tipoMov = partes[0];
            String nroCuenta = objCypher.desencriptar(partes[1]);
            int monto = Integer.parseInt(partes[2]);
            String nroTarjeta = objCypher.desencriptar(partes[3]);
            if (tipoMov.equals("1")) {
                respuesta = retiro(nroCuenta, monto, nroTarjeta, partes[4]);
            } else if (tipoMov.equals("2")) {
                respuesta = consulta(nroCuenta);
            }
            return respuesta;
        }

        private String consulta(String nroCuenta) {
            String respuesta = null;
            String saldo = objDatos.consultarSaldo(nroCuenta);
            if (saldo != null && saldo.matches("\\d+(\\.\\d{1,2})?")) {
                respuesta = String.format("OK%019.2f", Double.parseDouble(saldo));
            } else {
                respuesta = "ERROR";
            }
           return respuesta;
        }

        private String retiro(String nroCuenta, int montoRetiro, String nroTarjeta, String codAut) {
            String respuesta = null;
            double saldo = 0;
            saldo = Integer.valueOf(objDatos.consultarSaldo(nroCuenta));
            if (saldo >= montoRetiro) {
                respuesta = "OK";
                saldo -= montoRetiro;
                objDatos.registrarRetiro(nroCuenta, Integer.toString(montoRetiro), nroTarjeta, codAut);
                objDatos.actualizarSaldo(nroCuenta, saldo);
                return respuesta;
            } else if (montoRetiro > saldo) {
                respuesta = "INSUF";
                return respuesta;
            } else {
                respuesta = "ERROR";
                return respuesta;
            }
        }
    }
}

