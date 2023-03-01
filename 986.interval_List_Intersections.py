## solving  https://leetcode.com/problems/interval-list-intersections/

# need to shorten loop cuz many intervals are being compared with second list with no reason.
#       for i in(a):
#           for j in (b):
#               if min(j) > max(i): (dont compare intervals)
#
#

firstList = [[0,2],[5,10],[13,23],[24,25]] 
secondList = [[1,5],[8,12],[15,24],[25,26]]



def whole_interval(a : list)->list:
    integer_list_interval = []
    for x in range(a[0], a[1] + 1):
        integer_list_interval.append(x)
    
    return integer_list_interval
    



def eval_intersection(a : list, b : list)->list:
    intersection_interval = []
    #print(f"{a} inerval and {b} interval will be evaluated")
    for x in a:
        if x in b: 
            intersection_interval.append(x)
            #print(f"{x} appended")
    if len(intersection_interval) == 0: return []
    return [min(intersection_interval), max(intersection_interval)]
    


def eval_list_intervals(a : list, b : list)->list:
    list_intersections = []
    if len(a) == 0 or len(b) == 0: return list_intersections
    for interval_a in a:
        for interval_b in b:
            if len(eval_intersection(whole_interval(interval_a), whole_interval(interval_b))) == 0: pass
            else: list_intersections.append(((eval_intersection(whole_interval(interval_a), whole_interval(interval_b))))) 
    return list_intersections
        
        



print(eval_list_intervals(firstList, secondList))



