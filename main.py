import matplotlib.pyplot as plt
import numpy as np

# The quantity of numbers to generate
quantity = 1000000

# The maximum value of the random generated numbers
maxValue = 10000000


print("Generating sorted array of " + str(quantity) + " random numbers between 0 and " + str(maxValue) + "...\n")

randomNumbers = np.random.randint(maxValue, size=quantity)
randomNumbers = np.sort(randomNumbers)

print("Done.\n\n")


print("Generating array of the difference of each number to their predecessor...\n")

difference = np.empty(randomNumbers.size - 1, dtype=int)

for i in range(difference.size):
    difference[i] = abs(randomNumbers[i + 1] - randomNumbers[i])

print("Done.\n\n")


print("Plotting generated data...\n\n")

plt.figure(figsize=(12, 10), dpi=80)
plt.grid(axis='y', alpha=0.75)

plt.xlabel('Difference')
plt.ylabel('Frequency')

plt.title('Difference between each generated value by frequency')

_, counts = np.unique(difference, return_counts=True)
n, bins, patches = plt.hist(difference, bins=len(counts), color='skyblue', alpha=0.7, rwidth=0.95)

maxFrequency = n.max()
plt.ylim(ymax=np.ceil(maxFrequency / 10) * 12 if maxFrequency % 10 else maxFrequency + 10)

plt.show()

print("Done.\n\n")
