def constructTree(input, segTree, low, high, pos):
    if low == high:
        segTree[pos] = input[low]
        return
    mid = (low+high)//2
    constructTree(input, segTree, low, mid, 2*pos+1)
    constructTree(input, segTree, mid+1, high, 2*pos+2)
    segTree[pos] = min(segTree[2*pos+1], segTree[2*pos+2])

def rangeMinQuery(segTree, qlow, qhigh, low, high, pos):
    #total overlap
    if qlow <= low and qhigh >= high:
        return segTree[pos]
    #no overlap
    if qlow > high or qhigh < low:
        return float("inf")
    mid = (low+high)//2
    return min(rangeMinQuery(segTree, qlow, qhigh, low, mid, 2*pos+1),
               rangeMinQuery(segTree, qlow, qhigh, mid+1, high, 2*pos+2))

def updateSegmentTreeRangeLazy(segTree, lazy, startRange, endRange, delta,
                               low, high, pos):
    if low > high:
        return
    if lazy[pos] != 0:
        segTree[pos] += lazy[pos]
        if low != high: # non-leaf nodes
            lazy[2*pos+1] += lazy[pos]
            lazy[2*pos+2] += lazy[pos]
        lazy[pos] = 0
    if startRange > high or endRange < low:
        return
    if startRange <= low and endRange >= high:
        segTree[pos] += delta
        if low != high:
            lazy[2*pos+1] += delta
            lazy[2*pos+2] += delta
        return
    mid = (low+high)//2
    updateSegmentTreeRangeLazy(segTree, lazy, startRange, endRange, delta, low, mid, 2*pos+1)
    updateSegmentTreeRangeLazy(segTree, lazy, startRange, endRange, delta, mid+1, high, 2*pos+2)
    segTree[pos] = min(segTree[2*pos+1], segTree[2*pos+2])

def rangeMinQueryLazy(segTree, lazy, qlow, qhigh, low, high, pos):
    if low > high:
        return
    if lazy[pos] != 0:
        segTree[pos] += lazy[pos]
        if low != high:
            lazy[2*pos+1] += lazy[pos]
            lazy[2*pos+2] += lazy[pos]
        lazy[pos] = 0

    if qlow > high or qhigh < low:
        return float("inf")
    if qlow <= low and qhigh >= high:
        return segTree[pos]
    mid = (low+high)//2
    return min(rangeMinQueryLazy(segTree, lazy, qlow, qhigh, low, mid, 2*pos+1),
               rangeMinQueryLazy(segTree, lazy, qlow, qhigh, mid+1, high, 2*pos+2))

if __name__ == "__main__":
    #input = [-1,0,3,6]
    input = [-1, 3, 4, 0, 2, 1]
    segTree = [float("inf")]*15
    constructTree(input, segTree, 0, len(input)-1, 0)
    print (input[0:3])
    print (segTree)
    print (rangeMinQuery(segTree, 0, 2, 0, len(input)-1, 0))
    lazy = [0] * 15
    updateSegmentTreeRangeLazy(segTree, lazy, 0, 3, 3, 0, len(input)-1, 0)
    print (segTree)
    print (rangeMinQueryLazy(segTree, lazy, 0, 2, 0, len(input)-1, 0))
