import os, zipfile, glob


def delete_json_files():
    _path = '/Users/ferna/Downloads/Takeout/Google Fotos'

    # Navegar pelos diretórios e arquivos dentro do caminho
    for root, dirs, files in os.walk(_path):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)  # Apagar o arquivo .json
                    print(f"Arquivo {file} apagado com sucesso.")
                except Exception as e:
                    print(f"Erro ao apagar {file}: {e}")


def extract_zip(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        try:
            zip_ref.extractall(os.path.dirname(zip_path))
        except FileNotFoundError as e:
            print(f"Error extracting {zip_path}: {e}")


def main():
    directory_path = '/Users/ferna/Downloads'
    zip_files = glob.glob(os.path.join(directory_path, '*.zip'))

    for zip_file in zip_files:
        print(f"Extracting content from: {zip_file}")
        extract_zip(zip_file)


if __name__ == "__main__":
    # main()
    delete_json_files()
