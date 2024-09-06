n, m, k, x, y, z, t, a = [int(input()) for i in range(8)]
s1 = n + m - x - t
s2 = m + k - y - t
s3 = k + n - z - t
s = (n - s1 - s3 - t) + (m - s1 - s2 - t) + (k - s2 - s3 - t)
print(s)
print(s1 + s2 + s3)
print(a - s - s1 - s2 - s3 - t)
