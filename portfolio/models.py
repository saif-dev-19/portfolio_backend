from django.db import models


class TimeStampedModel(models.Model):
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["order", "id"]


class Hero(TimeStampedModel):
    name = models.CharField(max_length=160)
    role = models.CharField(max_length=160)
    headline_name = models.CharField(max_length=160, blank=True)
    headline_role = models.CharField(max_length=160, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="hero/", blank=True, null=True)
    cv_file = models.FileField(upload_to="hero/files/", blank=True, null=True)
    cv_url = models.URLField(blank=True)

    class Meta(TimeStampedModel.Meta):
        verbose_name = "Hero"
        verbose_name_plural = "Hero"

    def __str__(self):
        return self.name


class HeroInfo(TimeStampedModel):
    hero = models.ForeignKey(Hero, related_name="info_items", on_delete=models.CASCADE)
    label = models.CharField(max_length=80)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.label}: {self.value}"


class HeroStat(TimeStampedModel):
    hero = models.ForeignKey(Hero, related_name="stats", on_delete=models.CASCADE)
    value = models.CharField(max_length=40)
    label = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.value} {self.label}"


class EssentialLink(TimeStampedModel):
    hero = models.ForeignKey(Hero, related_name="essential_links", on_delete=models.CASCADE)
    label = models.CharField(max_length=80)
    url = models.URLField(blank=True)
    icon = models.CharField(max_length=80, help_text="Example: github, linkedin, leetcode, codeforces")
    color = models.CharField(max_length=20, default="#12F7D6")

    def __str__(self):
        return self.label


class About(TimeStampedModel):
    title = models.CharField(max_length=160, default="About Me")
    greeting = models.CharField(max_length=160, default="Hello!")
    description = models.TextField()
    image = models.ImageField(upload_to="about/", blank=True, null=True)

    class Meta(TimeStampedModel.Meta):
        verbose_name = "About"
        verbose_name_plural = "About"

    def __str__(self):
        return self.title


class SkillGroup(TimeStampedModel):
    title = models.CharField(max_length=160)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Skill(TimeStampedModel):
    group = models.ForeignKey(SkillGroup, related_name="skills", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    icon_name = models.CharField(max_length=80, blank=True, help_text="Simple Icons slug, e.g. django, react")
    icon_image = models.ImageField(upload_to="skills/icons/", blank=True, null=True)
    color = models.CharField(max_length=20, default="#12F7D6")
    fallback = models.CharField(max_length=12, blank=True)

    def __str__(self):
        return self.name


class Experience(TimeStampedModel):
    role = models.CharField(max_length=160)
    company = models.CharField(max_length=160, blank=True)
    location = models.CharField(max_length=160, blank=True)
    period = models.CharField(max_length=160, blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    tags = models.JSONField(default=list, blank=True)

    def __str__(self):
        return f"{self.role} - {self.company}"


class Education(TimeStampedModel):
    degree = models.CharField(max_length=180)
    school = models.CharField(max_length=180)
    location = models.CharField(max_length=160, blank=True)
    period = models.CharField(max_length=160, blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    tags = models.JSONField(default=list, blank=True)

    def __str__(self):
        return f"{self.degree} - {self.school}"


class Project(TimeStampedModel):
    title = models.CharField(max_length=180)
    category = models.CharField(max_length=120, blank=True)
    description = models.TextField(blank=True)
    details = models.TextField(blank=True)
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    tags = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.title


class Certificate(TimeStampedModel):
    name = models.CharField(max_length=180)
    issuer = models.CharField(max_length=160, blank=True)
    credential = models.CharField(max_length=160, default="Certificate")
    credential_id = models.CharField(max_length=160, blank=True)
    period = models.CharField(max_length=80, blank=True)
    issue_date = models.CharField(max_length=80, blank=True)
    image = models.ImageField(upload_to="certificates/", blank=True, null=True)
    verify_url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    tags = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.name


class Blog(TimeStampedModel):
    title = models.CharField(max_length=180)
    label = models.CharField(max_length=100, blank=True)
    author = models.CharField(max_length=120, blank=True)
    date = models.CharField(max_length=80, blank=True)
    duration = models.CharField(max_length=80, blank=True)
    image = models.ImageField(upload_to="blogs/", blank=True, null=True)
    excerpt = models.TextField(blank=True)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Contact(TimeStampedModel):
    title = models.CharField(max_length=160, default="Contact")
    description = models.TextField(blank=True)
    email = models.EmailField()

    class Meta(TimeStampedModel.Meta):
        verbose_name = "Contact"
        verbose_name_plural = "Contact"

    def __str__(self):
        return self.email


class Footer(TimeStampedModel):
    copyright_text = models.CharField(max_length=255)
    design_by_text = models.CharField(max_length=120, blank=True)
    design_by_url = models.URLField(blank=True)

    class Meta(TimeStampedModel.Meta):
        verbose_name = "Footer"
        verbose_name_plural = "Footer"

    def __str__(self):
        return self.copyright_text
