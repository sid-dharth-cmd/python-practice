s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}
print(f"Before removing common element: \ns1 = {s1}\ns2 = {s2}")
common = s1 & s2
s1 = s1 - (common)
s2 = s2 - (common)
print(f"After removing common element: \ns1 = {s1}\ns2 = {s2}")