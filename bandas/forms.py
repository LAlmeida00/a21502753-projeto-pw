from django import forms    # formulários Django
from .models import Banda, Album, Musica

class BandaForm(forms.ModelForm):
  class Meta:
    model = Banda           # classe para a qual é o formulário
    fields = '__all__'      # inclui no form todos os campos da classe Banda.

    help_texts = {
        'foto': 'Envie uma imagem para a foto da banda (opcional).',
        'nome': 'Digite o nome da banda (máximo de 50 caracteres).',
        'biografia': 'Insira uma breve biografia de 4-5 linhas.',
        'nacionalidade': 'Digite o país de origem da banda.',
        'ano_criacao': 'Digite o ano de criação da banda (opcional).',
   }


class AlbumForm(forms.ModelForm):
  class Meta:
    model = Album           # classe para a qual é o formulário
    fields = '__all__'      # inclui no form todos os campos da classe Album.

    help_texts = {
        'banda': 'Selecione a banda deste álbum.',
        'capa': 'Envie uma imagem para a capa do álbum.',
        'nome': 'Digite o nome do álbum (máximo de 50 caracteres).',
        'ano': 'Digite o ano de lançamento do álbum (opcional).',
    }



class MusicaForm(forms.ModelForm):
  class Meta:
    model = Musica          # classe para a qual é o formulário
    fields = '__all__'      # inclui no form todos os campos da classe Musica.

    help_texts = {
        'album': 'Selecione o álbum desta música.',
        'nome': 'Digite o nome da música (máximo de 50 caracteres).',
        'duracao_musica': 'Digite a duração da música no formato MM:SS (opcional).',
        'spotify_link': 'Insira o link do Spotify para a música (opcional).',
        'letra': 'Insira a letra da música, se disponível.',
    }