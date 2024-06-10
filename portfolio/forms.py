from django import forms    # formulários Django
from django.forms import inlineformset_factory
from .models import Profile, Interest, Skill, Competency, Experience, SocialLink, Project

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user_photo', 'user_name']

InterestFormSet = inlineformset_factory(Profile, Interest, form=forms.ModelForm, fields=['interest_title', 'description'], extra=1)
SkillFormSet = inlineformset_factory(Profile, Skill, form=forms.ModelForm, fields=['skills_title', 'description'], extra=1)
CompetencyFormSet = inlineformset_factory(Profile, Competency, form=forms.ModelForm, fields=['competency_title', 'description'], extra=1)
ExperienceFormSet = inlineformset_factory(Profile, Experience, form=forms.ModelForm, fields=['experience_title', 'start_date', 'end_date', 'description'], extra=1)
SocialLinkFormSet = inlineformset_factory(Profile, SocialLink, form=forms.ModelForm, fields=['platform', 'link'], extra=1)


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'photo', 'website_link']


class SocialLinkForm(forms.ModelForm):
    class Meta:
        model = SocialLink
        fields = ['platform', 'link']
