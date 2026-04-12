from typing import Optional
from django.utils import timezone


def make_naive(dt: Optional[timezone.datetime]) -> Optional[timezone.datetime]:
    if dt and timezone.is_aware(dt):
        return timezone.make_naive(dt, timezone.get_current_timezone())
    return dt
