# Which of the following are equivalent to O(N)
# 1. O(N + P), where P < N/2 --> O(N) becaue P has to be smaller than N/2, its a constant we can drop
# 2. O(2N) -> O(n) because we can drop constants
# 3. O(N + logN) -> O(N) because O(N) is dominant
# 4. O(N + NlogN) -> O(NlogN) because O(NlogN) is dominant
# 5. O(N+M) stays the same becuase we dont know M