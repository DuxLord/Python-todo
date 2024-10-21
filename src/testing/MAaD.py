import os
import shutil

def move_files_to_folders(root_folder):
    # Recorremos las carpetas y archivos
    for folder_name, subfolders, filenames in os.walk(root_folder):
        # Nos saltamos la carpeta raíz para no hacer operaciones sobre ella
        if folder_name == root_folder:
            continue

        # Obtenemos la carpeta principal de nivel superior
        parent_folder = os.path.basename(os.path.normpath(folder_name))

        # Creamos el destino donde moveremos los archivos (directamente en la carpeta del mod)
        mod_folder = os.path.join(root_folder, parent_folder)
        if not os.path.exists(mod_folder):
            os.makedirs(mod_folder)  # Crear la carpeta si no existe

        # Mover cada archivo a su carpeta superior correspondiente
        for filename in filenames:
            file_path = os.path.join(folder_name, filename)
            new_path = os.path.join(mod_folder, filename)

            # Si ya existe un archivo con el mismo nombre en la carpeta destino, añadimos un número al nombre
            counter = 1
            while os.path.exists(new_path):
                base, extension = os.path.splitext(filename)
                new_path = os.path.join(mod_folder, f"{base}_{counter}{extension}")
                counter += 1

            # Mover el archivo
            shutil.move(file_path, new_path)
            print(f"Movido: {file_path} -> {new_path}")

    print("Todos los archivos han sido movidos a sus carpetas superiores.")
    delete_empty_folders(root_folder)

def delete_empty_folders(root_folder):
    # Recorremos las carpetas de nuevo para encontrar y eliminar carpetas vacías
    for folder_name, subfolders, filenames in os.walk(root_folder, topdown=False):
        if folder_name != root_folder:  # No borrar la carpeta raíz
            # Si la carpeta está vacía, la eliminamos
            if not os.listdir(folder_name):
                os.rmdir(folder_name)
                print(f"Carpeta vacía eliminada: {folder_name}")
# Uso del programa
root_folder = r"D:\Neowiz\Browndust2\Browndust2_10000001\BepInEx\plugins\BrownDustX\mods"
move_files_to_folders(root_folder)

