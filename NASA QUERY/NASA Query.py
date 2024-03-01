# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 19:27:51 2022

@author: julsi
"""

import os


import astropy.units as u
from astropy.time import Time
import sunpy.coordinates  # NOQA

from sunpy.net import Fido
from sunpy.net import attrs as a
import shutil




start_time = Time('2014-06-09T11:00:00', scale='utc', format='isot')
#bottom_left = SkyCoord(-500*u.arcsec, -275*u.arcsec, obstime=start_time, observer="earth", frame="helioprojective")
#top_right = SkyCoord(150*u.arcsec, 375*u.arcsec, obstime=start_time, observer="earth", frame="helioprojective")



#cutout = a.jsoc.Cutout(bottom_left, top_right=top_right, tracking=True)



jsoc_email = ''



query = Fido.search(
    a.Time(start_time - 3*u.h, start_time + 3*u.h),
    a.Wavelength(1600*u.angstrom),
    a.Sample(24*u.s),
    a.jsoc.Series.aia_lev1_uv_24s,
    a.jsoc.Notify(""), #email goes here
    a.jsoc.Segment.image,
    #cutout,
)
print(query)



files = Fido.fetch(query)
files.sort()


source = r"C:\Users"
destination = r"D:"

allfiles = os.listdir(source)

for f in allfiles:

    shutil.move(source+ r"\\" + f, destination)


