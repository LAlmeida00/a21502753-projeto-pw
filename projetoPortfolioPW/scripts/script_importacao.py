from projetoPortfolioPW.models import *  # Importa todos os modelos do seu aplicativo
from django.db import transaction  # Importa o utilitário de transação do Django
import json  # Importa o módulo JSON para trabalhar com dados JSON
import os  # Importa o módulo OS para lidar com caminhos de arquivos

def importar_curso(ficheiro_json):

    # Remove todos os registros existentes dos modelos para evitar duplicados
    Curso.objects.all().delete()
    Disciplina.objects.all().delete()
    AreaCientifica.objects.all().delete()
    LinguagemProgramacao.objects.all().delete()
    Projeto.objects.all().delete()
    Docente.objects.all().delete()

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

            # Extrai os detalhes do curso do dicionário de dados
            detalhes_curso = dados['courseDetail']

            # Cria ou obtém o objeto Curso do base de dados com base nos detalhes fornecidos
            curso, created = Curso.objects.get_or_create(
                nome=detalhes_curso['courseName'],
                apresentacao=detalhes_curso['presentation'],
                objetivos=detalhes_curso['objectives'],
                competencias=detalhes_curso['competences']
            )

            # Itera sobre os dados do plano de curso para criar as disciplinas
            for disciplina_data in dados['courseFlatPlan']:

                # cria a Área Científica associada à disciplina
                area_cientifica, _ = AreaCientifica.objects.get_or_create(
                    nome=disciplina_data['curricularBranchName']
                )

                # Cria ou obtém a Disciplina na Base de dados com base nos dados fornecidos
                disciplina, created = Disciplina.objects.get_or_create(
                    nome=disciplina_data['curricularUnitName'],
                    ano=disciplina_data['curricularYear'],
                    semestre=disciplina_data['semester'],
                    ects=disciplina_data['ects'],
                    curricular_unit_readable_code=disciplina_data['curricularIUnitReadableCode'],
                    area_cientifica=area_cientifica,
                    curso=curso
                )

    print("Importação dos dados para a base de dados concluída com sucesso.")



# Django Shell

#python manage.py shell
# from projetoPortfolioPW.scripts import script_importacao
# script_importacao.importar_curso("lei.json")
