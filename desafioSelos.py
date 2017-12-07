#calcular numero de selos utilizados

def stamps(numOfStamps):
    p5 = 0
    p2 = 0
    p1 = 0
    
    while(numOfStamps >= 1):
        if(numOfStamps >= 5):
            numOfStamps = numOfStamps - 5
            p5 = p5+1
        else:
            
            if(numOfStamps >= 2 and numOfStamps < 5):
                numOfStamps = numOfStamps - 2
                p2 = p2+1
            else:
                if(numOfStamps == 1):
                    numOfStamps = numOfStamps - 2
                    p1 = p1+1
                    
    return p5, p2,p1

    print(stamps(29))