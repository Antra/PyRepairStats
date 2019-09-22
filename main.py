import matplotlib.pyplot as plt
import random

# set the basic behaviour
a = b = 0
cut_a = cut_b = 11
n = 10000
p = 1/3
array = []


# how many simulations?
i = 0
while i < n:
    # remember to reset a and b between simulation
    a = b = 0
    # run each simulation until either a or b reaches the cut-off
    while a < cut_a and b < cut_b:
        # it doesn't matter if it's a or b that has probability p, as long as we're consistent
        x = random.random()
        if x >= p:
            a = a + 1
        else:
            b = b + 1
        # if either a or b reaches the cut-off, then add the number of the other part to the array
        if a == cut_a:
            array.append(b)
        elif b == cut_b:
            array.append(a)
    # and then increment to the next simulation run
    i = i + 1

# calculate the frequencies
frequency = {}
for item in array:
    if (item in frequency):
        frequency[item] += 1
    else:
        frequency[item] = 1
sorted_freq_val = sorted(frequency.items(), key=lambda x: x[1])
sorted_freq_ord = sorted(frequency.items(), key=lambda x: x)
print(sorted_freq_val)
print(sorted_freq_ord)

# display the distribution
bins = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
plt.hist(array, bins=bins)
plt.title(
    "Histogram of the parts we didn't need,\nnumber of runs: {}".format(str(n)))
plt.xlabel("Number of parts used when we ran out of the other part")
plt.ylabel("Frequency")
plt.show()
