# RULES:
# - You will start from the top and move downwards to an adjacent number as in below.
# - You are only allowed to walk downwards and diagonally.
# - You can only walk over NON PRIME NUMBERS.


import time
#Global values for better readibility of the input of the functions.
__primesarr = []
__values = {}
__height = 0
__totrescount = 0 


def arrofprimes(maxval):
    arr = []

    for i in range(2,maxval,1):
        flag = True
        for j in range(2,i,1):
            if (i%j == 0):
                flag = False
                break
        if flag == True:
            arr.append(i)

    return arr


def indexcalculator(layer, rescount):
    if layer > 0:
        return indexcalculator(layer-1, (rescount/2))
    elif layer == 0:
        return int(rescount/2)
    else:
        print("This cannot be possible.")
        return 0


def goleft(tree, index, layer, col):
    if layer < __height:
        #tree dict'in keyleri geregi layer+1'i kullanıyoruz.
        templayer = layer+1
        temparr = tree[templayer]
        
        #Eger asal sayı ise:
        if temparr[col] in __primesarr:
            #onun budaklandıgı butun sayilari -1 yap
            for itr in range(index, index + (indexcalculator(layer,__totrescount)),1):
                __values[itr] = int(-1)
        #Eger asal degilse:
        else:
            #onun budaklandıgı butun sayilara ekle.
            for itr in range(index, index + (indexcalculator(layer,__totrescount)),1):
                __values[itr] += temparr[col]

            goleft(tree, index, layer+1, col)
            goright(tree, index + (indexcalculator(templayer,__totrescount)), layer+1, col+1)
    else:
        return


def goright(tree, index, layer, col):
    if layer < __height:
        #tree dict'in keyleri geregi layer+1'i kullanıyoruz.
        templayer = layer+1
        temparr = tree[templayer]

        #Eger asal sayı ise:
        if temparr[col] in __primesarr:
            #onun budaklandıgı butun sayilari -1 yap
            for itr in range(index, index + (indexcalculator(layer,__totrescount)),1):
                __values[itr] = int(-1)
        #Eger asal degilse:
        else:
            #onun budaklandıgı butun sayilara ekle.
            for itr in range(index, index + (indexcalculator(layer,__totrescount)),1):
                __values[itr] += temparr[col]

            goleft(tree, index, layer+1, col)
            goright(tree, index + (indexcalculator(templayer, __totrescount)), layer+1, col+1)
    
    else:
        return


if __name__ == "__main__":
    start_time = time.time()
    #The part that reads the entire thing.
    myl = """215
            193 124
            117 237 442
            218 935 347 235
            320 804 522 417 345
            229 601 723 835 133 124
            248 202 277 433 207 263 257
            359 464 504 528 516 716 871 182
            461 441 426 656 863 560 380 171 923
            381 348 573 533 447 632 387 176 975 449
            223 711 445 645 245 543 931 532 937 541 444
            330 131 333 928 377 733 017 778 839 168 197 197
            131 171 522 137 217 224 291 413 528 520 227 229 928
            223 626 034 683 839 053 627 310 713 999 629 817 410 121
            924 622 911 233 325 139 721 218 253 223 107 233 230 124 233"""
    #Reformatting.
    myl = myl.replace("\n"," ")
    myl = list(map(int,myl.split()))
    #The tree in linear array form.
    #print(myl)
    #find the max. value in the list for the prime array
    maxval = 0
    for itr in myl:
        if maxval < itr:
            maxval = itr
    # print("The maxval value in the tree:",maxval)
    #Our primes array,roofed with the maxval above, for the constraint of the triangle.
    __primesarr = arrofprimes(maxval)

    #Fill in the tree
    tree = {}
    key = 0
    count = 0
    countlimit = 1
    temparr = []
    for item in myl:
        temparr.append(item)
        count += 1
        if count == countlimit:
            tree[key] = temparr
            temparr = []
            key += 1
            countlimit += 1
            count = 0
    #Write the tree
    # for line in tree:
    #     print(line, tree[line])
    # print("\n")

    #finding the height of the tree:
    __height = (len(tree)-1)
    __totrescount = int(2**__height)
    #The number of the elements
    elmsum = 0
    for itr in range(0,len(tree),1):
        elmsum += len(tree[itr])
    
    #index for __values.
    index = 0
    #fill in the __values array with the first element.
    for itr in range(0,__totrescount,1):
        __values[itr] = int((tree[0])[0])
    
    #current layer.
    layer = 0
    #going left is actually going down
    goleft(tree, index, layer, 0)
    #And going right is actually going diagonal(down-right)
    goright(tree, index + indexcalculator(layer,__totrescount), layer, 1)

    #Writing the __values array.
    # for itr in range(0,__totrescount,1):
    #     #Only writing the results that didn't have a prime number along the way.
    #     if __values[itr] != -1:
    #         print(itr,__values[itr])
    
    maxval = 0
    for item in __values:
        if maxval < __values[item]:
            maxval = __values[item]

    print("The desired result is:",maxval)
    
    print("\nExecution Time:",time.time() - start_time)
