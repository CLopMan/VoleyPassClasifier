import os

def modify_file(file_path, add_value=20):
   # Leer el contenido original del archivo
    with open(file_path, "r") as infile:
        lines = infile.readlines()

    # Sobrescribir el archivo con las líneas modificadas
    with open(file_path, "w") as outfile:
        for line in lines:
            line = line.strip()  # Elimina espacios o saltos de línea
            values = line.split()  # Divide la línea en valores separados por espacios
            
            if len(values) >= 2:
                # Procesar los dos primeros valores
                x = float(values[0]) / 1280
                y = float(values[1]) / 720

                w = float(add_value) / 1280
                h = float(add_value) / 720

                # Crear la nueva línea con los valores procesados y el valor añadido
                new_line = f"0 {x:.6f} {y:.6f} {w:.6f} {h:.6f}\n"
                outfile.write(new_line)

def process_directories(base_directory, add_value=20):
     for root, dirs, files in os.walk(base_directory):
        for file in files:
            
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                print(f"Procesando archivo: {file_path}")
                modify_file(file_path, add_value)


base_directory = "."

# Valor que se añadirá al final de cada línea
add_value = 20

# Procesar todos los directorios y archivos
process_directories(base_directory, add_value)

print("Procesamiento completado.")

