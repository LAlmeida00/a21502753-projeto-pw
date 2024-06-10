from django.db import models

class Profile(models.Model):
    user_name = models.CharField(max_length=50)
    user_photo = models.ImageField(upload_to='portfolio/', null=True, blank=True)
    landing_text = models.TextField(blank=True, null=True, max_length=100)

    def __str__(self):
        return self.user_name

class SocialLink(models.Model):
    profile = models.ForeignKey(Profile, related_name='social_links', on_delete=models.CASCADE)
    PLATFORM_CHOICES = [
        ('facebook', 'Facebook'),
        ('linkedin', 'LinkedIn'),
        ('twitter', 'Twitter'),
        ('instagram', 'Instagram'),
        ('other', 'Other'),
    ]
    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.profile.user_name} - {self.get_platform_display()}"

class Interest(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='interests_set')
    interest_title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.description

class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='skills_set')
    skills_title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.description

class Competency(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='competencies_set')
    competency_title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.description

class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='experiences_set')
    experience_title = models.CharField(max_length=50)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.description

class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='projects_set', null=True, blank=True)
    project_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='portfolio/', null=True, blank=True)
    website_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.project_name

