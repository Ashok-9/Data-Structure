def count_monsters_after_each_hero(A, B):
    # Create a list to store the number of monsters left after each hero
    result = []
    # Iterate through each hero
    for i in range(len(B)):
        # Get the position and strength of the current hero
        pos, strength = B[i][0], B[i][1]
        # Count the number of monsters at the hero's position and having strength less than the hero's strength
        count = 0
        for j in range(len(A)):
            if A[j][0] <= pos and A[j][1] >= pos and A[j][2] < strength:
                count += A[j][1] - pos + 1
        # Remove the monsters that the hero has defeated from the array A
        A = [m for m in A if not(A[j][0] <= pos and A[j][1] >= pos and A[j][2] < strength)]
        # Add the count of remaining monsters to the result list
        result.append(sum([A[j][1] - A[j][0] + 1 for j in range(len(A))]))
    return result


A = [[1,3,7],[2,5,4],[4,8,6]]
B = [[3,5],[5,8]]
print(count_monsters_after_each_hero(A,B))