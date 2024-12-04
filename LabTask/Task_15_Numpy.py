import numpy as np
score = np.array([85, 90, 78, 92, 88])

# 1
score_float = score.astype(float)
print("Score as float:", score_float)

# 2
score1 = score.copy()
score1 += 5
print("Score1 with 5 points added:", score1)
print("Original score remains unchanged:", score)

# 3
indices_85_plus = np.where(score >= 85)[0]
print("Indices of students who scored 85 or above:", indices_85_plus)

#4
print("Shape of score:", score.shape)
print("Number of dimensions:", score.ndim)
print("Size of array:", score.size)
print("Item size (in bytes):", score.itemsize)
print("Data type:", score.dtype)
print("Sorted scores:", np.sort(score))
print("Max score:", score.max())
print("Min score:", score.min())
print("Sum of scores:", score.sum())
print("Mean of scores:", score.mean())


print("score[::2]:", score[::2])
print("score[-3:-1]:", score[-3:-1])
print("score[1:4]:", score[1:4])