# -*- coding: utf-8 -*-
"""
Marzo López Cerón - NAS group - Chemical Physics - Lund University  
August 2024

code for calculating the focal lengths of the necessary lenses for the building of
an optical microscope set-up 

all the lenses are plano-convex and minimum Ø1" 

tube lens + telescope 
"""

import numpy as np 
import os

#INPUT VARIABLES OF THE SET-UP [mm][º]

#sample illumination spot
s_size = 0.015                          #size of the illuminated sample spot (radius)

#objective specs
obj_tube = 48.35                        #length of objective tube
obj_f = 2.87                            #focal length of the objective
obj_ca = 4.7/2                          #clear aperture

#distance constraints 
d_obj_to_tube = 250.0                   #distance from the objective lens to the tube lens
d_tl1_to_tl2 = 250.0                    #distance between the telescope lenses
d_total = 1000.0                        #total length of the set-up from objective lens to slit

#spectrometer slit
spec_slit_size = 12/2                   #size of the spectrometer slit (half)(final image cannot be bigger than that)

#lenses 
lens_tube_f = 0                         #focal length of tube lens 
lens_tl1_bf = 0                         #back focal length of telescope lens 1
lens_tl2_f = 0                          #focal length of telescope lens 2

#input first magnification 
mag_tube = 100.0                        #magnification at the image plane of the tube lens
               



#######################################################################################


#CREATION OF TXT FILE
file_name = "microscope"
file_txt = file_name + ".txt"
file = open(file_txt, "w")

file.write("OPTICAL MICROSCOPE SET-UP SPECIFICATIONS \n \n")
file.write("DISTANCE CONSTRAINTS \n")
file.write("- Distance between objective lens and tube lens: " + str(round(d_obj_to_tube, 4)) + " mm\n")
file.write("- Distance between telescope lenses TL1 and TL2: " + str(round(d_tl1_to_tl2, 4)) + " mm\n" )
file.write("- Total distance of the set-up (from objective lens to spectrometer slit: " + str(d_total) + " mm\n")

file.write("\nSPECTROMETER CONSTRAINTS\n")
file.write("- Spectrometer slit size: " + str(spec_slit_size) + " mm\n")


#OBTAIN  
#first we calculate the theoretical values for the focal lenghts of the three lenses by assuming a size at the spectrometer of 12 mm
#and a magnification after the tube lens of x100
if lens_tube_f == 0 and lens_tl1_bf == 0 and lens_tl2_f == 0: 
    
    file.write("\n#####FOCAL LENGTHS FOR TUBE, TL1 & TL2 CALCULATED BASED ON INPUT VARIABLES#####\n")
    
    #magnifications of the system
    mag_total = spec_slit_size/s_size
    mag_telescope = mag_total/mag_tube
    
    
    file.write("\nMAGNIFICATIONS OF THE SET-UP\n")
    file.write("- Total magnification: x" + str( round(mag_total, 3) ) + "\n") 
    file.write("- Magnification of tube lens: x" + str( round(mag_tube, 3) ) + "\n" ) 
    file.write("- Magnification of telescope: x" + str( round(mag_telescope, 3) ) + "\n" )
    
    print("MAGNIFICATIONS OF THE SET-UP")
    print("Total magnification: x" + str( mag_total ) )
    print("Magnification of tube lens: x" + str( mag_tube ))
    print("Magnification of telescope: x" + str( mag_telescope ))

    
    #theoretical focal length of the tube lens 
    lens_tube_f = mag_tube*obj_f
    
    #image size at the image plane of the tube lens
    image_size_imptube = mag_tube*s_size
    
    file.write("\nTUBE LENS\n")
    file.write("- Focal length: " + str( round(lens_tube_f, 4) ) + " mm\n" )
    file.write("- Image size @ tube lens image plane: " + str( round(image_size_imptube, 4) ) + " mm\n")
    
    #calculation of the focal lengths for the telescope lenses
    lens_tl1_bf = (d_total - d_obj_to_tube - lens_tube_f - d_tl1_to_tl2 )/(mag_telescope + 1)
    lens_tl2_f = mag_telescope*lens_tl1_bf
    
    file.write("\nTELESCOPE\n")
    file.write("- TL1 Back focal length: " + str( round(lens_tl1_bf, 4) ) + " mm\n" )
    file.write("- TL2 Focal length: " + str( round(lens_tl2_f, 4) ) + " mm\n" )
    
    print("\nLENSES")
    print("Tube lens focal length: " + str(lens_tube_f) + " mm")
    print("Image size @ tube lens image plane: " + str(image_size_imptube) + " mm")
    print("TL1 Back focal length: " + str(lens_tl1_bf) + " mm")
    print("TL2 Focal length: " + str(lens_tl2_f) + " mm")
    
    file.write("\nEOF")
    file.close()
    
    #renamig the file for the "obtain" results
    os.rename(file_txt, file_name + "_obtain_ss_" + str(s_size).replace(".", "_") + "_mag1_" + str(mag_tube).replace(".", "_") + "_sls_" + str(spec_slit_size).replace(".", "_") + "_dtot_" + str(d_total).replace(".", "_") + ".txt")

#CHECK 
#when the input focal lengths are number, this block of the codes determines if that lens configuration is suitable for the
#given set-up parameteres and constraints
else: 
    
    file.write("\n#####CHECK IF THE INPUT FOCAL LENGTHS ARE SUITABLE FOR THE SET-UP#####\n")
    file.write("\nTUBE LENS\n")
    file.write("- Focal length: " + str( round(lens_tube_f, 4) ) + " mm\n" )
    file.write("\nTELESCOPE\n")
    file.write("- TL1 Back focal length: " + str( round(lens_tl1_bf, 4) ) + " mm\n" )
    file.write("- TL2 Focal length: " + str( round(lens_tl2_f, 4) ) + " mm\n" )
    
    print("LENSES")
    print("Tube lens focal length: " + str(lens_tube_f) + " mm")
    print("TL1 Back focal length: " + str(lens_tl1_bf) + " mm")
    print("TL2 Focal length: " + str(lens_tl2_f) + " mm")
    
    #check if the distance constraints are fullfiled
    file.write("\n#####DISTANCE CONSTRAINTS#####\n")
    
    #we recalculate the total distance of the set-up with the input focal lenghts
    d_total_calc = d_obj_to_tube + lens_tube_f + lens_tl1_bf + d_tl1_to_tl2 + lens_tl2_f
    
    #and we compare it with the constraint
    if d_total_calc <= d_total:
        file.write("- Total distance: " + str( round(d_total_calc, 4) ) + "mm\n")
        
        #magnifications
        mag_tube = lens_tube_f/obj_f
        mag_telescope = lens_tl2_f/lens_tl1_bf
        mag_total = mag_tube*mag_telescope
        
        file.write("\nCALCULATED MAGNIFICATIONS\n")
        file.write("- Total magnification: x" + str( round(mag_total, 3) ) + "\n") 
        file.write("- Magnification of tube lens: x" + str( round(mag_tube, 3) ) + "\n" ) 
        file.write("- Magnification of telescope: x" + str( round(mag_telescope, 3) ) + "\n" )
        
        print("\nMAGNIFICATIONS OF THE SET-UP")
        print("Total magnification: x" + str( mag_total ) )
        print("Magnification of tube lens: x" + str( mag_tube ))
        print("Magnification of telescope: x" + str( mag_telescope ))


        file.write("\nIMAGE SIZE AFTER TUBE LENS AND AT SLIT\n")
        print("\nIMAGE SIZE AFTER TUBE LENS AND AT SLIT")
        
        #image size at the image plane of the tube lens
        image_size_imptube = mag_tube*s_size
        file.write("- Image size @ tube lens image plane: " + str( round(image_size_imptube, 4) ) + " mm\n")
        print("Image size @ tube lens image plane: " + str(image_size_imptube) + " mm")
        
        #image size at the spectrometer slit for this system of lenses 
        image_size_slit = mag_total*s_size
        file.write("- Image size @ spectrometer slit: " + str( round(image_size_slit, 4) ) + " mm\n" )
        print("Image size @ spectrometer slit: " + str(image_size_slit) + " mm")
        
        #comparisson of the image size at the spectrometer slit with the actual size of the slit
        if image_size_slit <= spec_slit_size:
            file.write("- The image fits the spectrometer slit \n")
            print("The image fits the spectrometer slit")
        elif image_size_slit > spec_slit_size: 
            file.write("- The image is too large for the spectrometer slit \n")
            print("The image is too large for the spectrometer slit")
            
    elif d_total_calc > d_total:
        file.write("- The total distance is too large: " + str( round(d_total_calc, 4) ) + "mm\n" )
        print("The total distance is too large: " + str(d_total_calc) + " mm")
  
    file.write("\nEOF")
    file.close()

    os.rename(file_txt, file_name + "_check_fTUBE_" + str( round(lens_tube_f, 2) ).replace(".", "_") + "_bfTL1_" + str( round(lens_tl1_bf, 2) ).replace(".", "_") + "_fTL2_" + str( round(lens_tl2_f, 2) ).replace(".", "_") + ".txt")    
























































