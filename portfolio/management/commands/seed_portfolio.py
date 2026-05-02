from django.core.management.base import BaseCommand

from portfolio.models import (
    About,
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


class Command(BaseCommand):
    help = "Create starter portfolio content without duplicating existing records."

    def handle(self, *args, **options):
        hero, _ = Hero.objects.get_or_create(
            order=1,
            defaults={
                "name": "Mahfuzur Rahman Saif",
                "role": "Backend Developer",
                "headline_name": "Mahfuz",
                "headline_role": "Backend Developer",
                "description": "I build scalable backend systems and useful web experiences.",
                "cv_url": "#contact",
            },
        )

        for order, (label, value) in enumerate(
            [
                ("Email", "mahfujurrahmansaif@gmail.com"),
                ("Location", "Bangladesh"),
                ("Work", "Onsite"),
                ("Link", "www.mahfuz.live"),
            ],
            start=1,
        ):
            HeroInfo.objects.get_or_create(hero=hero, label=label, defaults={"value": value, "order": order})

        for order, (value, label) in enumerate(
            [("4", "Programming language"), ("6", "Development tools"), ("8", "Years of experience")],
            start=1,
        ):
            HeroStat.objects.get_or_create(hero=hero, label=label, defaults={"value": value, "order": order})

        for order, (label, icon, color) in enumerate(
            [
                ("GitHub", "github", "#181717"),
                ("LinkedIn", "linkedin", "#0A66C2"),
                ("LeetCode", "leetcode", "#FFA116"),
                ("Codeforces", "codeforces", "#1F8ACB"),
            ],
            start=1,
        ):
            EssentialLink.objects.get_or_create(hero=hero, label=label, defaults={"icon": icon, "color": color, "order": order})

        About.objects.get_or_create(
            order=1,
            defaults={
                "title": "About Me",
                "greeting": "Hello!",
                "description": "My name is Mahfuzur Rahman Saif. I specialize in backend development and scalable web systems.",
            },
        )

        tech_group, _ = SkillGroup.objects.get_or_create(title="Technologies I Use", defaults={"order": 1})
        tools_group, _ = SkillGroup.objects.get_or_create(title="Development & Productivity Tools I Use", defaults={"order": 2})

        tech_skills = [
            ("C", "c", "#A8B9CC", ""),
            ("C++", "cplusplus", "#00599C", ""),
            ("Python", "python", "#3776AB", ""),
            ("Dart", "dart", "#0175C2", ""),
            ("Django", "django", "#092E20", ""),
            ("Django REST Framework", "django", "#A30000", ""),
            ("JWT", "jsonwebtokens", "#D63AFF", ""),
            ("Redis", "redis", "#DC382D", ""),
            ("Docker", "docker", "#2496ED", ""),
            ("Celery", "celery", "#37814A", ""),
            ("WebSocket", "", "#12F7D6", "WS"),
            ("React", "react", "#61DAFB", ""),
            ("JavaScript", "javascript", "#F7DF1E", ""),
            ("HTML/CSS", "html5", "#E34F26", ""),
            ("TailwindCSS", "tailwindcss", "#38BDF8", ""),
            ("PostgreSQL", "postgresql", "#4169E1", ""),
            ("MySQL", "mysql", "#4479A1", ""),
            ("SQLite", "sqlite", "#003B57", ""),
            ("Supabase", "supabase", "#3ECF8E", ""),
        ]
        tools_skills = [
            ("Git", "git", "#F05032", ""),
            ("GitHub", "github", "#181717", ""),
            ("Vercel", "vercel", "#000000", ""),
            ("Render", "render", "#46E3B7", ""),
            ("Netlify", "netlify", "#00C7B7", ""),
            ("Prompt Engineering", "openai", "#12F7D6", ""),
            ("ChatGPT", "openai", "#10A37F", ""),
            ("GitHub Copilot", "githubcopilot", "#6E40C9", ""),
            ("Gemini CLI", "googlegemini", "#4285F4", ""),
            ("Cursor", "cursor", "#FFFFFF", ""),
        ]

        self.create_skills(tech_group, tech_skills)
        self.create_skills(tools_group, tools_skills)

        Experience.objects.get_or_create(
            role="Python Developer",
            company="Softvence Agency",
            defaults={
                "period": "5 Jan 2026 - Present",
                "location": "Onsite",
                "description": "Building backend systems with Python, Django, REST APIs, Docker, PostgreSQL, and Redis.",
                "tags": ["Python", "Django", "Rest API", "Docker", "PostgreSQL", "Redis"],
                "order": 1,
            },
        )

        Education.objects.get_or_create(
            degree="Computer Science",
            school="Anadolu University",
            defaults={
                "period": "2015 - 2019",
                "location": "Turkey",
                "description": "Focused on software fundamentals, database systems, web technologies, and practical problem solving.",
                "tags": ["Algorithms", "Databases", "Web"],
                "order": 1,
            },
        )

        Project.objects.get_or_create(
            title="Portfolio Website",
            defaults={
                "category": "Personal Brand",
                "description": "A responsive developer portfolio with dark styling, reusable sections, and contact flow.",
                "details": "A full portfolio website connected to a Django backend CMS.",
                "tags": ["React", "Tailwind", "Django"],
                "order": 1,
            },
        )

        Certificate.objects.get_or_create(
            name="Responsive Web Design",
            defaults={
                "issuer": "freeCodeCamp",
                "credential": "Certificate",
                "credential_id": "FCC-RWD-2023",
                "period": "2023",
                "issue_date": "2023",
                "description": "Completed semantic HTML, responsive layouts, accessibility basics, and CSS fundamentals.",
                "tags": ["HTML", "CSS", "Responsive"],
                "order": 1,
            },
        )

        Contact.objects.get_or_create(
            order=1,
            defaults={
                "title": "Contact",
                "description": "I'm currently available for work",
                "email": "mahfujurrahmansaif@gmail.com",
            },
        )

        Footer.objects.get_or_create(
            order=1,
            defaults={
                "copyright_text": "© 2025 Mahfuz Saif. All rights reserved.",
                "design_by_text": "mahfuz",
                "design_by_url": "https://www.facebook.com/hey.mahfuz.here.ok",
            },
        )

        self.stdout.write(self.style.SUCCESS("Portfolio starter content is ready."))

    def create_skills(self, group, skills):
        for order, (name, icon_name, color, fallback) in enumerate(skills, start=1):
            Skill.objects.get_or_create(
                group=group,
                name=name,
                defaults={
                    "icon_name": icon_name,
                    "color": color,
                    "fallback": fallback,
                    "order": order,
                },
            )
