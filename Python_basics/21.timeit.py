import timeit
'0-1-2-3-.....-99'
print("-".join(str(n) for n in range(100)))
print("\n")
print(",".join(str(n) for n in range(100)))

print(timeit.timeit( '",".join(str(n) for n in range(100))', number=10000 ))

print(timeit.timeit( '",".join([str(n) for n in range(100)])', number=10000 ))