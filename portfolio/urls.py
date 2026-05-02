from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    AboutViewSet,
    BlogViewSet,
    CertificateViewSet,
    ContactViewSet,
    EducationViewSet,
    EssentialLinkViewSet,
    ExperienceViewSet,
    FooterViewSet,
    HeroInfoViewSet,
    HeroStatViewSet,
    HeroViewSet,
    ProjectViewSet,
    PublicPortfolioView,
    SkillGroupViewSet,
    SkillViewSet,
)

router = DefaultRouter()
router.register("admin/hero", HeroViewSet, basename="admin-hero")
router.register("admin/hero-info", HeroInfoViewSet, basename="admin-hero-info")
router.register("admin/hero-stats", HeroStatViewSet, basename="admin-hero-stats")
router.register("admin/essential-links", EssentialLinkViewSet, basename="admin-essential-links")
router.register("admin/about", AboutViewSet, basename="admin-about")
router.register("admin/skill-groups", SkillGroupViewSet, basename="admin-skill-groups")
router.register("admin/skills", SkillViewSet, basename="admin-skills")
router.register("admin/experience", ExperienceViewSet, basename="admin-experience")
router.register("admin/education", EducationViewSet, basename="admin-education")
router.register("admin/projects", ProjectViewSet, basename="admin-projects")
router.register("admin/certificates", CertificateViewSet, basename="admin-certificates")
router.register("admin/blogs", BlogViewSet, basename="admin-blogs")
router.register("admin/contact", ContactViewSet, basename="admin-contact")
router.register("admin/footer", FooterViewSet, basename="admin-footer")

urlpatterns = [
    path("", PublicPortfolioView.as_view(), name="portfolio"),
]

urlpatterns += router.urls
