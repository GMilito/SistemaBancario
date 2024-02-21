/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package corebancario;

/**
 *
 * @author gmili
 */
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class Datos {
    Conexion conexion = new Conexion();
    String stringConexion = "jdbc:sqlserver://DESKTOP-BC9PPIJ\\PRINCIPAL:1433;databaseName=BDCore;user=sa;password=1598753";
    


    public String consultarSaldo(String nroCuenta) {
    String respuesta = null;
    try (Connection connection = DriverManager.getConnection(stringConexion);
         PreparedStatement statement = connection.prepareStatement("SELECT saldoCuenta FROM Cuenta WHERE numeroCuenta = ?");
    ) {
        statement.setString(1, nroCuenta);
        try (ResultSet resultado = statement.executeQuery()) {
            if (resultado.next()) { // Verificar si hay resultados
                respuesta = resultado.getString("saldoCuenta");
            } else {
                System.out.println("No se encontró saldo para la cuenta " + nroCuenta);
            }
        }
    } catch (SQLException e) {
        e.printStackTrace();
    }
    return respuesta;
}

    public void actualizarSaldo(String nroCuenta,double monto){
        String insertSql = "UPDATE Cuenta SET saldoCuenta="+monto+" WHERE numeroCuenta = "+nroCuenta+";";
        ResultSet resultSet = null;
        try (Connection connection = DriverManager.getConnection(stringConexion);
            PreparedStatement comando = connection.prepareStatement(insertSql, Statement.RETURN_GENERATED_KEYS);) {
            comando.execute();
        
            resultSet = comando.getGeneratedKeys();
 
            while (resultSet.next()) {
                System.out.println("Generated: " + resultSet.getString(1));
            }
        }
        catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void registrarRetiro(String nroCuenta, String monto, String nroTarjeta, String codAut){
        String insertSql = "INSERT INTO Movimientos (numeroCuenta, montoMovimiento, descripcionMovimiento) VALUES ('"+nroCuenta+"','"+monto+"','"+"Retiro "+nroTarjeta+" "+codAut+"')";
        ResultSet resultSet = null;
        try (Connection connection = DriverManager.getConnection(stringConexion);
            PreparedStatement comando = connection.prepareStatement(insertSql, Statement.RETURN_GENERATED_KEYS);) {
            comando.execute();
        
            resultSet = comando.getGeneratedKeys();
 
            while (resultSet.next()) {
                System.out.println("Generated: " + resultSet.getString(1));
            }
        }
        catch (Exception e) {
            e.printStackTrace();
        }
    }
}