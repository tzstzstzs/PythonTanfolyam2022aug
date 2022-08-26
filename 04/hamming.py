
def hamming(s1, s2):
    if len(s1) != len(s2):
        return -1
    # else
    cnt = 0
    # for c1, c2 in zip(s1, s2):
        # if c1 != c2:
            # cnt += 1
        #
    #

    size = len(s1)
    for i in range(size):
        if s1[i] != s2[i]:
            cnt += 1

    return cnt


def main():
    s1 = "toned"
    s2 = "tonxx"
    distance = hamming(s1, s2)
    print(distance)

##############################################################################

if __name__ == "__main__":
    main()
