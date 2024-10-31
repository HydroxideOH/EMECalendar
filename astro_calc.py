import numpy as np
from skyfield.api import load, Topos
import datetime


def get_moon_info(date_str):
    """Calculates the Moon's declination, distance, and Sun offset for a given date.

    Args:
        date_str: A string representing the date in 'YYYY-MM-DD' format.

    Returns:
        A tuple containing the Moon's declination (degrees), distance (km),
        and Sun offset (degrees). Returns None if an error occurs.
    """
    ts = load.timescale()
    year, month, day = map(int, date_str.split('-'))
    t = ts.utc(year, month, day, 0, 0)
    eph = load('de421.bsp')
    sun, moon, earth = eph['sun'], eph['moon'], eph['earth']

    # Moon's position relative to the Earth
    astrometric = earth.at(t).observe(moon)
    ra, dec, distance = astrometric.radec()

    # Sun's position relative to the Earth
    astrometric_sun = earth.at(t).observe(sun)
    ra_sun, dec_sun, distance_sun = astrometric_sun.radec()

    # Calculate sun offset (angular separation between the sun and the moon)
    sun_offset = np.degrees(np.arccos(np.sin(dec.radians) * np.sin(dec_sun.radians) +
                                    np.cos(dec.radians) * np.cos(dec_sun.radians) *
                                    np.cos(ra.radians - ra_sun.radians)))

    return dec.degrees, distance.km, sun_offset



def get_moon_ra_dec(date_str):
    """Get moon's right ascension and declination for galactic noise calculation."""
    ts = load.timescale()
    year, month, day = map(int, date_str.split('-'))
    t = ts.utc(year, month, day,0,0)
    eph = load('de421.bsp')
    sun, moon, earth = eph['sun'], eph['moon'], eph['earth']

    astrometric = earth.at(t).observe(moon)
    ra, dec, distance = astrometric.radec()

    return ra.hours, dec.degrees


def get_moon_noise(date_str, noise_table):
    """Look up to the noise table for galactic noise value."""
    ra, dec = get_moon_ra_dec(date_str)
    dec_size, ra_size = noise_table.shape
    ra_pixel = int((12-ra)*ra_size/24) % ra_size
    dec_pixel = (dec_size-1)//2-int(dec*(dec_size-1)/90)
    return noise_table[dec_pixel, ra_pixel]


def get_pathloss(distance):
    """Calculate path loss in DL7APV moon calendar format."""
    apogee_dist = 356635
    return 0.3-40*np.log10(distance/apogee_dist)


def sunday_dates(year):
    """Generates a list of dates for all Sundays in the given year."""
    sundays = []
    date = datetime.date(year, 1, 1)
    while date.year == year:
        if date.weekday() == 6:  # Sunday is represented by 6
            sundays.append(date.strftime("%Y-%m-%d"))
        date += datetime.timedelta(days=1)
    return sundays

