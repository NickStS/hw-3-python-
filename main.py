import os
import shutil
import concurrent.futures

def process_file(file_path, destination_folder):
    file_name = os.path.basename(file_path)
    file_extension = os.path.splitext(file_name)[1][1:].lower()
    new_folder = os.path.join(destination_folder, file_extension)
    os.makedirs(new_folder, exist_ok=True)
    new_file_path = os.path.join(new_folder, file_name)
    shutil.move(file_path, new_file_path)

def process_folder(folder_path, destination_folder):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for root, _, files in os.walk(folder_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                futures.append(executor.submit(process_file, file_path, destination_folder))
        concurrent.futures.wait(futures)

if __name__ == '__main__':
    folder_path = 'H:\Programming\Projects_Python\less goit\garbage'
    destination_folder = 'Sorted file'
    os.makedirs(destination_folder, exist_ok=True)
    process_folder(folder_path, destination_folder)
    print("Sorting is complete.")
