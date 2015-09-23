import random
#m= 80
#global z

#ef print_board():
#	print '\n'.join([' '.join(row) for row in z])
def create_layout():
	global z
	z=[['x' for _ in range(80)] for _ in range(30)]
	for i in range(1,79):
		for j in range(1,29):
			if( (j%4 ) != 0):
				z[j][i]=' '
			
			if(j == 4):
				if((i>0 and i<30) or (i>45 and i<79)):
					z[j][i]=' '
			
			if(j == 28):
				if(i>45 and i<79):
					z[j][i]=' '
			
			if(j == 24):
				if(i>0 and i<20):
					z[j][i]=' '
			
			if(j == 20):
				if(i>55 and i<79):
					z[j][i]	= ' '
			
			if(j == 16):
				if(i>0 and i<30):
					z[j][i]=' '
			
			if(j == 12):
				if(i>40 and i<79):
					z[j][i]=' '
			
			if(j == 8):
				if(i>0 and i<20):
					z[j][i]=' '
			
			if(i == 35 or i == 43):
				if(j <4):
					z[j][i] = 'x'
			if(i == 40):
				if(j >=4 and j<8):
					z[j][i]='H'
			
			if(i == 30):
            			if(j >=8 and j<12):
                			z[j][i]='H'
			
			if(i == 40):
			 	if(j >=12 and j<16):
                    			z[j][i]='H'
			
			if(i == 35):
               			if(j >=16 and j<20):
                    			z[j][i]='H'
			
			if(i == 45):
                		if(j >=20 and j<24):
                    			z[j][i]='H'
			
			if(i == 25):
                		if(j >=24 and j<28):
                    			z[j][i]='H'

				

def print_board():
	print '\n'.join([' '.join(row) for row in z])

# creating the basic look of the board	
create_layout()
#print_board()


