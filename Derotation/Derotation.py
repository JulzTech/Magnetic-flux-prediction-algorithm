# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 17:04:54 2023

@author: JulzTech
"""



import astropy.units as u
from astropy.coordinates import SkyCoord
from astropy.time import Time
import sunpy.coordinates  # NOQA
import sunpy.map
from aiapy.calibrate import normalize_exposure, register, update_pointing
import glob 
from sunpy.coordinates import Helioprojective, propagate_with_solar_surface
from astropy.wcs import WCS

import pdb

from sunkit_image.coalignment import mapsequence_coalign_by_match_template as mc_coalign


import time

start = time.time()




start_time = Time('2014-06-12T16:56:00', scale='utc', format='isot')


files =glob.glob('D:/')
files.sort()
print(files)





maps = []

outwarp= []



for i in files:
    
    m = sunpy.map.Map([i])
    
    
    
    
    updated_map = update_pointing(m)
    registered_map = register(updated_map)
    normalized_map = normalize_exposure(registered_map)
    
    
    in_time = start_time
    out_time =  in_time
    out_frame = Helioprojective(observer='earth', obstime=out_time,
                                rsun=normalized_map.coordinate_frame.rsun)
    print(normalized_map)

    out_center = SkyCoord(0*u.arcsec, 0*u.arcsec, frame=out_frame)
    header = sunpy.map.make_fitswcs_header(normalized_map.data.shape,
                                          out_center,
                                           scale=u.Quantity(normalized_map.scale))
    out_wcs = WCS(header)
    with propagate_with_solar_surface():
        out_warp = normalized_map.reproject_to(out_wcs)
        
   
    top_right = SkyCoord(200 * u.arcsec, 500 * u.arcsec, frame=out_warp.coordinate_frame)
    bottom_left = SkyCoord(-400 * u.arcsec, 0 * u.arcsec, frame=out_warp.coordinate_frame)
    aiasubmap = out_warp.submap(bottom_left, top_right=top_right)
    
    outwarp.append(aiasubmap)
    pdb.set_trace()
    

    
    
    

#outwarp[0].peek()




maparray = sunpy.map.Map(outwarp, sequence=True)







coaligned_mc = mc_coalign(maparray)




coaligned_mc.save('C:/Users/.../map_{index:0000}.fits')

end = time.time()
print(end - start)



