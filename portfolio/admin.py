from django.contrib import admin

from .models import (
    About,
    Blog,
    Certificate,
    Contact,
    Education,
    EssentialLink,
    Experience,
    Footer,
    Hero,
    HeroInfo,
    HeroStat,
    Project,
    Skill,
    SkillGroup,
)


class HeroInfoInline(admin.TabularInline):
    model = HeroInfo
    extra = 0
    ordering = ("order", "id")


class HeroStatInline(admin.TabularInline):
    model = HeroStat
    extra = 0
    ordering = ("order", "id")


class EssentialLinkInline(admin.TabularInline):
    model = EssentialLink
    extra = 0
    ordering = ("order", "id")


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    inlines = [HeroInfoInline, HeroStatInline, EssentialLinkInline]
    list_display = ("name", "role", "is_active", "order", "updated_at")
    search_fields = ("name", "role", "headline_name", "headline_role", "description")
    list_filter = ("is_active",)
    ordering = ("order", "id")
    list_editable = ("is_active", "order")


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("title", "greeting", "is_active", "order", "updated_at")
    search_fields = ("title", "greeting", "description")
    list_filter = ("is_active",)
    ordering = ("order", "id")
    list_editable = ("is_active", "order")


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 0
    ordering = ("order", "id")


@admin.register(SkillGroup)
class SkillGroupAdmin(admin.ModelAdmin):
    inlines = [SkillInline]
    list_display = ("title", "is_active", "order", "updated_at")
    search_fields = ("title", "description", "skills__name")
    list_filter = ("is_active",)
    ordering = ("order", "id")
    list_editable = ("is_active", "order")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "group", "icon_name", "is_active", "order")
    search_fields = ("name", "icon_name", "group__title")
    list_filter = ("group", "is_active")
    ordering = ("group__order", "order", "id")
    list_editable = ("is_active", "order")


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("role", "company", "location", "period", "is_active", "order")
    search_fields = ("role", "company", "location", "description")
    list_filter = ("is_active",)
    ordering = ("order", "id")
    list_editable = ("is_active", "order")


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("degree", "school", "location", "period", "is_active", "order")
    search_fields = ("degree", "school", "location", "description")
    list_filter = ("is_active",)
    ordering = ("order", "id")
    list_editable = ("is_active", "order")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_active", "order", "updated_at")
    search_fields = ("title", "category", "description", "details")
    list_filter = ("category", "is_active")
    ordering = ("order", "id")
    list_editable = ("is_active", "order")


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("name", "issuer", "period", "is_active", "order", "updated_at")
    search_fields = ("name", "issuer", "credential", "credential_id", "description")
    list_filter = ("issuer", "is_active")
    ordering = ("order", "id")
    list_editable = ("is_active", "order")


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "label", "author", "date", "is_active", "order")
    search_fields = ("title", "label", "author", "excerpt", "content")
    list_filter = ("label", "is_active")
    ordering = ("order", "id")
    list_editable = ("is_active", "order")


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("title", "email", "is_active", "order", "updated_at")
    search_fields = ("title", "description", "email")
    list_filter = ("is_active",)
    ordering = ("order", "id")
    list_editable = ("is_active", "order")


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ("copyright_text", "design_by_text", "is_active", "order", "updated_at")
    search_fields = ("copyright_text", "design_by_text")
    list_filter = ("is_active",)
    ordering = ("order", "id")
    list_editable = ("is_active", "order")
