#spritelist.py
# Sprite organization
from pygame import*
# Natsu
sprite=[[""]*18  for i in range(7)]
sprite[0][0]=[image.load("Natsu\\NaRunL"+str(n)+".png")for n in range(6)]
sprite[0][1]=[image.load("Natsu\\NaRunR"+str(n)+".png")for n in range(6)]
sprite[0][2]=[image.load("Natsu\\NaJumpL"+str(n)+".png")for n in range(4)]
sprite[0][3]=[image.load("Natsu\\NaJumpR"+str(n)+".png")for n in range(4)]
sprite[0][4]=[image.load("Natsu\\NaAttack1L"+str(n)+".png")for n in range(11)]
sprite[0][5]=[image.load("Natsu\\NaAttack1R"+str(n)+".png")for n in range(11)]
sprite[0][6]=[image.load("Natsu\\NaAttack2L"+str(n)+".png")for n in range(22)]
sprite[0][7]=[image.load("Natsu\\NaAttack2R"+str(n)+".png")for n in range(22)]
sprite[0][8]=[image.load("Natsu\\NaAttack3L"+str(n)+".png")for n in range(4)]
sprite[0][9]=[image.load("Natsu\\NaAttack3R"+str(n)+".png")for n in range(4)]
sprite[0][10]=[image.load("Natsu\\NaFireballL0"+str(n)+".png")for n in range(8)]
sprite[0][11]=[image.load("Natsu\\NaFireballR"+str(n)+".png")for n in range(8)]
sprite[0][12]=[image.load("Natsu\\NaDamageL"+str(n)+".png")for n in range(7)]
sprite[0][13]=[image.load("Natsu\\NaDamageR"+str(n)+".png")for n in range(7)]
sprite[0][14]=[image.load("Natsu\\NaWin"+str(n)+".png")for n in range(9)]

NaStandR=image.load("Natsu\\NaStandR.png")
NaStandL=image.load("Natsu\\NaStandL.png")
NaTaunt=image.load("Natsu\\NaTaunt.png")
NaCrouchL=image.load("Natsu\\NaCrouchL.png")
NaCrouchR=image.load("Natsu\\NaCrouchR.png")
NaJumpL=image.load("Natsu\\NaJumpL.png")
NaJumpR=image.load("Natsu\\NaJumpR.png")

#Grey
sprite[1][0]=[image.load("Grey\\GrRunL"+str(g)+".png")for g in range(6)]
sprite[1][1]=[image.load("Grey\\GrRunR"+str(g)+".png")for g in range(6)]
sprite[1][2]=[image.load("Grey\\GrJumpL"+str(g)+".png")for g in range(4)]
sprite[1][3]=[image.load("Grey\\GrJumpR"+str(g)+".png")for g in range(4)]
sprite[1][4]=[image.load("Grey\\GrAttack1L"+str(g)+".png")for g in range(12)]
sprite[1][5]=[image.load("Grey\\GrAttack1R"+str(g)+".png")for g in range(12)]
sprite[1][6]=[image.load("Grey\\GrAttack2L"+str(g)+".png")for g in range(3)]
sprite[1][7]=[image.load("Grey\\GrAttack2R"+str(g)+".png")for g in range(3)]
sprite[1][8]=[image.load("Grey\\GrAttack3L"+str(g)+".png")for g in range(26)]
sprite[1][9]=[image.load("Grey\\GrAttack3R"+str(g)+".png")for g in range(26)]
sprite[1][10]=[image.load("Grey\\GrDamageL"+str(g)+".png")for g in range(7)]
sprite[1][11]=[image.load("Grey\\GrDamageR"+str(g)+".png")for g in range(7)]
sprite[1][12]=[image.load("Grey\\GrWin"+str(g)+".png")for g in range(7)]

arrowR=image.load("Grey\\GrArrowR.png")
arrowL=image.load("Grey\\GrArrowL.png")
GrTaunt=image.load("Grey\\GrTaunt.png")
GrStandL=image.load("Grey\\GrStandL.png")
GrStandR=image.load("Grey\\GrStandR.png")
GrCrouchL=image.load("Grey\\GrCrouchL.png")
GrCrouchR=image.load("Grey\\GrCrouchR.png")
GrJumpL=image.load("Grey\\GrJumpL.png")
GrJumpR=image.load("Grey\\GrJumpR.png")

#Erza
sprite[2][0]=[image.load("Erza\\ErRunL"+str(e)+".png")for e in range(7)]
sprite[2][1]=[image.load("Erza\\ErRunR"+str(e)+".png")for e in range(7)]
sprite[2][2]=[image.load("Erza\\ErJumpL"+str(e)+".png")for e in range(6)]
sprite[2][3]=[image.load("Erza\\ErJumpR"+str(e)+".png")for e in range(6)]
sprite[2][4]=[image.load("Erza\\ErAttack1L"+str(e)+".png")for e in range(10)]
sprite[2][5]=[image.load("Erza\\ErAttack1R"+str(e)+".png")for e in range(10)]
sprite[2][6]=[image.load("Erza\\ErAttack2L"+str(e)+".png")for e in range(5)]
sprite[2][7]=[image.load("Erza\\ErAttack2R"+str(e)+".png")for e in range(5)]
sprite[2][8]=[image.load("Erza\\ErAttack3L"+str(e)+".png")for e in range(6)]
sprite[2][9]=[image.load("Erza\\ErAttack3R"+str(e)+".png")for e in range(6)]
sprite[2][10]=[image.load("Erza\\ErDamageL"+str(e)+".png")for e in range(7)]
sprite[2][11]=[image.load("Erza\\ErDamageR"+str(e)+".png")for e in range(7)]
sprite[2][12]=[image.load("Erza\\ErWin"+str(e)+".png")for e in range(10)]

ErTaunt=image.load("Erza\\ErTaunt.png")
ErStandL=image.load("Erza\\ErStandL.png")
ErStandR=image.load("Erza\\ErStandR.png")
ErCrouchL=image.load("Erza\\ErCrouchL.png")
ErCrouchR=image.load("Erza\\ErCrouchR.png")
ErJumpL=image.load("Erza\\ErJumpL.png")
ErJumpR=image.load("Erza\\ErJumpR.png")

#Wendy
sprite[3][0]=[image.load("Wendy\\WeRunL"+str(w)+".png")for w in range(6)]              
sprite[3][1]=[image.load("Wendy\\WeRunR"+str(w)+".png")for w in range(6)]  
sprite[3][2]=[image.load("Wendy\\WeJumpL"+str(w)+".png")for w in range(5)]  
sprite[3][3]=[image.load("Wendy\\WeJumpR"+str(w)+".png")for w in range(5)]  
sprite[3][4]=[image.load("Wendy\\WeAttack1L"+str(w)+".png")for w in range(13)]  
sprite[3][5]=[image.load("Wendy\\WeAttack1R"+str(w)+".png")for w in range(13)]  
sprite[3][6]=[image.load("Wendy\\WeAttack2L"+str(w)+".png")for w in range(9)]  
sprite[3][7]=[image.load("Wendy\\WeAttack2R"+str(w)+".png")for w in range(9)]  
sprite[3][8]=[image.load("Wendy\\WeAttack3L"+str(w)+".png")for w in range(7)]  
sprite[3][9]=[image.load("Wendy\\WeAttack3R"+str(w)+".png")for w in range(7)]
sprite[3][10]=[image.load("Wendy\\WeDamageL"+str(w)+".png")for w in range(7)]  
sprite[3][11]=[image.load("Wendy\\WeDamageR"+str(w)+".png")for w in range(7)]  
sprite[3][12]=[image.load("Wendy\\WeWin"+str(w)+".png")for w in range(10)] 
sprite[3][13]=[image.load("Wendy\\WaterAtkL"+str(w)+".png")for w in range(4)]  
sprite[3][14]=[image.load("Wendy\\WaterAtkR"+str(w)+".png")for w in range(4)]  
sprite[3][15]=[image.load("Wendy\\WaterBulletL"+str(w)+".png")for w in range(3)]  
sprite[3][16]=[image.load("Wendy\\WaterBulletR"+str(w)+".png")for w in range(3)]  

WeTaunt=image.load("Wendy\\WeTaunt.png")
WeStandL=image.load("Wendy\\WeStandL.png")
WeStandR=image.load("Wendy\\WeStandR.png")
WeCrouchL=image.load("Wendy\\WeCrouchL.png")
WeCrouchR=image.load("Wendy\\WeCrouchR.png")
WeJumpL=image.load("Wendy\\WeJumpL.png")
WeJumpR=image.load("Wendy\\WeJumpR.png")

#Gajeel
sprite[4][0]=[image.load("Gajeel\\GaRunL"+str(gaj)+".png")for gaj in range(6)]   
sprite[4][1]=[image.load("Gajeel\\GaRunR"+str(gaj)+".png")for gaj in range(6)] 
sprite[4][2]=[image.load("Gajeel\\GaJumpL"+str(gaj)+".png")for gaj in range(5)] 
sprite[4][3]=[image.load("Gajeel\\GaJumpR"+str(gaj)+".png")for gaj in range(5)] 
sprite[4][4]=[image.load("Gajeel\\GaAttack1L"+str(gaj)+".png")for gaj in range(17)] 
sprite[4][5]=[image.load("Gajeel\\GaAttack1R"+str(gaj)+".png")for gaj in range(17)] 
sprite[4][6]=[image.load("Gajeel\\GaAttack2L"+str(gaj)+".png")for gaj in range(9)] 
sprite[4][7]=[image.load("Gajeel\\GaAttack2R"+str(gaj)+".png")for gaj in range(9)] 
sprite[4][8]=[image.load("Gajeel\\GaAttack3L"+str(gaj)+".png")for gaj in range(8)] 
sprite[4][9]=[image.load("Gajeel\\GaAttack3R"+str(gaj)+".png")for gaj in range(8)] 
sprite[4][10]=[image.load("Gajeel\\GaDamageL"+str(gaj)+".png")for gaj in range(7)] 
sprite[4][11]=[image.load("Gajeel\\GaDamageR"+str(gaj)+".png")for gaj in range(7)] 
sprite[4][12]=[image.load("Gajeel\\GaWin"+str(gaj)+".png")for gaj in range(4)] 
sprite[4][13]=[image.load("Gajeel\\MetalAtkL"+str(gaj)+".png")for gaj in range(7)] 
sprite[4][14]=[image.load("Gajeel\\MetalAtkR"+str(gaj)+".png")for gaj in range(7)] 

GaTaunt=image.load("Gajeel\\GaTaunt.png")
GaStandL=image.load("Gajeel\\GaStandL.png")
GaStandR=image.load("Gajeel\\GaStandR.png")
GaCrouchL=image.load("Gajeel\\GaCrouchL.png")
GaCrouchR=image.load("Gajeel\\GaCrouchR.png")
GaJumpL=image.load("Gajeel\\GaJumpL.png")
GaJumpR=image.load("Gajeel\\GaJumpR.png")

#Freed
sprite[5][0]=[image.load("Freed\\FrRunL"+str(fr)+".png")for fr in range(6)]
sprite[5][1]=[image.load("Freed\\FrRunR"+str(fr)+".png")for fr in range(6)]
sprite[5][2]=[image.load("Freed\\FrJumpL"+str(fr)+".png")for fr in range(5)]
sprite[5][3]=[image.load("Freed\\FrJumpR"+str(fr)+".png")for fr in range(5)]
sprite[5][4]=[image.load("Freed\\FrAttack1L"+str(fr)+".png")for fr in range(24)]
sprite[5][5]=[image.load("Freed\\FrAttack1R"+str(fr)+".png")for fr in range(24)]
sprite[5][6]=[image.load("Freed\\FrAttack2L"+str(fr)+".png")for fr in range(20)]
sprite[5][7]=[image.load("Freed\\FrAttack2R"+str(fr)+".png")for fr in range(20)]
sprite[5][8]=[image.load("Freed\\FrAttack3L"+str(fr)+".png")for fr in range(17)]
sprite[5][9]=[image.load("Freed\\FrAttack3R"+str(fr)+".png")for fr in range(17)]
sprite[5][10]=[image.load("Freed\\FrDamageL"+str(fr)+".png")for fr in range(8)]
sprite[5][11]=[image.load("Freed\\FrDamageR"+str(fr)+".png")for fr in range(8)]
sprite[5][12]=[image.load("Freed\\FrWin"+str(fr)+".png")for fr in range(9)]

FrTaunt=image.load("Freed\\FrTaunt.png")
FrStandL=image.load("Freed\\FrStandL.png")
FrStandR=image.load("Freed\\FrStandR.png")
FrCrouchL=image.load("Freed\\FrCrouchL.png")
FrCrouchR=image.load("Freed\\FrCrouchR.png")
FrJumpL=image.load("Freed\\FrJumpL.png")
FrJumpR=image.load("Freed\\FrJumpR.png")

#Lucy
#This sprite list below does not follow the pattern/ order like the rest
sprite[6][0]=[image.load("Lucy\\LucyRunpicsL0"+str(lu)+".png")for lu in range(6)]
sprite[6][1]=[image.load("Lucy\\LucyRunpicsR"+str(lu)+".png")for lu in range(6)]
sprite[6][2]=[image.load("Lucy\\LuAttack1L"+str(lu)+".png")for lu in range(16)]
sprite[6][3]=[image.load("Lucy\\LuAttack1R"+str(lu)+".png")for lu in range(16)]
sprite[6][4]=[image.load("Lucy\\LuAttack2SummonL"+str(lu)+".png")for lu in range(6)]
sprite[6][5]=[image.load("Lucy\\LuAttack2SummonR"+str(lu)+".png")for lu in range(6)]
sprite[6][6]=[image.load("Lucy\\LuAttack3L"+str(lu)+".png")for lu in range(5)]
sprite[6][7]=[image.load("Lucy\\LuAttack3R"+str(lu)+".png")for lu in range(5)]
sprite[6][8]=[image.load("Lucy\\LuAttack2L"+str(lu)+".png")for lu in range(5)]
sprite[6][9]=[image.load("Lucy\\LuAttack2R"+str(lu)+".png")for lu in range(5)]
sprite[6][10]=[image.load("Lucy\\LuDamageL"+str(lu)+".png")for lu in range(8)]
sprite[6][11]=[image.load("Lucy\\LuDamageR"+str(lu)+".png")for lu in range(8)]
sprite[6][12]=[image.load("Lucy\\lucywin"+str(lu)+".png")for lu in range(8)]

#  =====NOTE=====
#sprite[6][8] are the lucy summon sprites in which lucy does the summoning motion
#sprite[6][9]
#  ==============

#rest of the pics
LuTaunt=image.load("Lucy\\LuTaunt.png")
LuStandL=image.load("Lucy\\LuStandL.png")
LuStandR=image.load("Lucy\\LuStandR.png")
LuCrouchL=image.load("Lucy\\LuCrouchL.png")
LuCrouchR=image.load("Lucy\\LuCrouchR.png")
# these are the pics for jumping- there are no
#sprites for jumping for the character Lucy
LuJumpL=image.load("Lucy\\LuJumpL.png")
LuJumpR=image.load("Lucy\\LuJumpR.png")

