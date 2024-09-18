-----CODE FOR CALCULATING AND CHECKING FOCAL LENGTHS----- 
--------FOR A ONE-LENS EXCITATION LIGHTPATH SET-UP------- 

Marzo López Cerón, Lund University



---------------------------------------------------------



SOFTWARE INFORMATION: 
	- Python v3.8.10 on Spyder v5.5.5


BEFORE RUNNING THE CODE: 
	- Select directory to save the generated .txt files


NOTES:
	- The code considers perfectly collimated rays coming out of the collimator for the 	calculations. This means that the lens L1 whose focal length is calculated can be placed 	at any distance from it. However, there will always be a small divergence angle for the 	rays out of the collimator, which is also calculated for information. The lens then 	should be placed as close to the collimator as possible. 

	- The numbers in the generated .txt files are rounded up to 4 decimals. This can be 	changed in the code.
	
	- The lens whose focal length is calculated in the code is assumed to be a plano-convex 	lens with a coating suitable for the excitation wavelength.

	- The calculations are made taking the radius of the illumination spot (sample size).

-----------------------------------------------------------



THE CODE:

	- The code either calculates a suitable focal length for the lens of the set-up or checks if a particular focal length is valid. Different variables must be input in order to do so. All of them are explained in the variables_1lens.txt file. The code will generate a .txt file when running. 

	1) Calculate focal length 
	(l1_f = 0)

	This block of the code runs when the input focal length is 0. 
	The code will generate a .txt file with a calculated focal length and information about 	the constraints and the selected optical fiber. 

	Generated file: excitation_obtain_(SM/MM)_core_xx_NA_xx_fxx.txt
	The diameter of the core fiber is expressed in micrometers.

	2) Check focal length 
	(l1_f = xx)
 
	This block of the code runs when a number is input for the focal length variable. 	The code will generate a .txt file with information of whether or not the input focal 	length is suitable for the indicated set up. The file will also provide information of 	why/why not it is suitable and the parameters this is based on. 

	Generated file: excitation_check_type.of.fiber(SM/MM)_core_xx(μm)_NA_xx_fxx.txt






