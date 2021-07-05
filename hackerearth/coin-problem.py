def solve(n):
  arr = [1, 3, 4]

  result = [0]
  for i in range(1, n+1):
    res = 0
    for val in arr:

      if i==val:
        res += 1

      if (i-val) >=0 and result[i-val] > 0 :
        res += result[i-val]

    result.append(res)
    print(result)

solve(5)