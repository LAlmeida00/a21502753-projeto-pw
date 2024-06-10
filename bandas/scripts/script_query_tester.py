from bandas.models import Banda, Album, Musica
import os

def clear():
    if os.name == 'posix':
        _ = os.system('clear')
    elif os.name == 'nt':
        _ = os.system('cls')


#1. Listar todas as bandas, em ordenadas alfabéticamente
def listar_bandas_ordem_alfabetica():
    bandas_ordenadas = Banda.objects.all().order_by('nome').values_list('nome', flat=True)
    for banda in bandas_ordenadas:
        print(banda)


#2. Listar o nome dos álbuns de uma banda, ordenados cronológicamente
def listar_albuns_banda(banda_nome):
    albuns_banda = Album.objects.filter(banda__nome=banda_nome).order_by('ano').values_list('nome', flat=True)
    for album in albuns_banda:
        print(album)


#3. Apresentar todos os álbuns que foram lançados entre dois anos à sua escolha.
def listar_albuns_entre_anos(inicio, fim):
    albuns_entre_anos = Album.objects.filter(ano__range=(inicio, fim)).values_list('nome', flat=True)
    for album in albuns_entre_anos:
        print(album)


#4. Criar uma lista de um album, que tenha o nome e os links das músicas.
def listar_musicas_album(album_nome):
    musicas_album = Musica.objects.filter(album__nome=album_nome).values_list('nome', 'spotify_link')
    for musica in musicas_album:
        print(f"Nome: {musica[0]}, Link: {musica[1]}")


#5. Listar os albuns com músicas que durem mais de 5 minutos
def listar_albuns_duracao_superior():
    albuns_superiores_a = Album.objects.filter(musicas__duracao_musica__gte="5:00").distinct()
    for album in albuns_superiores_a:
        print(album.nome)


#6. Listar o nome e o ano de criacao de uma banda
def listar_banda_ano_criacao():
    bandas_ano_criacao = Banda.objects.values_list('nome','ano_criacao')
    for banda in bandas_ano_criacao:
        print(f"Nome: {banda[0]}, Ano de Criação: {banda[1]}")


#7. Contar quantos albums uma banda tem
def contar_total_albums(banda_nome):
    total_albums = Album.objects.filter(banda__nome=banda_nome).count()
    print(f"A banda {banda_nome} tem {total_albums} álbuns.")


#8. Listar todas as músicas que tenham uma determinada palavra
def listar_musicas_com_palavra(palavra):
    musicas_com_palavra = Musica.objects.filter(nome__icontains=palavra).values_list('nome', flat=True)
    for musica in musicas_com_palavra:
        print(musica)


#9. Listar Bandas por nacionalidade
def listar_bandas_por_nacionalidade(nacionalidade):
    bandas_nacionalidade = Banda.objects.filter(nacionalidade__iexact=nacionalidade).values_list('nome', flat=True)
    for banda in bandas_nacionalidade:
        print(banda)


#10. Listar nacionalidades sem reptidos
def listar_nacionalidades_sem_repetidos():
    lista_nacionalidades = Banda.objects.values_list('nacionalidade', flat=True).distinct()
    for nacionalidade in lista_nacionalidades:
        print(nacionalidade)

def menu():
    while True:
        clear()
        print("\nMenu:")
        print("1. Listar todas as bandas em ordem alfabética")
        print("2. Listar os álbuns de uma banda ordenados cronologicamente")
        print("3. Listar os álbuns lançados entre dois anos específicos")
        print("4. Listar as músicas de um álbum com seus links")
        print("5. Listar os álbuns com músicas que duram mais de 5 minutos")
        print("6. Listar o nome e o ano de criação de uma banda")
        print("7. Contar quantos álbuns uma banda tem")
        print("8. Listar todas as músicas que tenham uma determinada palavra")
        print("9. Listar bandas por nacionalidade")
        print("10. Listar nacionalidades sem repetidos")
        print("0. Sair do programa")
        opcao = input("\nEscolha uma das opção: ")

        if opcao == '1':
            listar_bandas_ordem_alfabetica()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == '2':
            print("Exemplo: Metallica, ...")
            banda_nome = input("Introduza o nome da banda:")
            listar_albuns_banda(banda_nome)
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == '3':
            print("Exemplo: 1980, 1990, ...")
            inicio = input("Introduza o ano inicial: ")
            fim = input("Introduzao ano final: ")
            listar_albuns_entre_anos(inicio, fim)
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == '4':
            print("Exemplo: Kill 'Em All, ...")
            album_nome = input("Introduza o nome do álbum: ")
            listar_musicas_album(album_nome)
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == '5':
            listar_albuns_duracao_superior()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == '6':
            listar_banda_ano_criacao()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == '7':
            print("Exemplo: Metallica, ... ")
            banda_nome = input("Introduza o nome da banda: ")
            contar_total_albums(banda_nome)
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == '8':
            print("Exemplo: live, ... ")
            palavra = input("Introduza a palavra desejada:")
            listar_musicas_com_palavra(palavra)
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == '9':
            print("Exemplo: Reino Unido, ... ")
            nacionalidade = input("Introduza a nacionalidade desejada:")
            listar_bandas_por_nacionalidade(nacionalidade)
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == '10':
            listar_nacionalidades_sem_repetidos()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == '0':
            print("Sair do Script... ")
            break
        else:
            print("Opção inválida...")

# Chamando o menu
menu()


# Django Shell
#   python manage.py shell
#   from bandas.scripts import script_query_tester
