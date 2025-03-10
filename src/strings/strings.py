class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):
        """
        Verifica si una cadena es un palíndromo (se lee igual de izquierda a derecha y viceversa).
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si es palíndromo, False en caso contrario
        """
        texto = texto.lower().replace(" ", "")
        longitud = len(texto)
        for i in range(longitud // 2):
            if texto[i] != texto[longitud - 1 - i]:
                return False
        return True
    
    def invertir_cadena(self, texto):
        """
        Invierte una cadena de texto sin usar slicing ni reversed().
        
        Args:
            texto (str): Cadena a invertir
            
        Returns:
            str: Cadena invertida
        """
        resultado = ""
        for char in texto:
            resultado = char + resultado
        return resultado
    
    def contar_vocales(self, texto):
        """
        Cuenta el número de vocales en una cadena.
        
        Args:
            texto (str): Cadena para contar vocales
            
        Returns:
            int: Número de vocales en la cadena
        """
        vocales = "aeiouAEIOU"
        return sum(1 for char in texto if char in vocales)
    
    def contar_consonantes(self, texto):
        """
        Cuenta el número de consonantes en una cadena.
        
        Args:
            texto (str): Cadena para contar consonantes
            
        Returns:
            int: Número de consonantes en la cadena
        """
        vocales = "aeiouAEIOU"
        return sum(1 for char in texto if char.isalpha() and char not in vocales)
    
    def es_anagrama(self, texto1, texto2):
        """
        Verifica si dos cadenas son anagramas (contienen exactamente los mismos caracteres).
        
        Args:
            texto1 (str): Primera cadena
            texto2 (str): Segunda cadena
            
        Returns:
            bool: True si son anagramas, False en caso contrario
        """
        texto1 = texto1.lower().replace(" ", "")
        texto2 = texto2.lower().replace(" ", "")
        if len(texto1) != len(texto2):
            return False
        dict1 = {}
        for char in texto1:
            dict1[char] = dict1.get(char, 0) + 1
        for char in texto2:
            if char not in dict1:
                return False
            dict1[char] -= 1
            if dict1[char] == 0:
                del dict1[char]
        return len(dict1) == 0
    
    def contar_palabras(self, texto):
        """
        Cuenta el número de palabras en una cadena.
        
        Args:
            texto (str): Cadena para contar palabras
            
        Returns:
            int: Número de palabras en la cadena
        """
        if not texto.strip():
            return 0
        return len(texto.split())
    
    def palabras_mayus(self, texto):
        """
        Pon en Mayuscula la primera letra de cada palabra en una cadena.
        
        Args:
            texto (str): Cadena
            
        Returns:
            str: Cadena con la primera letra de cada palabra en mayúscula
        """
        palabras = texto.split()
        return " ".join(palabra[0].upper() + palabra[1:].lower() if palabra else "" for palabra in palabras)
    
    def eliminar_espacios_duplicados(self, texto):
        """
        Elimina espacios duplicados en una cadena.
        
        Args:
            texto (str): Cadena con posibles espacios duplicados
            
        Returns:
            str: Cadena sin espacios duplicados
        """
        resultado = ""
        anterior = ""
        for char in texto:
            if char != " " or anterior != " ":
                resultado += char
            anterior = char
        return resultado.strip()
    
    def es_numero_entero(self, texto):
        """
        Verifica si una cadena representa un número entero sin usar isdigit().
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si la cadena representa un número entero, False en caso contrario
        """
        texto = texto.strip()
        if not texto:
            return False
        if texto[0] == "-":
            texto = texto[1:]
        if not texto:
            return False
        for char in texto:
            if char < "0" or char > "9":
                return False
        return True
    
    def cifrar_cesar(self, texto, desplazamiento):
        """
        Aplica el cifrado César a una cadena de texto.
        
        Args:
            texto (str): Cadena a cifrar
            desplazamiento (int): Número de posiciones a desplazar cada letra
            
        Returns:
            str: Cadena cifrada
        """
        resultado = ""
        for char in texto:
            if char.isalpha():
                base = ord("A") if char.isupper() else ord("a")
                resultado += chr((ord(char) - base + desplazamiento) % 26 + base)
            else:
                resultado += char
        return resultado
    
    def descifrar_cesar(self, texto, desplazamiento):
        """
        Descifra una cadena cifrada con el método César.
        
        Args:
            texto (str): Cadena cifrada
            desplazamiento (int): Número de posiciones que se desplazó cada letra
            
        Returns:
            str: Cadena descifrada
        """
        return self.cifrar_cesar(texto, -desplazamiento)
    
    def encontrar_subcadena(self, texto, subcadena):
        """
        Encuentra todas las posiciones de una subcadena en un texto sin usar find() o index().
        
        Args:
            texto (str): Cadena principal
            subcadena (str): Subcadena a buscar
            
        Returns:
            list: Lista con las posiciones iniciales de cada ocurrencia
        """
        if not subcadena or len(subcadena) > len(texto):
            return []
        posiciones = []
        len_sub = len(subcadena)
        for i in range(len(texto) - len_sub + 1):
            match = True
            for j in range(len_sub):
                if texto[i + j] != subcadena[j]:
                    match = False
                    break
            if match:
                posiciones.append(i)
        return posiciones