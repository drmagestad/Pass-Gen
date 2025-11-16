import argparse
import string
import secrets
import random
import sys

# Constantes de límites solicitados
MIN_LENGTH = 4
MAX_LENGTH = 40
MIN_COUNT = 1
MAX_COUNT = 10

def build_charsets(include_upper: bool, include_lower: bool, include_digits: bool, include_symbols: bool):
    """
    Construye los conjuntos de caracteres según las opciones del usuario.
    Devuelve una lista de tuples (name, charset_string) para poder iterar y asegurar inclusión.
    """
    sets = []
    if include_upper:
        # Mayúsculas A-Z
        sets.append(("upper", string.ascii_uppercase))
    if include_lower:
        # Minúsculas a-z
        sets.append(("lower", string.ascii_lowercase))
    if include_digits:
        # Dígitos 0-9
        sets.append(("digits", string.digits))
    if include_symbols:
        # Símbolos típicos; string.punctuation contiene muchos símbolos útiles
        sets.append(("symbols", string.punctuation))
    return sets

def generate_password(length: int, charsets):
    """
    Genera una contraseña de 'length' caracteres usando los charsets provistos.
    Asegura que haya al menos un carácter de cada conjunto seleccionado.
    """
    # Comprobamos que hay conjuntos disponibles
    if not charsets:
        raise ValueError("No se seleccionó ningún conjunto de caracteres. Debe incluir al menos uno.")

    # Número de conjuntos seleccionados (necesitamos al menos uno por conjunto si queremos garantizar inclusión)
    n_sets = len(charsets)

    # Si la longitud es menor que el número de conjuntos, no es posible garantizar la inclusión
    if length < n_sets:
        raise ValueError(f"Longitud ({length}) demasiado corta para garantizar un carácter de cada uno de los {n_sets} conjuntos seleccionados.")

    # Lista donde iremos agregando caracteres seleccionados de forma segura
    pwd_chars = []

    # 1) Tomar al menos un carácter de cada conjunto (garantiza la presencia de cada tipo)
    for name, charset in charsets:
        # secrets.choice elige de forma criptográficamente segura
        chosen = secrets.choice(charset)
        pwd_chars.append(chosen)

    # 2) Rellenar el resto de la contraseña con caracteres aleatorios del conjunto combinado
    # Construimos la piscina combinada uniendo todos los conjuntos seleccionados
    combined = "".join(cs for _, cs in charsets)

    # Calculamos cuántos caracteres faltan por agregar
    remaining = length - len(pwd_chars)
    for _ in range(remaining):
        pwd_chars.append(secrets.choice(combined))

    # 3) Mezclar la lista de caracteres para que los caracteres "garantizados" no queden al inicio
    # Usamos random.SystemRandom().shuffle que usa un RNG seguro del sistema
    sr = random.SystemRandom()
    sr.shuffle(pwd_chars)

    # 4) Unir la lista en una cadena y retornar la contraseña
    return "".join(pwd_chars)

def parse_args():
    """
    Parseo de argumentos de línea de comandos.
    Permite activar/desactivar conjuntos y configurar longitud y cantidad.
    """
    parser = argparse.ArgumentParser(description="Generador de contraseñas seguras.")
    parser.add_argument("-l", "--length", type=int, default=16,
                        help=f"Longitud de cada contraseña (mín {MIN_LENGTH}, máx {MAX_LENGTH}). Por defecto 16.")
    parser.add_argument("-n", "--count", type=int, default=1,
                        help=f"Cuántas contraseñas generar (mín {MIN_COUNT}, máx {MAX_COUNT}). Por defecto 1.")
    # Flags para excluir conjuntos si el usuario quiere (por defecto todos incluidos)
    parser.add_argument("--no-upper", action="store_true", help="No incluir mayúsculas (A-Z).")
    parser.add_argument("--no-lower", action="store_true", help="No incluir minúsculas (a-z).")
    parser.add_argument("--no-digits", action="store_true", help="No incluir dígitos (0-9).")
    parser.add_argument("--no-symbols", action="store_true", help="No incluir símbolos (puntuación).")
    return parser.parse_args()

def main():
    # Parseamos los argumentos
    args = parse_args()

    # Validaciones de rango para longitud y cantidad
    if args.length < MIN_LENGTH or args.length > MAX_LENGTH:
        print(f"Error: la longitud debe estar entre {MIN_LENGTH} y {MAX_LENGTH}.", file=sys.stderr)
        sys.exit(2)
    if args.count < MIN_COUNT or args.count > MAX_COUNT:
        print(f"Error: la cantidad debe estar entre {MIN_COUNT} y {MAX_COUNT}.", file=sys.stderr)
        sys.exit(2)

    # Determinar qué conjuntos incluir (por defecto todos, a menos que el usuario haya pedido excluirlos)
    include_upper = not args.no_upper
    include_lower = not args.no_lower
    include_digits = not args.no_digits
    include_symbols = not args.no_symbols

    # Construimos la lista de conjuntos seleccionados (cada item es (nombre, charset_string))
    charsets = build_charsets(include_upper, include_lower, include_digits, include_symbols)

    # Si no hay conjuntos seleccionados, informamos y salimos
    if not charsets:
        print("Error: se excluyeron todos los conjuntos de caracteres. Debe permitir al menos uno.", file=sys.stderr)
        sys.exit(2)

    # Generamos las contraseñas solicitadas y las imprimimos en pantalla
    try:
        for i in range(args.count):
            pwd = generate_password(args.length, charsets)
            # Imprimimos cada contraseña en su propia línea
            print(pwd)
    except ValueError as e:
        # Capturamos errores de validación (por ejemplo longitud demasiado corta para garantizar inclusión)
        print("Error:", e, file=sys.stderr)
        sys.exit(3)

if __name__ == "__main__":
    main()
