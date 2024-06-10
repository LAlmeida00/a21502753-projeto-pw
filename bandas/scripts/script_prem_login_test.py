from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate

def obter_todos_os_grupos():
    return list(Group.objects.all().values_list('name', flat=True))

def verificar_autenticacao():
    username = input("Por favor, insira seu nome do User: ")
    password = input("Por favor, insira a Password: ")

    if User.objects.filter(username=username).exists():
        user = authenticate(username=username, password=password)

        if user is not None:
            grupos_do_utilizador = user.groups.all()

            if grupos_do_utilizador.exists():
                print("Grupos do user:")
                for grupo in grupos_do_utilizador:
                    print(grupo.name)
            else:
                print("O user não está associado a nenhum dos grupos.")

            if user.groups.filter(name__in=GRUPOS).exists():
                permissions = user.get_all_permissions()
                permissions_list = list(permissions)

                print("Login bem-sucedido e o user tem permissões necessárias.")
                print("Permissões do user:", permissions_list)
            else:
                print("User não tem permissões necessárias.")
        else:
            print("Autenticação falhou. Credenciais inválidas.")
    else:
        print("User não encontrado.")

def menu():
    while True:
        print("\nMenu:")
        print("1. Verificar autenticação")
        print("2. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            verificar_autenticacao()
        elif escolha == "2":
            print("Sair do Script...")
            break
        else:
            print("Opção inválida...")

GRUPOS = obter_todos_os_grupos()
menu()



# Django Shell
#python manage.py shell
# from bandas.scripts import script_prem_login_test

