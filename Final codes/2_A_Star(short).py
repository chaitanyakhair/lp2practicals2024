dict_hn={'A':11,'B':169,'C':431,'D':567, 'E':269}

dict_gn=dict(
    A=dict(B=21,D=12,E=52),
    B=dict(A=23,E=45,C=69),
    C=dict(B=78,D=87,E=90),
    D=dict(A=61,C=11),
    E=dict(A=44,B=92,C=59)
)

import queue as Q
start='B'
goal='A'
result=''

def get_fn(citystr):
    cities=citystr.split(" , ")
    hn=gn=0
    for ctr in range(0, len(cities)-1):
        gn=gn+dict_gn[cities[ctr]][cities[ctr+1]]
    hn=dict_hn[cities[len(cities)-1]]
    return(hn+gn)

def expand(cityq):
    global result
    tot, citystr, thiscity=cityq.get()
    if thiscity==goal:
        result=citystr+" : : "+str(tot)
        return
    for cty in dict_gn[thiscity]:
        cityq.put((get_fn(citystr+" , "+cty), citystr+" , "+cty, cty))
    expand(cityq)

def main():
    cityq=Q.PriorityQueue()
    thiscity=start
    cityq.put((get_fn(start),start,thiscity))
    expand(cityq)
    print("The A* path with the total is: ")
    print(result)
main()
