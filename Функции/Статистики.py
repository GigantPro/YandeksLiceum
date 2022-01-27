import statistics


def print_statistics(arr):
    if len(arr) == 0:
        print('\n'.join(['0', '0', '0', '0', '0']))
    else:
        print(len(arr))
        print(sum(arr) / len(arr))
        print(min(arr))
        print(max(arr))
        print(statistics.median(arr))
        
