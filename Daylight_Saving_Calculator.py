from astral import LocationInfo
from astral.sun import sun
from datetime import datetime, timedelta
from timezonefinder import TimezoneFinder
import pytz

# Define user inputs
desired_sunrise = "06:00"  # 6:00 AM
desired_sunset = "19:15"  # 7:15 PM
latitude = 42.3555  # Example: Boston
longitude = -71.0565

# Set up location
location = LocationInfo("Custom", "Region", "UTC", latitude, longitude)

# Print initial user inputs
print("\n------------------------------\n")
print(f"Desired Sunrise Time: {desired_sunrise}")
print(f"Desired Sunset Time: {desired_sunset}")
print(f"Location: Latitude {latitude}, Longitude {longitude}")
print("\n---\n")

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
def score_offset(offset_hours, year=datetime.now().year):
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


# Function to get current UTC offset for a location
def get_current_offset(lat, lon, date):
    tf = TimezoneFinder()
    timezone_str = tf.timezone_at(lat=lat, lng=lon)
    if timezone_str is None:
        return None  # No timezone found for this location
    timezone = pytz.timezone(timezone_str)
    # Make the date naive (remove UTC timezone) before localizing
    naive_date = date.replace(tzinfo=None)
    # Localize to the found timezone
    local_date = timezone.localize(naive_date)
    # Get UTC offset in hours
    utc_offset = local_date.utcoffset().total_seconds() / 3600
    return utc_offset, timezone_str


# Get current date and year
current_date = datetime.now(pytz.UTC)
current_year = current_date.year

# Test a range of offsets
best_offset = None
best_score = -1
for offset in [x / 4 for x in range(-48, 49)]:  # -12 to +12 hours in 15-min increments
    score = score_offset(offset, current_year)
    if score > best_score:
        best_score = score
        best_offset = offset

# Get current offset for the location
current_offset_info = get_current_offset(latitude, longitude, current_date)
if current_offset_info:
    current_offset, timezone_name = current_offset_info
else:
    current_offset = None
    timezone_name = "Unknown"

# Print results
print(f"Best offset: {best_offset:+.2f} hours")
print(f"Total sunlight hours in desired window: {best_score:.1f}")
if current_offset is not None:
    print(f"Current offset ({timezone_name}): {current_offset:+.2f} hours")
    offset_difference = best_offset - current_offset
    print(f"Difference (Best - Current): {offset_difference:+.2f} hours")
else:
    print("Current offset: Could not determine timezone for this location")

print("\n---\n")

# Define key dates for output
summer_solstice = datetime(current_year, 6, 21, tzinfo=pytz.UTC)  # Approx. summer solstice
winter_solstice = datetime(current_year, 12, 21, tzinfo=pytz.UTC)  # Approx. winter solstice

# Calculate and print sunrise/sunset for key dates
for key_date in [winter_solstice, summer_solstice, current_date]:
    sunrise, sunset = get_sun_times(key_date, best_offset)
    date_str = key_date.strftime('%B %d, %Y')
    sunrise_str = sunrise.strftime('%H:%M')
    sunset_str = sunset.strftime('%H:%M')
    print(f"{date_str}: Sunrise at {sunrise_str}, Sunset at {sunset_str}")

# Create buffer in terminal
print("\n------------------------------\n")
