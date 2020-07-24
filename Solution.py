def f(dis, weight, eat):
    if eat==0:
        return print('If elephant doesn\'t eat how will he move')
    rounds_tob_made = weight // 1000
    total_load = weight
    round=1
    loop_counter=0
    # dis-=1
    for i in range(dis):
        loop_counter+=1
        print('total_load :',total_load,'loop cycle:',i+1)
        if total_load <= 1000:
            total_load-=eat
        else:
            if (rounds_tob_made - 1) * 1000 == total_load:
                rounds_tob_made -= 1
            total_load-=eat
            total_load=total_load-((rounds_tob_made-1)*2*eat)
        round+=1
        if total_load <0:
            return print('oops... elephant doesn\'t have enough to eat')
    print('total load delivered =',total_load)

dis=1000
weight=3000
eat=1
f(dis,weight,eat)
