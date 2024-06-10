from bandas.models import *
import json


def load_data():
    Banda.objects.all().delete()
    Album.objects.all().delete()
    Musica.objects.all().delete()

    with open('bandas/json/bandas.json') as f:
        bandas = json.load(f)

        for banda in bandas:
            Banda.objects.create(
                foto = banda['foto'],
                nome = banda['nome'],
                biografia = banda['biografia'],
                nacionalidade = banda['nacionalidade'],
                ano_criacao = banda['ano_criacao']
                )

    with open('bandas/json/albums.json') as f:
        albums = json.load(f)

        for album_data in albums:

            album = Album.objects.create(
                banda = Banda.objects.get(nome = album_data['banda']),
                nome = album_data['nome'],
                ano = album_data['ano'],
                capa = album_data['capa']
            )

            for musica_data in album_data['musicas']:
                Musica.objects.create(
                    album = album,
                    nome = musica_data['nome'],
                    duracao_musica = musica_data['duracao_musica'],
                    spotify_link = musica_data['spotify_link']
                )

    print("Importação dos dados para a base de dados concluída com sucesso.")


# Django Shell

#python manage.py shell
#from bandas.loader import load_data
#load_data()
