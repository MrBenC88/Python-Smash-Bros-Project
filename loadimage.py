from pygame import*
##Sprites===========================================================================
## Natsu

sprite=[[""]*22  for i in range(8)]
sprite[0][0]=[image.load("pictures\\Natsu\\NaRunL"+str(n)+".png")for n in range(6)]
sprite[0][1]=[image.load("pictures\\Natsu\\NaRunR"+str(n)+".png")for n in range(6)]
sprite[0][2]=[image.load("pictures\\Natsu\\NaJumpL"+str(n)+".png")for n in range(4)]
sprite[0][3]=[image.load("pictures\\Natsu\\NaJumpR"+str(n)+".png")for n in range(4)]
sprite[0][4]=[image.load("pictures\\Natsu\\NaAttack1L"+str(n)+".png")for n in range(11)]
sprite[0][5]=[image.load("pictures\\Natsu\\NaAttack1R"+str(n)+".png")for n in range(11)]
sprite[0][6]=[image.load("pictures\\Natsu\\NaAttack2L"+str(n)+".png")for n in range(22)]
sprite[0][7]=[image.load("pictures\\Natsu\\NaAttack2R"+str(n)+".png")for n in range(22)]
sprite[0][8]=[image.load("pictures\\Natsu\\NaAttack3L"+str(n)+".png")for n in range(4)]
sprite[0][9]=[image.load("pictures\\Natsu\\NaAttack3R"+str(n)+".png")for n in range(4)]
sprite[0][10]=[image.load("pictures\\Natsu\\NaDamageL"+str(n)+".png")for n in range(7)]
sprite[0][11]=[image.load("pictures\\Natsu\\NaDamageR"+str(n)+".png")for n in range(7)]
sprite[0][12]=[image.load("pictures\\Natsu\\NaWin"+str(n)+".png")for n in range(9)]

sprite[0][13]=image.load("pictures\\Natsu\\NaStandL.png")
sprite[0][14]=image.load("pictures\\Natsu\\NaStandR.png")
sprite[0][15]=image.load("pictures\\Natsu\\NaCrouchL.png")
sprite[0][16]=image.load("pictures\\Natsu\\NaCrouchR.png")
sprite[0][17]=image.load("pictures\\Natsu\\NaTaunt.png")

sprite[0][18]=[image.load("pictures\\Natsu\\NaFireballL0"+str(n)+".png")for n in range(8)]
sprite[0][19]=[image.load("pictures\\Natsu\\NaFireballR"+str(n)+".png")for n in range(8)]

Natsulist=[6,4,11,22,2]

#Grey
sprite[1][0]=[image.load("pictures\\Grey\\GrRunL"+str(g)+".png")for g in range(6)]
sprite[1][1]=[image.load("pictures\\Grey\\GrRunR"+str(g)+".png")for g in range(6)]
sprite[1][2]=[image.load("pictures\\Grey\\GrJumpL"+str(g)+".png")for g in range(4)]
sprite[1][3]=[image.load("pictures\\Grey\\GrJumpR"+str(g)+".png")for g in range(4)]
sprite[1][4]=[image.load("pictures\\Grey\\GrAttack1L"+str(g)+".png")for g in range(12)]
sprite[1][5]=[image.load("pictures\\Grey\\GrAttack1R"+str(g)+".png")for g in range(12)]
sprite[1][6]=[image.load("pictures\\Grey\\GrAttack2L"+str(g)+".png")for g in range(3)]
sprite[1][7]=[image.load("pictures\\Grey\\GrAttack2R"+str(g)+".png")for g in range(3)]
sprite[1][8]=[image.load("pictures\\Grey\\GrAttack3L"+str(g)+".png")for g in range(26)]
sprite[1][9]=[image.load("pictures\\Grey\\GrAttack3R"+str(g)+".png")for g in range(26)]
sprite[1][10]=[image.load("pictures\\Grey\\GrDamageL"+str(g)+".png")for g in range(7)]
sprite[1][11]=[image.load("pictures\\Grey\\GrDamageR"+str(g)+".png")for g in range(7)]
sprite[1][12]=[image.load("pictures\\Grey\\GrWin"+str(g)+".png")for g in range(7)]

sprite[1][13]=image.load("pictures\\Grey\\GrStandL.png")
sprite[1][14]=image.load("pictures\\Grey\\GrStandR.png")
sprite[1][15]=image.load("pictures\\Grey\\GrCrouchL.png")
sprite[1][16]=image.load("pictures\\Grey\\GrCrouchR.png")
sprite[1][17]=image.load("pictures\\Grey\\GrTaunt.png")

sprite[1][18]=image.load("pictures\\Grey\\GrArrowR.png")
sprite[1][19]=image.load("pictures\\Grey\\GrArrowL.png")


#Erza
sprite[2][0]=[image.load("pictures\Erza\ErRunL"+str(e)+".png")for e in range(7)]
sprite[2][1]=[image.load("pictures\Erza\ErRunR"+str(e)+".png")for e in range(7)]
sprite[2][2]=[image.load("pictures\Erza\ErJumpL"+str(e)+".png")for e in range(6)]
sprite[2][3]=[image.load("pictures\Erza\ErJumpR"+str(e)+".png")for e in range(6)]
sprite[2][4]=[image.load("pictures\Erza\ErAttack1L"+str(e)+".png")for e in range(10)]
sprite[2][5]=[image.load("pictures\Erza\ErAttack1R"+str(e)+".png")for e in range(10)]
sprite[2][6]=[image.load("pictures\Erza\ErAttack2L"+str(e)+".png")for e in range(5)]
sprite[2][7]=[image.load("pictures\Erza\ErAttack2R"+str(e)+".png")for e in range(5)]
sprite[2][8]=[image.load("pictures\Erza\ErAttack3L"+str(e)+".png")for e in range(6)]
sprite[2][9]=[image.load("pictures\Erza\ErAttack3R"+str(e)+".png")for e in range(6)]
sprite[2][10]=[image.load("pictures\Erza\ErDamageL"+str(e)+".png")for e in range(7)]
sprite[2][11]=[image.load("pictures\Erza\ErDamageR"+str(e)+".png")for e in range(7)]
sprite[2][12]=[image.load("pictures\Erza\ErWin"+str(e)+".png")for e in range(10)]

sprite[2][13]=image.load("pictures\Erza\ErStandL.png")
sprite[2][14]=image.load("pictures\Erza\ErStandR.png")
sprite[2][15]=image.load("pictures\Erza\ErCrouchL.png")
sprite[2][16]=image.load("pictures\Erza\ErCrouchR.png")
sprite[2][17]=image.load("pictures\Erza\ErTaunt.png")

#Wendy
sprite[3][0]=[image.load("pictures\\Wendy\\WeRunL"+str(w)+".png")for w in range(6)]              
sprite[3][1]=[image.load("pictures\\Wendy\\WeRunR"+str(w)+".png")for w in range(6)]  
sprite[3][2]=[image.load("pictures\\Wendy\\WeJumpL"+str(w)+".png")for w in range(5)]  
sprite[3][3]=[image.load("pictures\\Wendy\\WeJumpR"+str(w)+".png")for w in range(5)]  
sprite[3][4]=[image.load("pictures\\Wendy\\WeAttack1L"+str(w)+".png")for w in range(13)]  
sprite[3][5]=[image.load("pictures\\Wendy\\WeAttack1R"+str(w)+".png")for w in range(13)]  
sprite[3][6]=[image.load("pictures\\Wendy\\WeAttack2L"+str(w)+".png")for w in range(9)]  
sprite[3][7]=[image.load("pictures\\Wendy\\WeAttack2R"+str(w)+".png")for w in range(9)]  
sprite[3][8]=[image.load("pictures\\Wendy\\WeAttack3L"+str(w)+".png")for w in range(7)]  
sprite[3][9]=[image.load("pictures\\Wendy\\WeAttack3R"+str(w)+".png")for w in range(7)]
sprite[3][10]=[image.load("pictures\\Wendy\\WeDamageL"+str(w)+".png")for w in range(7)]  
sprite[3][11]=[image.load("pictures\\Wendy\\WeDamageR"+str(w)+".png")for w in range(7)]  
sprite[3][12]=[image.load("pictures\\Wendy\\WeWin"+str(w)+".png")for w in range(10)] 

sprite[3][13]=image.load("pictures\\Wendy\\WeTaunt.png")
sprite[3][14]=image.load("pictures\\Wendy\\WeStandL.png")
sprite[3][15]=image.load("pictures\\Wendy\\WeStandR.png")
sprite[3][16]=image.load("pictures\\Wendy\\WeCrouchL.png")
sprite[3][17]=image.load("pictures\\Wendy\\WeCrouchR.png")

sprite[3][18]=[image.load("pictures\\Wendy\\WaterAtkL"+str(w)+".png")for w in range(4)]  
sprite[3][19]=[image.load("pictures\\Wendy\\WaterAtkR"+str(w)+".png")for w in range(4)]  
sprite[3][20]=[image.load("pictures\\Wendy\\WaterBulletL"+str(w)+".png")for w in range(3)]  
sprite[3][21]=[image.load("pictures\\Wendy\\WaterBulletR"+str(w)+".png")for w in range(3)]  

#Gajeel
sprite[4][0]=[image.load("pictures\\Gajeel\\GaRunL"+str(gaj)+".png")for gaj in range(6)]   
sprite[4][1]=[image.load("pictures\\Gajeel\\GaRunR"+str(gaj)+".png")for gaj in range(6)] 
sprite[4][2]=[image.load("pictures\\Gajeel\\GaJumpL"+str(gaj)+".png")for gaj in range(5)] 
sprite[4][3]=[image.load("pictures\\Gajeel\\GaJumpR"+str(gaj)+".png")for gaj in range(5)] 
sprite[4][4]=[image.load("pictures\\Gajeel\\GaAttack1L"+str(gaj)+".png")for gaj in range(17)] 
sprite[4][5]=[image.load("pictures\\Gajeel\\GaAttack1R"+str(gaj)+".png")for gaj in range(17)] 
sprite[4][6]=[image.load("pictures\\Gajeel\\GaAttack2L"+str(gaj)+".png")for gaj in range(9)] 
sprite[4][7]=[image.load("pictures\\Gajeel\\GaAttack2R"+str(gaj)+".png")for gaj in range(9)] 
sprite[4][8]=[image.load("pictures\\Gajeel\\GaAttack3L"+str(gaj)+".png")for gaj in range(8)] 
sprite[4][9]=[image.load("pictures\\Gajeel\\GaAttack3R"+str(gaj)+".png")for gaj in range(8)] 
sprite[4][10]=[image.load("pictures\\Gajeel\\GaDamageL"+str(gaj)+".png")for gaj in range(7)] 
sprite[4][11]=[image.load("pictures\\Gajeel\\GaDamageR"+str(gaj)+".png")for gaj in range(7)] 
sprite[4][12]=[image.load("pictures\\Gajeel\\GaWin"+str(gaj)+".png")for gaj in range(4)] 

sprite[4][13]=image.load("pictures\\Gajeel\\GaTaunt.png")
sprite[4][14]=image.load("pictures\\Gajeel\\GaStandL.png")
sprite[4][15]=image.load("pictures\\Gajeel\\GaStandR.png")
sprite[4][16]=image.load("pictures\\Gajeel\\GaCrouchL.png")
sprite[4][17]=image.load("pictures\\Gajeel\\GaCrouchR.png")

sprite[4][18]=[image.load("pictures\\Gajeel\\MetalAtkL"+str(gaj)+".png")for gaj in range(7)] 
sprite[4][19]=[image.load("pictures\\Gajeel\\MetalAtkR"+str(gaj)+".png")for gaj in range(7)]
6
#Freed
sprite[5][0]=[image.load("pictures\\Freed\\FrRunL"+str(fr)+".png")for fr in range(6)]
sprite[5][1]=[image.load("pictures\\Freed\\FrRunR"+str(fr)+".png")for fr in range(6)]
sprite[5][2]=[image.load("pictures\\Freed\\FrJumpL"+str(fr)+".png")for fr in range(5)]
sprite[5][3]=[image.load("pictures\\Freed\\FrJumpR"+str(fr)+".png")for fr in range(5)]
sprite[5][4]=[image.load("pictures\\Freed\\FrAttack1L"+str(fr)+".png")for fr in range(24)]
sprite[5][5]=[image.load("pictures\\Freed\\FrAttack1R"+str(fr)+".png")for fr in range(24)]
sprite[5][6]=[image.load("pictures\\Freed\\FrAttack2L"+str(fr)+".png")for fr in range(20)]
sprite[5][7]=[image.load("pictures\\Freed\\FrAttack2R"+str(fr)+".png")for fr in range(20)]
sprite[5][8]=[image.load("pictures\\Freed\\FrAttack3L"+str(fr)+".png")for fr in range(17)]
sprite[5][9]=[image.load("pictures\\Freed\\FrAttack3R"+str(fr)+".png")for fr in range(17)]
sprite[5][10]=[image.load("pictures\\Freed\\FrDamageL"+str(fr)+".png")for fr in range(8)]
sprite[5][11]=[image.load("pictures\\Freed\\FrDamageR"+str(fr)+".png")for fr in range(8)]
sprite[5][12]=[image.load("pictures\\Freed\\FrWin"+str(fr)+".png")for fr in range(9)]

sprite[5][13]=image.load("pictures\\Freed\\FrTaunt.png")
sprite[5][14]=image.load("pictures\\Freed\\FrStandL.png")
sprite[5][15]=image.load("pictures\\Freed\\FrStandR.png")
sprite[5][16]=image.load("pictures\\Freed\\FrCrouchL.png")
sprite[5][17]=image.load("pictures\\Freed\\FrCrouchR.png")


#Lucy
sprite[6][0]=[image.load("pictures\\Lucy\\LucyRunpicsL0"+str(lu)+".png")for lu in range(6)]
sprite[6][1]=[image.load("pictures\\Lucy\\LucyRunpicsR"+str(lu)+".png")for lu in range(6)]
sprite[6][2]=image.load("pictures\\Lucy\\LuJumpL.png")
sprite[6][3]=image.load("pictures\\Lucy\\LuJumpR.png")
sprite[6][4]=[image.load("pictures\\Lucy\\LuAttack1L"+str(lu)+".png")for lu in range(16)]
sprite[6][5]=[image.load("pictures\\Lucy\\LuAttack1R"+str(lu)+".png")for lu in range(16)]
sprite[6][6]=[image.load("pictures\\Lucy\\LuAttack2L"+str(lu)+".png")for lu in range(5)]
sprite[6][7]=[image.load("pictures\\Lucy\\LuAttack2R"+str(lu)+".png")for lu in range(5)]
sprite[6][8]=[image.load("pictures\\Lucy\\LuAttack3L"+str(lu)+".png")for lu in range(5)]
sprite[6][9]=[image.load("pictures\\Lucy\\LuAttack3R"+str(lu)+".png")for lu in range(5)]
sprite[6][10]=[image.load("pictures\\Lucy\\LuDamageL"+str(lu)+".png")for lu in range(8)]
sprite[6][11]=[image.load("pictures\\Lucy\\LuDamageR"+str(lu)+".png")for lu in range(8)]
sprite[6][12]=[image.load("pictures\\Lucy\\lucywin"+str(lu)+".png")for lu in range(8)]

sprite[6][13]=image.load("pictures\\Lucy\\LuTaunt.png")
sprite[6][14]=image.load("pictures\\Lucy\\LuStandL.png")
sprite[6][15]=image.load("pictures\\Lucy\\LuStandR.png")
sprite[6][16]=image.load("pictures\\Lucy\\LuCrouchL.png")
sprite[6][17]=image.load("pictures\\Lucy\\LuCrouchR.png")

sprite[6][18]=[image.load("pictures\\Lucy\\LuAttack2L"+str(lu)+".png")for lu in range(5)]
sprite[6][19]=[image.load("pictures\\Lucy\\LuAttack2R"+str(lu)+".png")for lu in range(5)]

#falcon
sprite[7][0]=[image.load("Falcon\\runcaptleft"+str(fa)+".png")for fa in range(5)]
sprite[7][1]=[image.load("Falcon\\runcaptright"+str(fa)+".png")for fa in range(5)]
sprite[7][2]=image.load("FalconMv\\jumpleft.png")
sprite[7][3]=image.load("FalconMv\\jumpright.png")
sprite[7][4]=[image.load("FalconMv\\rapidfalconL"+str(fa)+".png")for fa in range(7)]
sprite[7][5]=[image.load("FalconMv\\rapidfalconR"+str(fa)+".png")for fa in range(7)]
sprite[7][6]=[image.load("FalconMv\\raptorboostleft"+str(fa)+".png")for fa in range(3)]
sprite[7][7]=[image.load("FalconMv\\raptorboostright"+str(fa)+".png")for fa in range(3)]
sprite[7][8]=[image.load("FalconMv\\falpunchpt"+str(fa)+".png")for fa in range(6)]
sprite[7][9]=[image.load("FalconMv\\fpunchleft"+str(fa)+".png")for fa in range(6)]

sprite[7][10]=image.load("FalconMv\\captainfalconshowurmoves.png")
sprite[7][11]=image.load("FalconMv\\standingcaptL.png")
sprite[7][12]=image.load("FalconMv\\standingcaptR.png")
sprite[7][13]=image.load("Falcon\\captcrouchl.png")
sprite[7][14]=image.load("Falcon\\captcrouchr.png")

napic=image.load("Selection pictures\\natzupic.png")
erpic=image.load("Selection pictures\\erzapic.png")
grepic=image.load("Selection pictures\\greypic.png")
gajpic=image.load("Selection pictures\\gajeelpic.png")
frpic=image.load("Selection pictures\\freedpic.png")
lupic=image.load("Selection pictures\\lucypic.png")
wepic=image.load("Selection pictures\\wendypic.png")
