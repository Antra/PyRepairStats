import matplotlib.pyplot as plt
import random


n = 10000
a = b = 0
cut_a = cut_b = 11
p = 1/3
array = []
i = 0


while i < n:
    a = b = 0
    while a < cut_a and b < cut_b:
        x = random.random()
        if x >= p:
            a = a + 1
        else:
            b = b + 1
        if a == 11:
            array.append(b)
        elif b == 11:
            array.append(a)
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

bins = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
plt.hist(array, bins=bins)
plt.title(
    "Histogram of the parts we didn't need,\nnumber of runs: {}".format(str(n)))
plt.xlabel("Number of parts used when we ran out of the other part")
plt.ylabel("Frequency")
plt.show()
