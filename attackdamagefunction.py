def attackdamage(cha1,cha2,attacktypep1,attacktypep2):
    # all the attack statements
    global damagep1, damagep2
    
    if cha1=="Na":
        if attacktypep1=="attack1":
            damagep2+=4+damagep2//1000
        elif attacktypep1=="attack2":
            damagep2+=8+damagep2//1000
        elif attacktypep1=="attack3":
            damagep2+=18+damagep2//1000                                            
        
    elif cha1=="Gr":
        if attacktypep1=="attack1":
            damagep2+=7+damagep2//1000
        elif attacktypep1=="attack2":
            damagep2+=6+damagep2//1000
        elif attacktypep1=="attack3":
            damagep2+=14+damagep2//1000            
        
    elif cha1=="Er":
        if attacktypep1=="attack1":
            damagep2+=3+damagep2//1000
        elif attacktypep1=="attack2":
            damagep2+=10+damagep2//1000
        elif attacktypep1=="attack3":
            damagep2+=20+damagep2//1000            
        
    elif cha1=="Ga":
        if attacktypep1=="attack1":
            damagep2+=8+damagep2//1000
        elif attacktypep1=="attack2":
            damagep2+=5+damagep2//1000
        elif attacktypep1=="attack3":
            damagep2+=12+damagep2//1000            
        
    elif cha1=="Fr":
        if attacktypep1=="attack1":
            damagep2+=2+damagep2//1000
        elif attacktypep1=="attack2":
            damagep2+=14+damagep2//1000
        elif attacktypep1=="attack3":
            damagep2+=19+damagep2//1000            
        
    elif cha1=="Lu":
        if attacktypep1=="attack1":
            damagep2+=4+damagep2//1000
        elif attacktypep1=="attack2":
            damagep2+=12+damagep2//1000
        elif attacktypep1=="attack3":
            damagep2+=14+damagep2//1000            
        
    elif cha1=="We":
        if attacktypep1=="attack1":
            damagep2+=2+damagep2//1000
        elif attacktypep1=="attack2":
            damagep2+=11+damagep2//1000
        elif attacktypep1=="attack3":
            damagep2+=16+damagep2//1000            
        

    if cha2=="Na":
        if attacktypep2=="attack1":
            damagep1+=4+damagep1//1000
        elif attacktypep2=="attack2":
            damagep1+=8+damagep1//10000
        elif attacktypep2=="attack3":
            damagep1+=18+damagep1//10000              
        
    elif cha2=="Gr":
        if attacktypep2=="attack1":
            damagep1+=7+damagep1//10000
        elif attacktypep2=="attack2":
            damagep1+=6+damagep1//1000
        elif attacktypep2=="attack3":
            damagep1+=14+damagep1//1000              
        
    elif cha2=="Er":
        if attacktypep2=="attack1":
            damagep1+=3+damagep1//1000
        elif attacktypep2=="attack2":
            damagep1+=10+damagep1//1000
        elif attacktypep2=="attack3":
            damagep1+=20+damagep1//1000              
        
    elif cha2=="Ga":
        if attacktypep2=="attack1":
            damagep1+=8+damagep1//1000
        elif attacktypep2=="attack2":
            damagep1+=5+damagep1//1000
        elif attacktypep2=="attack3":
            damagep1+=12+damagep1//1000              
        
    elif cha2=="Fr":
        if attacktypep2=="attack1":
            damagep1+=2+damagep1//1000
        elif attacktypep2=="attack2":
            damagep1+=14+damagep1//1000
        elif attacktypep2=="attack3":
            damagep1+=19+damagep1//1000              
        
    elif cha2=="Lu":
        if attacktypep2=="attack1":
            damagep1+=4+damagep1//1000
        elif attacktypep2=="attack2":
            damagep1+=12+damagep1//1000
        elif attacktypep2=="attack3":
            damagep1+=14+damagep1//1000              
        
    elif cha2=="We":
        if attacktypep2=="attack1":
            damagep1+=2+damagep1//1000
        elif attacktypep2=="attack2":
            damagep1+=11+damagep1//1000
        elif attacktypep2=="attack3":
            damagep1+=16+damagep1//1000              

    print(damagep1,damagep2)
