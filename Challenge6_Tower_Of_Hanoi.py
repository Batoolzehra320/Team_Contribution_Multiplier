def towerOfHanoi(N, from_rod, to_rod, aux_rod):
    if N == 1:
        print(f"Disk 1 moved from {from_rod} to {to_rod}")
        return
    towerOfHanoi(N - 1, from_rod, aux_rod, to_rod)
    print(f"Disk {N} moved from {from_rod} to {to_rod}")
    towerOfHanoi(N - 1, aux_rod, to_rod, from_rod)
towerOfHanoi(8,"A","B","C")