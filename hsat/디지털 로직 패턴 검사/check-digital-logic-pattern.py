import sys
input = sys.stdin.readline

digital_logic = input().strip()
K, M = map(int, input().split())

N = len(digital_logic)
if N < K:
    print(0)
    sys.exit()

current_hash = int(digital_logic[:K], 2)
counts = {current_hash: 1}

mask = (1 << K) - 1

for i in range(1, N - K + 1):
    new_bit = int(digital_logic[i + K - 1])
    
    current_hash = ((current_hash << 1) & mask) | new_bit
    
    counts[current_hash] = counts.get(current_hash, 0) + 1
    
    if counts[current_hash] >= M:
        print(1)
        sys.exit()

print(0)