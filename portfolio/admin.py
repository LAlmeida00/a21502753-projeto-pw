from django.contrib import admin
from .models import Profile, SocialLink, Interest, Skill, Competency, Experience, Project

class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 1

class InterestInline(admin.TabularInline):
    model = Interest
    extra = 1

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1

class CompetencyInline(admin.TabularInline):
    model = Competency
    extra = 1

class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1

class ProjectInline(admin.TabularInline):
    model = Project
    extra = 1

class ProfileAdmin(admin.ModelAdmin):
    inlines = [SocialLinkInline, InterestInline, SkillInline, CompetencyInline, ExperienceInline, ProjectInline]

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Project)
