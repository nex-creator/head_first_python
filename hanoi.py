def hanoi_solver(n):
    rods = [list(range(n, 0, -1)), [], []]  # Initial state
    moves = [f"{rods[0]} {rods[1]} {rods[2]}"]  # Store initial state

    def move(num_disks, source, target, auxiliary):
        if num_disks == 0:
            return
        # Step 1: Move n-1 disks from source to auxiliary
        move(num_disks - 1, source, auxiliary, target)
        # Step 2: Move the nth disk from source to target
        rods[target].append(rods[source].pop())
        moves.append(f"{rods[0]} {rods[1]} {rods[2]}")
        # Step 3: Move n-1 disks from auxiliary to target
        move(num_disks - 1, auxiliary, target, source)

    # Start moving n disks from rod 0 (left) to rod 2 (right) using rod 1 (middle)
    move(n, 0, 2, 1)

    return "\n".join(moves)

print(hanoi_solver(5))