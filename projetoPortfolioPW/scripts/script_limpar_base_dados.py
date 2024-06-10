from projetoPortfolioPW.models import * # Importando os modelos do Django


# Função para limpar a base de dados
def limpar_base_de_dados():
    print("Iniciar processo de Limpeza da base de dados...")

    # Excluindo todos os objetos de cada modelo
    Curso.objects.all().delete()
    print("Tabela Curso Limpa")
    Disciplina.objects.all().delete()
    print("Tabela Disciplina Limpa")
    AreaCientifica.objects.all().delete()
    print("Tabela AreaCientifica Limpa")
    LinguagemProgramacao.objects.all().delete()
    print("Tabela LinguagemProgramacao Limpa")
    Projeto.objects.all().delete()
    print("Tabela Projeto Limpa")
    Docente.objects.all().delete()
    print("Tabela Docente Limpa")

    print("CONCLUIDO COM SUCESSO!!\nBase de dados limpa")

# Django Shell

# python manage.py shell

# from projetoPortfolioPW.scripts.script_limpar_base_dados import limpar_base_de_dados
# limpar_base_de_dados()
