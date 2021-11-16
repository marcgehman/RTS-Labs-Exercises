class RTS():

    # Returns a hash/object/map/etc. with the keys "above" and "below" with
    # the corresponding count of integers from the list that are above or below the comparison value
    def aboveBelow(self, lst, comparer):
        above = 0
        below = 0

        for i in lst:
            if (i > comparer):
                above += 1
            elif (i < comparer):
                below += 1

        return {
            "above": above,
            "below": below
        }
    

    # Rotate a string to the right by an offset
    # Returns a new string, rotating the characters in the original string to the right
    # by the rotation amount, and have the overflow appear at the beginning.
    def stringRotation(self,value, offset):
        # The portion of the string that isn't going to overflow
        base = value[0 : len(value) - offset]
        
        # When rotating right, the right-most characters contained within
        # the offset length will overflow
        overflow = value[len(value) - offset: ]

        return overflow + base
    












if __name__ == '__main__':
    rts = RTS()

    test1 = [1, 2000, 300, 17, 39, 16, 59, 50, 5000]
    comparer = 40
    res1 = rts.aboveBelow(test1, comparer)
    print(res1)


    test2 = "Hello, World!"
    offset = 2
    res2 = rts.stringRotation(test2, offset)
    print(res2)
