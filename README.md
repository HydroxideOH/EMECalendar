# EMECalendar
An annual moon data generator in the format of [DL7APV moon calendar](http://dl7apv.de/moon2010/moon2010.htm) for ham radio Earth-Moon-Earth (EME) communication planning, recreated by BI1QGX.

Thanks DL7APV(SK) for the original idea and all the effort to publish the calendars every year during his lifetime. The calendars are very reliable and intuitive, and helped me a lot when I was planning my first EME attempt. However, Bernd has passed away and is no longer able to update his website. That's why I made this project. 

Thanks VK3UM(SK) for the sky noise data, and also the great softwares which is still used by the whole EME community including myself.


## Required packages:
numpy>=2.1.2

skyfield>=1.49

## Usage:
Simply change the YEAR variable in main.py to your desired year and run the script!

If you need more accurate sky noise estimation which may differs from the original DL7APV calendar, change the noise table filename as instructed.

## Data Source
The 400MHz sky noise table is a slightly modified version of the VK3UMSkyData.dat in the [VK3UM EME planner](https://www.vk5dj.com/doug.html). The 432MHz one is roughly adjusted for 432MHz using the frequency-temperature relationship estimation described in the paper [A model of the radio-frequency radiation from the galaxy](https://www.tandfonline.com/doi/abs/10.1080/14786440908521063).
