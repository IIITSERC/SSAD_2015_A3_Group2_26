import random
from a import *
global px
#px=n-2
global py
global posd_x
global posd_y
global score
global life
#py=1
#z[px][py]='P'
#class person:
#	def _init_(self,name=""):
#		self._name = name
#		self._pos_x = pos_x
#		self._pos_y = pos_y
#print '*'

class person(object):
	def __init__(self, pl_x, pl_y):
		self.pl_x = pl_x
		self.pl_y = pl_y

class player(person):
	def __init__(self, pl_x, pl_y, name_ply):
		person.__init__(self, pl_x, pl_y)
		self.name_ply = name_ply

class donkey(object):
	def __init__(self, pl_x, pl_y, name_donk):
		person.__init__(self, pl_x, pl_y)
		self.name_donk = name_donk
		
prn = player(27, 1, 0)

v=0
k=0
#global prn.pl_x
#global prn.pl_y
global score
global hit_wall
global c
global	 hit 
score = 0
while(1):
	x=random.randint(1,79)
	y=random.randint(1,29)
	if( (z[y][x] == ' ' )and (z[y+1][x] == 'x') ):
		if(y+1 !=29 and x!=3):
			v=v+1
		 	#print v
		 	
			z[y][x] = 'C'
	if(v>20):
	
		break;
v=0
while(1):
	x=random.randint(1,79)
	y=random.randint(1,29)
	if( (z[y][x] == ' ' )and (z[y+1][x] == 'x') ):
		if(y+1 !=29 and x!=3):
			v=v+1
			 	#print v
			 	
			z[y][x] = 'O'
			if(v>8):
				break;
#prn.pl_y=1
z[prn.pl_x][prn.pl_y]='p'
print_board()
class person(object):
	def _init_(self):
		self._name = name
class coin_collect(object):
	def _init_(self,score):
		self._score=score
	def scored(self,k):
		
		self.score = 5*(k)
		return self.score
def jump():
	#global prn.pl_x
	#global prn.pl_y
	global c
	global e
#	e = raw_input('direction:' )
	# s=z[prn.pl_x][prn.pl_y]
	# z[prn.pl_x][prn.pl_y]=z[prn.pl_x-1][prn.pl_y]
	# z[prn.pl_x-1][prn.pl_y]=s
	# prn.pl_x=prn.pl_x-1
	e=raw_input('direction?:' )
	if(e == 'a'):
		s=z[prn.pl_x][prn.pl_y]
		z[prn.pl_x][prn.pl_y]=z[prn.pl_x][prn.pl_y-2]
		z[prn.pl_x][prn.pl_y-2]=s
		prn.pl_y = prn.pl_y-2
	if(e == 'd'):
		s=z[prn.pl_x][prn.pl_y]
		z[prn.pl_x][prn.pl_y]=z[prn.pl_x][prn.pl_y+2]
		z[prn.pl_x][prn.pl_y+2]=s
		prn.pl_y = prn.pl_y+2	

	
def check_wall(c):
	if(c == 'a'):
		if(z[prn.pl_x][prn.pl_y-1] != 'x'):
			return 1
		else:
			return 0
	if(c == 'd'):
		if(z[prn.pl_x][prn.pl_y+1] != 'x'):
			return 1
	  	else:
	    		return 0
	if(c == 'w'):
		if(z[prn.pl_x-1][prn.pl_y] != 'x'):
			return 1
		else:
			return 0
	if(c == 's'):
		if(z[prn.pl_x+1][prn.pl_y] != 'x'):
			return 1
		else:
			return 0
#create_layout()
#print_board()			
#def initial_donk():
##	for j in range(m):
#		if z[6][j].=='.':
#			x=random.randint(j,m-1)
#			z[5][x] = 'D'
#			break
##initial_donk()
#pri##nt_board()
z[3][38]='Q'
d=1 
posd_x = 7
posd_y = 0
z[posd_x][posd_y] = 'D'
global l
life = 3
global jj= 5*k
# 3 lifes for player
 ### flag condition to recognise stair case encounter
 #while(l):
# def left():

#string=raw_input("make your move")
def play():
	global score
	#global prn.pl_x
	#global prn.pl_y
	global score
	global hit_wall
	global c
	global	 hit 
	global px
#px=n-2
	global py
	global posd_x
	global posd_y
	global life
	global k
#py=
#	
	total = coin_collect()
	string=raw_input("make your move" )

	for c in string:
		if(c=='q'):
			life = life -1
			prn.pl_x = 27
			prn.pl_y=1
			k = 0
			#print "life"
		while(c!='q'):
	
			z[posd_x][posd_y] =' '
			posd_y = random.randint(21,78)
	#	posd_x = 7
			z[posd_x][posd_y]='D'
		#if player wants to go to left
			if (c=='a'):
			#checking for wall
			 #flag for checking stair case encountering
				hit = check_wall(c)
				if(hit ==1 and z[prn.pl_x+1][prn.pl_y-1] == 'x'):
					s=z[prn.pl_x][prn.pl_y]
					z[prn.pl_x][prn.pl_y]=z[prn.pl_x][prn.pl_y-1]
					z[prn.pl_x][prn.pl_y-1]=s
			#if player encounters coin
					if(z[prn.pl_x][prn.pl_y] == 'C'):
						z[prn.pl_x][prn.pl_y] == ' '
						k=k+1
					
					if(z[prn.pl_x][prn.pl_y] == 'H'):
						z[prn.pl_x][prn.pl_y] = ' '
						#player encountering fireball
					if(z[prn.pl_x][prn.pl_y] == 'O'):
						life = life-1
						j=j-25
					#	total.scored(k) = total.scored(k) -25
						prn.pl_x=27
						prn.pl_y=1

						break
				#when  player encounters stair cases
				# if(z[prn.pl_x][prn.pl_y-1] == 'H'):
				# 	d=0
				# 	z[prn.pl_x][prn.pl_y] = ' '
				#to keep track of number of coins collected
						#k=k+1
				#updating player position
					prn.pl_y=prn.pl_y-1
				else:
					print('OOPs! It hurts!')

		#if player wants to go to right
	 		if (c=='d'):
	 	#checking for wall
				hit = check_wall(c)
	 			if(hit==1 and z[prn.pl_x+1][prn.pl_y+1] == 'x'):
					s=z[prn.pl_x][prn.pl_y]
					z[prn.pl_x][prn.pl_y]=z[prn.pl_x][prn.pl_y+1]
					z[prn.pl_x][prn.pl_y+1]=s
					#d=d+1
			#if player encounters coin
					if(z[prn.pl_x][prn.pl_y] == 'C'):
						#print 1	
			            		z[prn.pl_x][prn.pl_y] = ' '
				#to keep track of no.of coins collected
						k=k+1
					if(z[prn.pl_x][prn.pl_y] == 'H'):
						z[prn.pl_x][prn.pl_y] = ' '	
						#player encountering fireball
					if(z[prn.pl_x][prn.pl_y] == 'O'):
						life = life-1
						j=j-25
						#total.scored(k)=total.scored(k) - 25
						prn.pl_x=27
						prn.pl_y = 1
						print 2
						break
				#updating player position
					prn.pl_y=prn.pl_y+1
				else:
					print('OOPS! Its a wall')
			if (c=='w'):
			#checking for walls
				hit=check_wall(c)
				if(hit == 1):
					s=z[prn.pl_x][prn.pl_y]
					z[prn.pl_x][prn.pl_y]=z[prn.pl_x-1][prn.pl_y]
					z[prn.pl_x-1][prn.pl_y]=s
					prn.pl_x=prn.pl_x-1
					if(z[prn.pl_x+1][prn.pl_y] == ' '):
						z[prn.pl_x+1][prn.pl_y] = 'H'

			#updating player position
				else:
					print ('oops!it is a wall')
			#hit_wall=0
				#prn.pl_x=prn.pl_x-1
			if (c=='s'):
			#checking for wall
				hit = check_wall(c)
				if (hit ==1):
					s=z[prn.pl_x][prn.pl_y]
					z[prn.pl_x][prn.pl_y]=z[prn.pl_x+1][prn.pl_y]
					z[prn.pl_x+1][prn.pl_y]=s
			#updating player position
					prn.pl_x=prn.pl_x+1
			if (c==' '):
				jump()
		#prn.pl_y=prn.pl_y+2
			# if(prn.pl_x == 3 and prn.pl_y == 38):
			# 	c=q
			# 	print YAYY!YOU WON !!!
			# 	pass
		

			print_board()
			total=coin_collect()
			y=j
		#	y=total.scored(k)
			print y
			if(prn.pl_x == 3 and prn.pl_y == 38):
				c=q
				life = 3
				j=j+50
				#total.scored(k) =total.scored(k) +50
				print "YAYY!YOU WON !!!"
				pass
			c=raw_input("next")
#life =3
	if(life <=2 and life>0):
		print_board()
		total = coin_collect()
		y=j
		print y
while(life>0):
	play()



