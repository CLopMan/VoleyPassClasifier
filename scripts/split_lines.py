import os

def process_files_and_split_lines(base_directory):
    """
    Recorre un conjunto de directorios, toma cada archivo, y escribe
    cada línea del archivo en un nuevo archivo llamado 'carpeta_N.txt'.

    :param base_directory: Ruta del directorio base donde se encuentran los archivos.
    """
    for root, dirs, files in os.walk(base_directory):
        carpeta = os.path.basename(root)  # Nombre de la carpeta actual
        file_index = 1  # Índice del archivo en la carpeta
        
        for file in files:
            sec = os.path.splitext(file)[0]
            if file.endswith(".txt"):  # Procesar solo archivos .txt
                file_path = os.path.join(root, file)
                
                # Leer el contenido del archivo
                with open(file_path, "r") as infile:
                    lines = infile.readlines()
                
                # Escribir cada línea en un archivo separado
                for i, line in enumerate(lines):
                    # Crear el nombre del nuevo archivo
                    new_filename = f"{carpeta}_{sec}_{file_index}.txt"
                    output_directory = os.path.join(base_directory, "output")
                    os.makedirs(output_directory, exist_ok=True)
                    new_filepath = os.path.join(output_directory, new_filename)

                    
                    # Escribir la línea en el archivo correspondiente
                    with open(new_filepath, "w") as outfile:
                        outfile.write(line.strip() + "\n")
                    
                    print(f"Línea {i+1} del archivo '{file}' escrita en '{new_filename}'")
                
                file_index += 1  # Incrementar el índice del archivo en la carpeta

# Ruta del directorio base (cámbiala por tu ruta)
base_directory = "."

# Procesar los archivos
process_files_and_split_lines(base_directory)

print("Procesamiento completado.")

