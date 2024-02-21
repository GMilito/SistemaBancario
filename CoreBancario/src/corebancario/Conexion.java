package corebancario;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

import java.sql.Connection;
import java.sql.DriverManager;
/**
 *
 * @author gmili
 */
public class Conexion {
    Connection con = null;
    
    public Connection Conectarse(){
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String cadenaConexion = "jdbc:sqlserver://DESKTOP-BC9PPIJ\\PRINCIPAL:1433;databaseName=DBCore;user=sa;password=1598753;";
            con = DriverManager.getConnection(cadenaConexion);
            System.out.println("Conexion exitosa");
        } catch (Exception error) {
            System.out.println("Error con la conexion" + error.getMessage());
        }
        return con;
    }
}
