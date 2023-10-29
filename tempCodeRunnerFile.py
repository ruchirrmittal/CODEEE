from datetime import datetime, timezone
try:
    import zoneinfo
except ImportError:
    from backports import zoneinfo

zones=(
    'Europe/Paris',
    'Europe/London',
    'Asia/Hong_Kong',
    'Africa/Nairobi'
)

utc_now=datetime.now(tz=timezone.utc)

for zone in zones:
    tz=zoneinfo.ZoneInfo(zone)
    required=datetime.now(tz=tz)
    # required=utc_now.astimezone(tz)
    city=zone.split('/')[-1]
    print(f'The time in {city} is {required}')