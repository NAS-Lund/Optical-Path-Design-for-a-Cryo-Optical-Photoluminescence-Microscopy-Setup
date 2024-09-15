# -*- coding: utf-8 -*-
"""
Marzo López Cerón - NAS group - Chemical Physics - Lund University  
July 2024

code for obtaining the focal lengths of the lenses needed to illuminate
the sample with the light coming from the fiber coupled to the diode laser

the focusing lens is plano-convex and minimum Ø1" 

one-lens configuration
"""

import numpy as np 
import os

#INPUT VARIABLES OF THE SET-UP [mm][º]

#sample illumination spot
s_size = 0.015                  #size of the illuminated sample spot (radius)

#optical fiber parameters 
fib_r_core = 0.00225            #radius of the fiber core
fib_na = 0.13                   #numerical aperture of the fiber
fib_type = "SM"                 #type of fiber multimode (MM)/single mode (SM)

#collimator specs
coll_f = 4.6                    #focal length of the collimator
coll_mount = 6.4                #minimum distance from end of collimator to TL1
coll_theta_measured = 0         #measured divergence angle (in degrees)
divergence_angle = "theo"       #option to use experimental or theoretical divergence angle

#objective specs
obj_tube = 48.35                #length of objective tube
obj_f = 2.87                    #focal length of the objective
obj_ca = 4.7/2                  #clear aperture


#more distance constraints 
d_fpoint_to_objlens = 60        #distance from the focal point of L1 until objective lens (f''+obj_f)
d_l1_to_objlens = 210           #distance from the objective lens until L1 (min distance at which the first optics can be place wrt objective lens)

#lens
l1_f = 150                   #focal length of the L1 lens (l1_f = 0 for calcu)



##########################################################################################################################
 

#STEPS 

#STEP 1
#STEP 1.1: create a .txt file with the specifications of the lens and its placement wrt collimator mount
fib_diam_microm = str((fib_r_core*2)*1e3).replace(".", "_")
fib_na_str = str(fib_na).replace(".", "_")
file_name = "excitation_" 
file_txt = file_name + ".txt"

file = open(file_txt, "w")
 
file.write("SPECIFICATIONS ONE-LENS CONFIGURATION \n \n")
file.write("FIBER SPECIFICATIONS \n")
file.write(fib_type + " optical fiber Ø" + str((fib_r_core*2)*1e3) + "µm " + str(fib_na) + "NA \n \n")  
 

#STEP 1.2: divergence angle of the light coming out of the collimator
file.write("BEAM AFTER COLLIMATOR \n")
print("BEAM AFTER COLLIMATOR:")

if divergence_angle == "exp":
    coll_theta_div = coll_theta_measured*(np.pi/180) 
    print("Experimentally measured divergence angle: " + str(coll_theta_div*(180/np.pi)) + " deg")
    
    file.write("- Experimentally measured divergence angle: " + str(round(coll_theta_div*(180/np.pi), 4)) + " deg \n")
    
    
elif divergence_angle == "theo":
    coll_theta_div = (fib_r_core/coll_f) #*(180/np.pi)
    print("Theoretical divergence angle: " + str(coll_theta_div*(180/np.pi)) + " deg")

    file.write("- Theoretical divergence angle: " + str(round(coll_theta_div*(180/np.pi), 4)) + " deg \n")
    
    
#size of the collimated beam after the collimator assuming perfect collimation
beam_r_coll = coll_f*fib_na 
file.write("- Size of the collimated beam: " + str(round(beam_r_coll, 4)) + " mm \n")

#increase in the size of the collimated beam per mm [mm/mm] : not used in calculations, but it is nice to have as reference
incr_beam_r_coll = np.tan(coll_theta_div) 
file.write("- Increase in radius of the collimated beam per mm: " + str(round(incr_beam_r_coll, 4)) + " mm \n")


#STEP 2 
#Constraints 

#f'' on the sketches' notation. Distance from the focal point of L1 to the obj_f before the objective lens
d_fpp = d_fpoint_to_objlens - obj_f

#f': displacement of the focal point of the obj wrt focal plane: lens equation constraint
d_fp = ((obj_f)**2)/d_fpp 

#minimal focal length for L1 according to the constraints
l1_min_f = d_l1_to_objlens-d_fpp-obj_f


#STEP 3 

#STEP 3.1.1: calculate focal length of L1 (OBTAIN)
if l1_f == 0:  
    
    file.write("\n########FOCAL LENGTH FOR L1 IS CALCULATED BASED ON INPUT VARIABLES########\n")
    
    #Size of beam at objective lens
    file.write("\nBEAM AT OBJECTIVE LENS\n")
    print("\nBEAM AT OBJECTIVE LENS:")
    
    obj_y = (s_size*(obj_f+d_fp))/d_fp
    
    file.write("- Size of beam at objective: " + str(round(obj_y, 4)) + " mm \n" )    

    #comparisson with the objective's numerical aperture
    if obj_y > obj_ca: 
        print("Image size does not fit clear aperture of objective")
    
        file.write("- Image size does not fit clear aperture of objective by " + str(obj_y-obj_ca) + " mm \n")

    else: 
        print("Image size fits clear aperture")
        
        file.write("- Image size fits clear aperture of objective \n")

   
    #calculate angle with respect to optic axis after focus
    d = obj_f+d_fpp
    tan_phi = np.tan(obj_y/d)
    

    file.write("\nLENS SPECIFICATIONS\n")
    print("\nLENS SPECIFICATIONS:")
    
    #calculate focal length of L1
    l1_f = beam_r_coll/tan_phi #consider collimated beam 
    
    #apply constraints and compare with the minimal result coming from the constraints
    dd = l1_f + obj_f + d_fpp
    
    if dd >= d_l1_to_objlens:
        print("Focal length of L1 fits the criteria")
        print("Calculated focal length: " + str(l1_f) + " mm")
        
        file.write("- Calculated focal length for L1: " + str(round(l1_f,4)) + " mm \n")
        
    elif dd < d_l1_to_objlens: 
        print("Focal length of L1 is too short")
        print("Calculated focal length: " + str(l1_f) + " mm")
        print("Needs to be at least " + str(l1_min_f))
        
        file.write("- Focal length of L1 is too short \n")
        file.write("    - Calculated focal length: " + str(round(l1_f, 4)) + " mm \n")
        file.write("    - Needs to be at least: " + str(round(l1_min_f, 4)) + " mm \n")
        
    file.write("\nEOF")
    file.close()
    
    new_file_name = file_name + "obtain_"  + fib_type + "_core_" + fib_diam_microm + "_NA_" + fib_na_str + "_f" + str(round(l1_f, 3)).replace(".", "_") + ".txt"
    
    if os.path.exists(new_file_name):
        os.remove(new_file_name)
    
    os.rename(file_txt,  new_file_name)
    
    
    
#STEP 3.1.2: reverse calculations to check if a chosen focal length is suitable for the set-up (CHECK)
elif l1_f != 0: 

    file.write("\n########CHECK IF INPUT FOCAL LENGTH IS SUITABLE FOR THE SPECIFIED SET-UP########\n")
   
    
   #check if the input focal length fullfils the min focal length calculated  
    if l1_f >= l1_min_f:
        print("Focal length of L1 fits the criteria")
        print("Input focal length: " + str(l1_f) + " mm")
        
        file.write("\nLENS SPECIFICATIONS\n")
        print("\nLENS SPECIFICATIONS:")
        
        file.write("- Calculated minimum focal length: " + str(round(l1_min_f, 4)) + " mm \n")
        file.write("- Input focal length: " + str(round(l1_f, 4)) + " mm \n")
        
        #angle wrt optic axis
        tan_phi = beam_r_coll/l1_f
        
        #size of the beam at obj lens (must not exceed obj clear aperture)
        file.write("\nBEAM AT OBJECTIVE LENS\n")
        print("\nBEAM AT OBJECTIVE LENS:")
        
        obj_y = d*tan_phi
        if obj_y > obj_ca: 
            print("Image size does not fit numerical aperture of objective")
            
            file.write("- Image size does not fit clear aperture of objective by " + str(obj_y-obj_ca) + " mm \n")
            
        else: 
            print("Image size fits numerical aperture")
            
            file.write("- Image size fits clear aperture of objective \n")
            
        #sample illumination spot must be a certain size (no bigger than s_size input)
        file.write("\nILLUMINATION SPOT\n")
        print("\nILLUMINATION SPOT:")
        
        ss_size = (d_fp*obj_y)/(obj_f+d_fp)
        file.write("- Maximum size for the sample illumination spot: " + str(s_size*1e3) + " µm \n")
        if ss_size <= s_size:
            print("The sample illumination spot is small enough: " + str(ss_size*1e3) + " micro m")
            
            file.write("    - The sample illumination spot is small enough: " + str(round(ss_size*1e3, 4)) + " µm \n")
            
        elif ss_size > s_size:
            print("The sample illumination spot is NOT small enough: " + str(ss_size*1e3) + " micro m")
            
            file.write("    - The sample illumination spot is NOT small enough: " + str(round(ss_size*1e3, 4)) + " µm \n")
            
            
    elif l1_f < l1_min_f: 
        file.write("\nLENS SPECIFICATIONS\n")
        print("\nLENS SPECIFICATIONS:")
        
        print("Focal length of L1 is too short")
        print("Input focal length: " + str(l1_f) + " mm")
        print("Calculated minimum focal length: " + str(l1_min_f) + " mm" )
        
        file.write("- Focal length of L1 is too short \n")
        file.write("    - Calculated minimum focal length: " + str(round(l1_min_f, 4)) + " mm\n")
        file.write("    - Input focal length: " + str(round(l1_f, 4)) + " mm\n")

        
    file.write("\nEOF")
    file.close()
    
    
    new_file_name = file_name + "check_"  + fib_type + "_core_" + fib_diam_microm + "_NA_" + fib_na_str + "_f" + str(round(l1_f, 3)).replace(".", "_") + ".txt"
    
    if os.path.exists(new_file_name):
        os.remove(new_file_name)

    os.rename(file_txt, new_file_name)

    
    










