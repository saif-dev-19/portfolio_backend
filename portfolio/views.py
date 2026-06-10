from rest_framework import permissions, response, views, viewsets

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
from .serializers import (
    AboutSerializer,
    BlogSerializer,
    CertificateSerializer,
    ContactSerializer,
    EducationSerializer,
    EssentialLinkSerializer,
    ExperienceSerializer,
    FooterSerializer,
    HeroInfoSerializer,
    HeroSerializer,
    HeroStatSerializer,
    PortfolioSerializer,
    ProjectSerializer,
    SkillGroupSerializer,
    SkillSerializer,
)


# class PublicPortfolioView(views.APIView):
#     permission_classes = [permissions.AllowAny]

#     def get(self, request):
#         serializer = PortfolioSerializer({}, context={"request": request})
#         return response.Response(serializer.data)


class PublicPortfolioView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        serializer = PortfolioSerializer(instance=None, context={"request": request})
        return response.Response(serializer.data)

class AdminOnlyViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]


class HeroViewSet(AdminOnlyViewSet):
    queryset = Hero.objects.all().order_by("order", "id")
    serializer_class = HeroSerializer


class HeroInfoViewSet(AdminOnlyViewSet):
    queryset = HeroInfo.objects.select_related("hero").all().order_by("hero__order", "order", "id")
    serializer_class = HeroInfoSerializer


class HeroStatViewSet(AdminOnlyViewSet):
    queryset = HeroStat.objects.select_related("hero").all().order_by("hero__order", "order", "id")
    serializer_class = HeroStatSerializer


class EssentialLinkViewSet(AdminOnlyViewSet):
    queryset = EssentialLink.objects.select_related("hero").all().order_by("hero__order", "order", "id")
    serializer_class = EssentialLinkSerializer


class AboutViewSet(AdminOnlyViewSet):
    queryset = About.objects.all().order_by("order", "id")
    serializer_class = AboutSerializer


class SkillGroupViewSet(AdminOnlyViewSet):
    queryset = SkillGroup.objects.prefetch_related("skills").all().order_by("order", "id")
    serializer_class = SkillGroupSerializer


class SkillViewSet(AdminOnlyViewSet):
    queryset = Skill.objects.select_related("group").all().order_by("group__order", "order", "id")
    serializer_class = SkillSerializer


class ExperienceViewSet(AdminOnlyViewSet):
    queryset = Experience.objects.all().order_by("order", "id")
    serializer_class = ExperienceSerializer


class EducationViewSet(AdminOnlyViewSet):
    queryset = Education.objects.all().order_by("order", "id")
    serializer_class = EducationSerializer


class ProjectViewSet(AdminOnlyViewSet):
    queryset = Project.objects.all().order_by("order", "id")
    serializer_class = ProjectSerializer


class CertificateViewSet(AdminOnlyViewSet):
    queryset = Certificate.objects.all().order_by("order", "id")
    serializer_class = CertificateSerializer


class BlogViewSet(AdminOnlyViewSet):
    queryset = Blog.objects.all().order_by("order", "id")
    serializer_class = BlogSerializer


class ContactViewSet(AdminOnlyViewSet):
    queryset = Contact.objects.all().order_by("order", "id")
    serializer_class = ContactSerializer


class FooterViewSet(AdminOnlyViewSet):
    queryset = Footer.objects.all().order_by("order", "id")
    serializer_class = FooterSerializer
