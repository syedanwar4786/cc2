class BankersAlgorithm:
  def __init__(self, available_resources, max_resources, allocation):
    self.available_resources = available_resources
    self.max_resources = max_resources
    self.allocation = allocation
    self.num_processes = len(allocation)
    self.num_resources = len(available_resources)

  def is_safe_state(self):
    work = self.available_resources.copy()
    finish = [False] * self.num_processes
    safe_sequence = []
    for _ in range(self.num_processes):
      for i in range(self.num_processes):
        if not finish[i] and all(work[j] >= self.allocation[i][j] for j in range(self.num_resources)):
          safe_sequence.append(i)
          work = [work[j] + self.allocation[i][j] for j in range(self.num_resources)]
          finish[i] = True
          break

      if all(finish):
        print("Safe sequence:", safe_sequence)
        return True
    print("The system is in an unsafe state.")
    return False

allocation_matrix = [[0,1,0],[2,0,0],[3,0,2],[2,1,1],[0,0,2]]
max_matrix = [[7,5,3],[3,2,2],[9,0,2],[2,2,2],[9,3,3]]
available_resources = [3,3,2]
banker = BankersAlgorithm(available_resources, max_matrix, allocation_matrix)
banker.is_safe_state()