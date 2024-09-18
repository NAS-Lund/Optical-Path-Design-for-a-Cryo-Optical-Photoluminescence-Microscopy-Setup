-----CODE FOR CALCULATING AND CHECKING FOCAL LENGTHS-----
---FOR AN INFINITE-CORRECTED OPTICAL MICROSCOPE SET-UP---

	Marzo López Cerón, Lund University

---------------------------------------------------------


SOFTWARE INFORMATION: 
	- Python v3.8.10 on Spyder v5.5.5


BEFORE RUNNING: 
	- Select directory to save the generated .txt files


NOTES:
	- The code considers perfectly collimated rays coming from the objective and into the tube lens.
	
	- All the lenses whose focal lengths are calculated are considered to be plano-convex lenses with coatings corresponding to the wavelength of the photoluminescence. 
		
	- The numbers in the generated .txt files are rounded up to 4 decimals. This can be changed in the code.

	- The calculations are made taking the radius of the illumination spot (sample size). The sizes of the different images along the imaging system that are calculated in the code are actually only half of the 	total image.


----------------------------------------------------------


THE CODE: 

	- The code either calculates the suitable focal lengths for the tube lens and the telescope lenses of the set-up or checks if particular focal lengths are valid. Different variables must be input in order to do 	so. All of them are explained in the variables_microscope.txt file. The code will generate a .txt file when running. 

	1) Calculate focal length 
	(lens_tube_f = 0, lens_tl1_bf = 0, lens_tl2_f = 0)
 	
	This block of the code runs when the input focal lengths are 0.
	The code will generate a .txt file with the calculated focal lengths and information about the constraints. 

	Generated file: microscope_obtain_ss_xx_mag1_xx_sls_xx_dtot_xx.txt
		- ss: sample size (half of the diameter of the illumination spot in mm)
		- mag1: magnification of the objective-tube lens system
		- sls: size of the spectrometer slit (size of the image at slit - fixed for "obtain" code)
		- dtot: total distance of the set-up in mm 

	2) Check focal length 
	(lens_tube_f = xx, lens_tl1_bf = xx, lens_tl2_f = xx) 
	
	This block of the code runs when numbers are input for the focal lengths variables.
	The code will generate a .txt file with information of whether or not the input focal 	lengths are suitable for the indicated set up. The file will also provide information of 	why/why not they are suitable 	and the parameters this is based on. 

	Generated file: microscope_check_fTUBE_xx_bfTL1_xx_FTL2_xx.txt
	
	
