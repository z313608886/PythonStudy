def insertsort(lyst):
    i = 1
    while i < len(lyst):
        itemtoinsert = lyst[i]
        j = i -1
        while j>= 0:
            if itemtoinsert < lyst[j]:
                lyst[j+1] = lyst[j]
                j -= 1
            else:
                break
        lyst[j+1] = itemtoinsert
        i += 1

lm=[1,7,3,5,1,2]
insertsort(lm)
    
