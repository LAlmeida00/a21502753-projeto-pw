import zipfile
import os

def extract_icons(zip_file_path, output_folder):
    # Verificar se o arquivo ZIP existe
    if not os.path.exists(zip_file_path):
        print(f"Arquivo ZIP '{zip_file_path}' não encontrado.")
        return

    # Extrair os arquivos
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(output_folder)

    # Verificar se a extração foi bem-sucedida
    extracted_files = os.listdir(output_folder)
    if extracted_files:
        print(f"Arquivos extraídos com sucesso para '{output_folder}'.")
    else:
        print("Nenhum arquivo foi extraído. Verifique se o arquivo ZIP contém arquivos.")

if __name__ == "__main__":
    zip_file_path = "/home/a21502753/project/static/meteo/zip/icons_ipma_weather.zip"  # Caminho para o arquivo ZIP
    output_folder = "/home/a21502753/project/static/meteo/icones"  # Pasta onde deseja extrair os arquivos
    extract_icons(zip_file_path, output_folder)


# Django Shell
#python manage.py shell
#exec(open('/home/a21502753/project/meteo/scripts/unzinp_file.py').read())
