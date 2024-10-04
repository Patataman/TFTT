def trit_power(numbers):
    val = 0
    for i, n in enumerate(numbers):
        val += n*3**i
    return val

# print(trit_power([2,0,1]))

def successor(numbers: list) -> list:
    """ Return input successor
    """
    carriage = 1  # carriage = 1 for first iteration, instead of having an if
    output = []
    for i, n in enumerate(numbers):
        n = (n + carriage) % 3
        # As we are working with powers of 3:
        # if a number is higher than 2, it becomes a 0 and next position has +1
        #   (e.g. [2,0,1] -> [0,1,1]
        if n == 0 and carriage != 0:
            # Check to avoid assuming a 0 is always because the previous sum
            carriage = 1
        else:
            carriage = 0
        output.append(n)
    # if we end with a carriage we need to add the number
    if carriage != 0:
        output.append(1)

    return output

# print(successor([2,2,2]))
# print(trit_power([2,2,2]), trit_power([0,0,0,1]))

def trit_power(numbers) -> int:
    val = 0
    for i, n in enumerate(numbers):
        val += n*3**i
    return val

def leq(tritA: list, tritB: list) -> bool:
    """ Return if tritA is <= than tritB
    """
    # Cannot do this because lists can have all 0s
    # if len(tritB) > len(tritA):
    #     return False
    valA = trit_power(tritA)
    valB = trit_power(tritB)
    return valA <= valB

# print(leq([0,1,1],[2,0,1]), leq([2,0,1,0],[2,0,1]), leq([0,0,0,0,1], [2,2,2,2]))

def tritwise_min(tritA: list, tritB: list) -> list:
    """ Return minimum value for each position of the lists
    """
    output = []
    for n_A, n_B in zip(tritA, tritB):
        _min = min(n_A, n_B)
        output.append(_min)

    # If any list is longer than the other, we don't care because it will be
    # 0s in that case, as the example min([2,1], [0,2,1]) -> [0,1]
    return output

# print(tritwise_min([2,1], [0,2,1]))
# print(tritwise_min([1,0,3], [0,1,2]))
# print(tritwise_min([2,1], []))
# print(tritwise_min([1,0,2], [1,1,1]))

def eq(tritA: list, tritB: list) -> bool:
    """ Return if tritA is <= than tritB
    """
    # Cannot do this because lists can have all 0s
    # if len(tritB) > len(tritA):
    #     return False
    valA = trit_power(tritA)
    valB = trit_power(tritB)
    return valA == valB


def f(tritA: list, tritB: list) -> list:
    if not leq(tritA, tritB):
        print("A is not smaller than B, swapping values")
        _aux = tritA
        tritA = tritB
        tritB = _aux

    succ_A = successor(tritA)
    tritwise_A = tritwise_min(tritA, succ_A)
    while not eq(succ_A, tritB):
        succ_A = successor(succ_A)
        tritwise_A = tritwise_min(tritwise_A, succ_A)

    return tritwise_A

A = [1,2]
B = [2,2]
print(trit_power(A))
print(trit_power(B))
print(f(A, B))

def f_eff(tritA: list, tritB: list) -> list:
    """ As we are doing tritwise with the successor
        of A, output will eventually be 0 or the smallest number
        between 1,N positions
    """
    if not leq(tritA, tritB):
        print("A is not smaller than B, swapping values")
        _aux = tritA
        tritA = tritB
        tritB = _aux

    output = []

    Aval = trit_power(tritA)
    Bval = trit_power(tritB)

    if len(tritB) > len(tritA):
        # In this cases it will be all 0s
        # tritwise_min([0,2,2], [1,2,2,1]) -> (0,2,2,0)
        # and the last 0 will be carried on until the end
        return [0] * len(tritA)
    else:
        output = []
        prevA_smaller = False
        for i in range(len(tritB)-1, -1, -1):
            if prevA_smaller:
                val = 0
                prevA_smaller = False
            elif tritB[i] == tritA[i]:
                val = tritB[i]
            elif tritB[i] > tritA[i]:
                if i != (len(tritB)-1) and Bval - Aval > 1:
                    val = 0
                else:
                    val = tritA[i]
                prevA_smaller = True
            elif tritB[i] < tritA[i]:
                val = 0
            output.insert(0, val)

        return output

print(f_eff(A,B))

