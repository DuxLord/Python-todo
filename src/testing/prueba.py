import os
import shutil

# Define los parámetros
root_dir = 'C:\\Users\\Gabri\\Desktop\\testdisk-7.3-WIP\\SALVADOR'  # Cambia esto a la ruta donde están las carpetas de PhotoRec
target_dir = 'C:\\Users\\Gabri\\Desktop\\testdisk-7.3-WIP\\SALVADOR'  # Carpeta raíz donde mover los archivos útiles
min_size = 1 * 1024 * 1024 * 1024  # 1 GB en bytes (cambia si es necesario)

# Crea la carpeta destino si no existe
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# Función para mover archivos grandes a la carpeta raíz y eliminar los demás
def process_files():
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(subdir, file)

            try:
                # Verifica el tamaño del archivo
                file_size = os.path.getsize(file_path)

                if file_size >= min_size:
                    # Mueve el archivo a la carpeta raíz
                    shutil.move(file_path, target_dir)
                    print(f'Moved: {file_path} to {target_dir}')
                else:
                    # Borra los archivos pequeños
                    os.remove(file_path)
                    print(f'Deleted: {file_path}')
            except Exception as e:
                print(f'Error processing {file_path}: {e}')

# Ejecuta el proceso
process_files()
