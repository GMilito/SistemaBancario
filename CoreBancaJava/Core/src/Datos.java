import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class Datos {
    String conexionString =
    "jdbc:sqlserver://localhost:1433"
    + "database=BDCore;"
    + "user=sa@DESKTOP-BC9PPIJ\\PRINCIPAL;"
    + "password=1598753;"
    + "encrypt=true;"
    + "trustServerCertificate=false;"
    + "loginTimeout=30;";

    public String consultarSaldo(String nroCuenta){
        ResultSet resultado = null;
        String respuesta = null;
        try (Connection connection = DriverManager.getConnection(conexionString);
            Statement comando = connection.createStatement();) {
            String sqlQuery = "SELECT saldoCuenta FROM Cuenta WHERE numeroCuenta = "+nroCuenta+";";
            resultado = comando.executeQuery(sqlQuery);
            respuesta = resultado.getString("saldoCuenta");
        }
        catch (SQLException e) {
            e.printStackTrace();
        }
        return respuesta;
    }
    public void actualizarSaldo(String nroCuenta,String monto){
        String insertSql = "UPDATE Cuenta SET saldoCuenta="+monto+" WHERE numeroCuenta = "+nroCuenta+";";
        ResultSet resultSet = null;
        try (Connection connection = DriverManager.getConnection(conexionString);
            PreparedStatement comando = connection.prepareStatement(insertSql, Statement.RETURN_GENERATED_KEYS);) {
            comando.execute();
        
            resultSet = comando.getGeneratedKeys();
 
            while (resultSet.next()) {
                System.out.println("Generated: " + resultSet.getString(1));
            }
        }
        // Handle any errors that may have occurred.
        catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void registrarMovimiento(String nroCuenta, String monto, String desc){
        String insertSql = "INSERT INTO Movimientos (numeroCuenta, montoMovimiento, descripcionMovimiento) VALUES ('"+nroCuenta+"','"+monto+"','"+desc+"')";
        ResultSet resultSet = null;
        try (Connection connection = DriverManager.getConnection(conexionString);
            PreparedStatement comando = connection.prepareStatement(insertSql, Statement.RETURN_GENERATED_KEYS);) {
            comando.execute();
        
            resultSet = comando.getGeneratedKeys();
 
            while (resultSet.next()) {
                System.out.println("Generated: " + resultSet.getString(1));
            }
        }
        // Handle any errors that may have occurred.
        catch (Exception e) {
            e.printStackTrace();
        }
    }
}