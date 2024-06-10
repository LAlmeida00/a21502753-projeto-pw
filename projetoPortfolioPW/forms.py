from django import forms    # formulários Django
from .models import Curso, Disciplina, Projeto

class CursoForm(forms.ModelForm):
  class Meta:
    model = Curso        # classe para a qual é o formulário
    fields = '__all__'   # inclui no form todos os campos da classe Curso.
    

class DisciplinaForm(forms.ModelForm):
  class Meta:
    model = Disciplina        # classe para a qual é o formulário
    fields = '__all__'   # inclui no form todos os campos da classe Disciplina.
    

class ProjetoForm(forms.ModelForm):
  class Meta:
    model = Projeto          # classe para a qual é o formulário
    fields = '__all__'       # inclui no form todos os campos da classe Projeto.
