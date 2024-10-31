from astro_calc import get_moon_info, get_pathloss, get_moon_noise, sunday_dates
import numpy as np

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    """
    By default, the 400MHz noise table is used, like the original DL7APV moon calendar
    Change to VK3UM_noise_432.npy if you need noise temperature corrected for 432MHz
    """
    noise_table = np.load('./data/VK3UM_noise_400.npy')
    # noise_table = np.load('./data/VK3UM_noise_400.npy')
    YEAR = 2026  # change to your desired year
    with open(f'EME_Calender_{YEAR}.csv', 'w') as f:
        f.write('date,declination,pathloss,sun_offset,noise\n')
        for date in sunday_dates(YEAR):
            declination, distance, sun_offset = get_moon_info(date)
            pathloss = -get_pathloss(distance)
            noise = get_moon_noise(date, noise_table)
            f.write(','.join([date, f'{declination:.1f}', f'{pathloss:.2f}', f'{sun_offset:.0f}', f'{noise}']) + '\n')
