import os
import django
from projetoPortfolioPW.models import *
from django.db.models import Count, Min

# Configurando o ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')
django.setup()

def query_tester():
    try:
        print("\n 1. Número total de áreas científicas que estao registadas na base de dados")
        total_areas_cientificas = AreaCientifica.objects.count()
        print(f"O número total de áreas científicas que existem na base de dados é {total_areas_cientificas}")

        print("\n 2. Listar todos os cursos disponíveis:")
        for curso in Curso.objects.all():
            print(f"- {curso.nome}")

        print("\n 3. Lista todas as disciplinas com mais de 4 ECTS")
        disciplinas_com_mais_ects = Disciplina.objects.filter(ects__gt=4)
        for disciplina in disciplinas_com_mais_ects:
            print(f"- {disciplina.nome} com {disciplina.ects} etcs")

        print(f"\n 4.Numero total de disciplinas que existe no primeiro ano")
        total_disciplinas_ano = Disciplina.objects.filter(ano=1).count()
        print(f"O número total de disciplinas do 1º ano é: {total_disciplinas_ano}")

        print("\n 5. Listar todas as disciplinas do 3º ano")
        disciplinas_terceiro_ano = Disciplina.objects.filter(ano=3, curso__nome="Engenharia Informática")
        for disciplina in disciplinas_terceiro_ano:
            print(f"- {disciplina.nome}")

    except Exception as e:
        print(f"Ocorreu um erro na execucao do script: {e}")


# Django Shell

# python manage.py shell

# from projetoPortfolioPW.scripts.script_query_tester import query_tester
# query_tester()