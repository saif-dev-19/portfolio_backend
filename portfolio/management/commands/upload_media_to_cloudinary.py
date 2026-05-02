from pathlib import Path

import cloudinary.uploader
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Upload existing local media files to Cloudinary using their current relative paths."

    def add_arguments(self, parser):
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Show what would be uploaded without sending files to Cloudinary.",
        )

    def handle(self, *args, **options):
        if not getattr(settings, "CLOUDINARY_URL", None):
            raise CommandError("CLOUDINARY_URL is not set.")

        media_root = Path(settings.MEDIA_ROOT)
        if not media_root.exists():
            raise CommandError(f"Media folder does not exist: {media_root}")

        files = [path for path in media_root.rglob("*") if path.is_file()]
        if not files:
            self.stdout.write(self.style.WARNING("No media files found."))
            return

        for path in files:
            relative_path = path.relative_to(media_root).as_posix()
            public_id = str(Path(relative_path).with_suffix("")).replace("\\", "/")

            if options["dry_run"]:
                self.stdout.write(f"Would upload {relative_path} -> {public_id}")
                continue

            cloudinary.uploader.upload(
                str(path),
                public_id=public_id,
                resource_type="auto",
                overwrite=True,
            )
            self.stdout.write(self.style.SUCCESS(f"Uploaded {relative_path}"))

        self.stdout.write(self.style.SUCCESS("Media upload complete."))
