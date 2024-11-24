def test_location(cards, query, mid):
    mid_number = cards[mid]
    print("mid:", mid, "mid_number:", mid_number)
    if mid_number == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'
    

def locate_cards(cards, query):
    lo, hi =0, len(cards) -1 
    while lo <= hi:
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)
        mid_number = cards[mid]

        print("lo:", lo, "hi:", hi,"mid:",mid , "mid_number:", mid_number)

        if result == 'found':
            print(mid)
            return mid
        elif result == 'left':
            hi = mid-1
        elif result == 'right':
            lo = mid+1

    return -1


locate_cards([9, 7, 8 , 3, 2, 1], 1)