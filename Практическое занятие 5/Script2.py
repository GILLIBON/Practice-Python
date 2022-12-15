def summ(*param):
    sumparam = 0
    for n in param:
        sumparam = sumparam + n
    return(sumparam)

print(summ(1,2,3,4,5,6,7,8,9,0))