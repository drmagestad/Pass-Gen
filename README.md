## Generador de Contraseñas Seguras (CLI)

Este proyecto es un generador de contraseñas seguras escrito en Python, diseñado para ofrecer combinaciones robustas utilizando fuentes criptográficamente seguras. Permite personalizar la longitud, la cantidad de contraseñas y los tipos de caracteres incluidos, manteniendo siempre un nivel alto de seguridad.

### Características

- Longitud configurable de cada contraseña (mín. 4, máx. 40).  
- Generación múltiple: crea entre 1 y 10 contraseñas por ejecución.  
- Conjuntos de caracteres seleccionables: mayúsculas, minúsculas, dígitos y símbolos.  
- Garantiza al menos un carácter de cada tipo seleccionado.  
- Usa `secrets` para selección criptográficamente segura.  
- Mezcla final con `random.SystemRandom()` para evitar patrones.  
- Código comentado en español para fácil comprensión.  

### Uso

En la línea de comandos:

```bash
python password_generator.py --help
python password_generator.py -l 16 -n 5
python password_generator.py --length 12 --count 3 --no-symbols

