from rest_framework import serializers

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


class AbsoluteFileFieldMixin:
    def absolute_url(self, value):
        if not value:
            return None
        request = self.context.get("request")
        url = value.url
        return request.build_absolute_uri(url) if request else url


class HeroInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroInfo
        fields = ("id", "label", "value", "is_active", "order")


class HeroStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroStat
        fields = ("id", "value", "label", "is_active", "order")


class EssentialLinkSerializer(serializers.ModelSerializer):
    href = serializers.CharField(source="url")

    class Meta:
        model = EssentialLink
        fields = ("id", "label", "href", "icon", "color", "is_active", "order")


class HeroSerializer(AbsoluteFileFieldMixin, serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    cv_file = serializers.SerializerMethodField()
    info = serializers.SerializerMethodField()
    stats = serializers.SerializerMethodField()
    essential_links = serializers.SerializerMethodField()

    class Meta:
        model = Hero
        fields = (
            "id",
            "name",
            "role",
            "headline_name",
            "headline_role",
            "description",
            "image",
            "cv_file",
            "cv_url",
            "info",
            "stats",
            "essential_links",
            "is_active",
            "order",
        )

    def get_image(self, obj):
        return self.absolute_url(obj.image)

    def get_cv_file(self, obj):
        return self.absolute_url(obj.cv_file)

    def get_info(self, obj):
        qs = obj.info_items.filter(is_active=True).order_by("order", "id")
        return HeroInfoSerializer(qs, many=True, context=self.context).data

    def get_stats(self, obj):
        qs = obj.stats.filter(is_active=True).order_by("order", "id")
        return HeroStatSerializer(qs, many=True, context=self.context).data

    def get_essential_links(self, obj):
        qs = obj.essential_links.filter(is_active=True).order_by("order", "id")
        return EssentialLinkSerializer(qs, many=True, context=self.context).data


class AboutSerializer(AbsoluteFileFieldMixin, serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = About
        fields = ("id", "title", "greeting", "description", "image", "is_active", "order")

    def get_image(self, obj):
        return self.absolute_url(obj.image)


class SkillSerializer(AbsoluteFileFieldMixin, serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Skill
        fields = ("id", "name", "icon_name", "image", "color", "fallback", "is_active", "order")

    def get_image(self, obj):
        return self.absolute_url(obj.icon_image)


class SkillGroupSerializer(serializers.ModelSerializer):
    skills = serializers.SerializerMethodField()

    class Meta:
        model = SkillGroup
        fields = ("id", "title", "description", "skills", "is_active", "order")

    def get_skills(self, obj):
        qs = obj.skills.filter(is_active=True).order_by("order", "id")
        return SkillSerializer(qs, many=True, context=self.context).data


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = (
            "id",
            "role",
            "company",
            "location",
            "period",
            "start_date",
            "end_date",
            "description",
            "tags",
            "is_active",
            "order",
        )


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = (
            "id",
            "degree",
            "school",
            "location",
            "period",
            "start_date",
            "end_date",
            "description",
            "tags",
            "is_active",
            "order",
        )


class ProjectSerializer(AbsoluteFileFieldMixin, serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "category",
            "description",
            "details",
            "image",
            "github_url",
            "live_url",
            "tags",
            "is_active",
            "order",
        )

    def get_image(self, obj):
        return self.absolute_url(obj.image)


class CertificateSerializer(AbsoluteFileFieldMixin, serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Certificate
        fields = (
            "id",
            "name",
            "issuer",
            "credential",
            "credential_id",
            "period",
            "issue_date",
            "image",
            "verify_url",
            "description",
            "tags",
            "is_active",
            "order",
        )

    def get_image(self, obj):
        return self.absolute_url(obj.image)


class BlogSerializer(AbsoluteFileFieldMixin, serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = (
            "id",
            "title",
            "label",
            "author",
            "date",
            "duration",
            "image",
            "excerpt",
            "content",
            "is_active",
            "order",
        )

    def get_image(self, obj):
        return self.absolute_url(obj.image)


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ("id", "title", "description", "email", "is_active", "order")


class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = ("id", "copyright_text", "design_by_text", "design_by_url", "is_active", "order")


class PortfolioSerializer(serializers.Serializer):
    hero = serializers.SerializerMethodField()
    about = serializers.SerializerMethodField()
    skills = serializers.SerializerMethodField()
    experience = serializers.SerializerMethodField()
    education = serializers.SerializerMethodField()
    projects = serializers.SerializerMethodField()
    certificates = serializers.SerializerMethodField()
    blogs = serializers.SerializerMethodField()
    contact = serializers.SerializerMethodField()
    footer = serializers.SerializerMethodField()

    def first_active(self, model):
        return model.objects.filter(is_active=True).order_by("order", "id").first()

    def active_many(self, model):
        return model.objects.filter(is_active=True).order_by("order", "id")

    def get_hero(self, obj):
        hero = self.first_active(Hero)
        return HeroSerializer(hero, context=self.context).data if hero else None

    def get_about(self, obj):
        about = self.first_active(About)
        return AboutSerializer(about, context=self.context).data if about else None

    def get_skills(self, obj):
        groups = self.active_many(SkillGroup)
        return SkillGroupSerializer(groups, many=True, context=self.context).data

    def get_experience(self, obj):
        return ExperienceSerializer(self.active_many(Experience), many=True, context=self.context).data

    def get_education(self, obj):
        return EducationSerializer(self.active_many(Education), many=True, context=self.context).data

    def get_projects(self, obj):
        return ProjectSerializer(self.active_many(Project), many=True, context=self.context).data

    def get_certificates(self, obj):
        return CertificateSerializer(self.active_many(Certificate), many=True, context=self.context).data

    def get_blogs(self, obj):
        return BlogSerializer(self.active_many(Blog), many=True, context=self.context).data

    def get_contact(self, obj):
        contact = self.first_active(Contact)
        return ContactSerializer(contact, context=self.context).data if contact else None

    def get_footer(self, obj):
        footer = self.first_active(Footer)
        return FooterSerializer(footer, context=self.context).data if footer else None
