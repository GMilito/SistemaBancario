using System;
using System.Text;


namespace Cajero
{
    public class AuthCode
    {
        public string GenerarCodigoAutorizacion(int lar)
        {
            const string chars = "0123456789";
            Random random = new Random();
            StringBuilder stringBuilder = new StringBuilder(lar);

            for (int i = 0; i < lar; i++)
            {
                stringBuilder.Append(chars[random.Next(chars.Length)]);
            }

            return stringBuilder.ToString();
        }
    }
}
