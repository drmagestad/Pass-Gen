<h1 align="center">Generador de Contraseñas Seguras (CLI)</h1>

<p align="center">
  <img src="https://github.com/drmagestad/Pass-Gen/blob/846b99fa9710d6478da76856161969ef350848f1/img/pass_gen.png" alt="INFO" />
</p>

Este proyecto es un generador de contraseñas seguras escrito en Python, diseñado para ofrecer combinaciones robustas utilizando fuentes criptográficamente seguras. Permite personalizar la longitud, la cantidad de contraseñas y los tipos de caracteres incluidos, manteniendo siempre un nivel alto de seguridad.

### Características

- Longitud configurable de cada contraseña (mín. 4, máx. 40).  
- Generación múltiple: crea entre 1 y 10 contraseñas por ejecución.  
- Conjuntos de caracteres seleccionables: mayúsculas, minúsculas, dígitos y símbolos.  
- Garantiza al menos un carácter de cada tipo seleccionado.  
- Usa `secrets` para selección criptográficamente segura.  
- Mezcla final con `random.SystemRandom()` para evitar patrones.  

### Modo de Uso

En la línea de comandos:

- Mostrar la ayuda completa del script

```bash
python password_generator.py --help
```
- Generar 1 contraseña de 16 caracteres (valores por defecto)

```bash
python password_generator.py
```
- Generar 5 contraseñas de 16 caracteres

```bash
python password_generator.py -n 5
```
- Generar 3 contraseñas de 12 caracteres

```bash
python password_generator.py --length 12 --count 3
```
- Generar una contraseña sin simbolos

```bash
python password_generator.py --no-symbols
```
- Generar una contraseña solo con letras mayúsculas y dígitos

```bash
python password_generator.py --no-lower --no-symbols
```

---

### Notas finales

Este generador de contraseñas lo hice después de ver varios proyectos similares en YouTube, Reddit y algunos foros. Quería probar cómo se estructuran y funcionan este tipo de scripts, y a la vez, entender mejor algunos conceptos básicos de seguridad y manejo de contraseñas en Python.

Es un proyecto sencillo, pero me ayudó a practicar con temas como la selección aleatoria segura, el manejo de argumentos en la línea de comandos y la organización del código.  


