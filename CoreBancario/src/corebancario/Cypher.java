/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package corebancario;

/**
 *
 * @author gmili
 */
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.util.Base64;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;


public class Cypher {

private static final String SECRET_KEY = "123456789asdfghj"; // Clave secreta de 16 bytes
private static final String ALGORITHM = "AES";

public String encriptar(String plainText) {
        try {
                SecretKeySpec secretKey = new SecretKeySpec(SECRET_KEY.getBytes(), ALGORITHM);
                Cipher cipher = Cipher.getInstance(ALGORITHM);
                cipher.init(Cipher.ENCRYPT_MODE, secretKey);
        
                byte[] encryptedBytes = cipher.doFinal(plainText.getBytes());
                return Base64.getEncoder().encodeToString(encryptedBytes);
        } catch (Exception e) {
                // Manejar la excepción aquí, por ejemplo, imprimir el mensaje de error
                System.err.println("Error al encriptar: " + e.getMessage());
                // Devolver un valor predeterminado o lanzar una excepción personalizada si es necesario
                return null;
        }
}
    
public String desencriptar(String encryptedText) {
        try{
                SecretKeySpec secretKey = new SecretKeySpec(SECRET_KEY.getBytes(), ALGORITHM);
                Cipher cipher = Cipher.getInstance(ALGORITHM);
                cipher.init(Cipher.DECRYPT_MODE, secretKey);
                
                byte[] decodedBytes = Base64.getDecoder().decode(encryptedText);
                byte[] decryptedBytes = cipher.doFinal(decodedBytes);
    
                return new String(decryptedBytes);
        } catch (Exception e) {
                // Manejar la excepción aquí, por ejemplo, imprimir el mensaje de error
                System.err.println("Error al desencriptar: " + e.getMessage());
                // Devolver un valor predeterminado o lanzar una excepción personalizada si es necesario
                return null;
        }

}
public String encriptar256(String input) {
        try {
                // Crear una instancia de MessageDigest con el algoritmo SHA-256
                MessageDigest digest = MessageDigest.getInstance("SHA-256");
        
                // Calcular el hash de la cadena de entrada
                byte[] hash = digest.digest(input.getBytes());
                    
                // Convertir el hash byte[] a una representación hexadecimal
                StringBuilder hexString = new StringBuilder();
                for (byte b : hash) {
                        String hex = Integer.toHexString(0xff & b);
                        if (hex.length() == 1) hexString.append('0');
                        hexString.append(hex);
                }
                    
                // Devolver el hash en formato hexadecimal
                return hexString.toString();
                    
        } catch (NoSuchAlgorithmException e) {
                // Manejar la excepción en caso de que el algoritmo no esté disponible
                System.err.println("Algoritmo SHA-256 no encontrado.");
                e.printStackTrace();
                return null; // Devolver nulo en caso de error
        }
        }


}
