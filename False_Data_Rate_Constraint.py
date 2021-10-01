# Find the largest k such that p(k) <= k/m * alpha
p_values = [0.007,0.004,0.01,0.0027,.017,0.08,.0054,0.033,0.017,0.08,.0054,0.033,.06,.08,.1]
sorted_pv = sorted(p_values)
alpha = 0.05
m = len(p_values)

print(sorted_pv)
k = 0
for pv in sorted_pv:
    if pv <= ((k+1) * alpha / m):
        k += 1
        print("Contraint passed: ",k * alpha / m)
        continue
    else:
        break
print("Soln for k: ",k)
print("Contraint Reached: ",k * alpha / m)
for i in range(0,k):
    print(sorted_pv[i])

    

