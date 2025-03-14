from astral import LocationInfo
from astral.sun import sun
from datetime import datetime, timedelta
import pytz

# Define user inputs
desired_sunrise = "07:00"  # 7:00 AM
desired_sunset = "19:00"  # 7:00 PM
latitude = 40.7128  # Example: New York City
longitude = -74.0060

# Set up location
location = LocationInfo("Custom", "Region", "UTC", latitude, longitude)


# Function to calculate sunrise/sunset for a given day and offset
def get_sun_times(date, offset_hours):
    s = sun(location.observer, date=date, tzinfo=pytz.UTC)
    sunrise = s["sunrise"] + timedelta(hours=offset_hours)
    sunset = s["sunset"] + timedelta(hours=offset_hours)
    return sunrise, sunset


# Convert desired times to datetime objects for comparison
def parse_time(time_str, date):
    return datetime.strptime(f"{date.strftime('%Y-%m-%d')} {time_str}", "%Y-%m-%d %H:%M").replace(tzinfo=pytz.UTC)


# Score function: how much sunlight falls between desired times
def score_offset(offset_hours, year=2025):
    total_sunlight = 0
    date = datetime(year, 1, 1, tzinfo=pytz.UTC)
    for day in range(365):
        current_date = date + timedelta(days=day)
        sunrise, sunset = get_sun_times(current_date, offset_hours)
        desired_start = parse_time(desired_sunrise, current_date)
        desired_end = parse_time(desired_sunset, current_date)

        # Calculate overlap of sunlight with desired window
        sunlight_start = max(sunrise, desired_start)
        sunlight_end = min(sunset, desired_end)
        if sunlight_end > sunlight_start:
            total_sunlight += (sunlight_end - sunlight_start).total_seconds() / 3600  # Hours

    return total_sunlight


# Test a range of offsets
best_offset = None
best_score = -1
for offset in [x / 4 for x in range(-48, 49)]:  # -12 to +12 hours in 15-min increments
    score = score_offset(offset)
    if score > best_score:
        best_score = score
        best_offset = offset

print(f"Best offset: {best_offset:+.2f} hours")
print(f"Total sunlight hours in desired window: {best_score:.1f}")

# Example output for a specific day
sample_date = datetime(2025, 6, 21, tzinfo=pytz.UTC)
sunrise, sunset = get_sun_times(sample_date, best_offset)
print(f"June 21st: Sunrise at {sunrise.strftime('%H:%M')}, Sunset at {sunset.strftime('%H:%M')}")
