from projetoPortfolioPW.models import *  # Importa o modelo LinguagemProgramacao do seu aplicativo
from django.db import transaction  # Importa o utilitário de transação do Django
import json  # Importa o módulo JSON para trabalhar com dados JSON
import os  # Importa o módulo OS para lidar com caminhos de arquivos

def importar_linguagens_prog(ficheiro_json):

    LinguagemProgramacao.objects.all().delete()

    # Obtém o diretório atual do script Python
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))

    # Constrói o caminho absoluto para o arquivo JSON fornecido
    caminho_json = os.path.abspath(os.path.join(diretorio_atual, "..", "json", ficheiro_json))

    #print("Caminho do arquivo JSON:", caminho_json)

    # Abre o arquivo JSON para leitura
    with open(caminho_json, 'r') as f:

        # Carrega os dados do arquivo JSON em um dicionário Python
        dados = json.load(f)

        # Inicia uma transação atômica para garantir consistência do banco de dados
        with transaction.atomic():
            for item in dados:
                LinguagemProgramacao.objects.create(nome=item["nome"])

    print("Importação dos dados para tabela de linguagens de programacao concluída com sucesso.")

# Django Shell

# python manage.py shell
# from projetoPortfolioPW.scripts import script_import_ling_prog
# script_import_ling_prog.importar_linguagens_prog("lingProg.json")
