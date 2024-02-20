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
    + "integratedSecurity=true;"
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
        catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void registrarRetiro(String nroCuenta, String monto, String nroTarjeta, String codAut){
        String insertSql = "INSERT INTO Movimientos (numeroCuenta, montoMovimiento, descripcionMovimiento) VALUES ('"+nroCuenta+"','"+monto+"','"+"Retiro "+nroTarjeta+" "+codAut+"')";
        ResultSet resultSet = null;
        try (Connection connection = DriverManager.getConnection(conexionString);
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