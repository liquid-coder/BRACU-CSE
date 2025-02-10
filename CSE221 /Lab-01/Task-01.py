import numpy as np
import fhm_unittest as unittest
import numpy as np
def playRight(sequence, beats):
  size1 = sequence.size
  for i in range(size1):
    if beats[i] == 1:
      temp1 = sequence[size1-1]
      for j in range(size1-1,0,-1):
        sequence[j] = sequence[j-1]
      sequence[j-1] = temp1
  return sequence

print("///  Test 01: Play Right  ///")
sequence = np.array([10, 20, 30, 40, 50, 60])
beats = np.array([1, 0, 0, 1, 0, 1])
returned_value = playRight(sequence, beats)
print(f'Task 1: {returned_value}')
