import os
import shutil

def move_folders_to_temp(root_folder):
    """Mueve todas las carpetas de 'mods' a 'temp', excepto 'temp'."""
    temp_folder = os.path.join(root_folder, 'temp')

    # Crear la carpeta temp si no existe
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)
        print(f"Carpeta creada: {temp_folder}")

    # Recorremos todas las carpetas dentro de 'mods'
    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)

        # Mover las carpetas que no sean 'temp'
        if os.path.isdir(folder_path) and folder_name != 'temp':
            dest_path = os.path.join(temp_folder, folder_name)

            # Mover la carpeta a 'temp'
            shutil.move(folder_path, dest_path)
            print(f"Carpeta movida: {folder_path} -> {dest_path}")

def move_folders_from_temp(root_folder):
    """Mueve todas las carpetas desde 'temp' a la raíz de 'mods'."""
    temp_folder = os.path.join(root_folder, 'temp')

    # Verifica si la carpeta 'temp' existe
    if not os.path.exists(temp_folder):
        print(f"La carpeta 'temp' no existe en {root_folder}")
        return

    # Recorremos todas las carpetas dentro de 'temp'
    for folder_name in os.listdir(temp_folder):
        folder_path = os.path.join(temp_folder, folder_name)

        # Mover las carpetas de vuelta a la raíz de 'mods'
        if os.path.isdir(folder_path):
            dest_path = os.path.join(root_folder, folder_name)

            # Mover la carpeta de 'temp' a la raíz de 'mods'
            shutil.move(folder_path, dest_path)
            print(f"Carpeta movida: {folder_path} -> {dest_path}")

# Uso del programa
mods_folder = r"D:\Neowiz\Browndust2\Browndust2_10000001\BepInEx\plugins\BrownDustX\mods"  # Cambia esta ruta según tu caso

# Mover las carpetas a 'temp'
move_folders_to_temp(mods_folder)
# Mover las carpetas de 'temp' a la raíz de 'mods'
#move_folders_from_temp(mods_folder)