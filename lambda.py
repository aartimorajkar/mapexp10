nums=[58,44,96,87,52,43,69,33]

evens= list(filter(lambda n: n%2==0, nums))
print(evens)
doubles = list(map(lambda n: n*n, evens))
print(doubles)


