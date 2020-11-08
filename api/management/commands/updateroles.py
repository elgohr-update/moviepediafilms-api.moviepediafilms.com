from django.core.management.base import BaseCommand
from api.models import CrewMember, Profile
from api.constants import MOVIE_STATE
from logging import getLogger

logger = getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        for cm in CrewMember.objects.filter(movie__state=MOVIE_STATE.PUBLISHED):
            if cm.role not in cm.profile.roles.all():
                logger.info(f"{cm.profile} is {cm.role.name}")
                cm.profile.roles.add(cm.role)
                cm.profile.save()
