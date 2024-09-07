def mean(*args):
    lst = [i for i in args if type(i) == int or type(i) == float]
    try:
        return sum(lst) / len(lst)
    except:
        return 0.0
