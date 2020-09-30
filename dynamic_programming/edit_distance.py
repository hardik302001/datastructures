# URL: https://practice.geeksforgeeks.org/problems/edit-distance/0
# Edit Distance

# Optimizing the code
def optimize_edit(S, i, T, j):
    dist = [[x for x in range(j+1) ] for x in range(i+1)]

    for i in range(i+1):
        for j in range(j+1):
            if i == 0:
                dist[i][j] = j
            elif j == 0:
                dist[i][j] = i
            elif S[i-1] == T[j-1]:
                dist[i][j] = dist[i-1][j-1]
            else:
                dist[i][j] = 1 + min(dist[i-1][j-1], dist[i-1][j], dist[i][j-1])

    for x in dist:
        for j in x:
            print j,
        print
    return dist[len(S)][len(T)]




# Recursive soliution for the problem which takes more time than expected.
# Calculates sub-problems again and again
def edit(S, i, T, j):
    if i == 0:
        return j-i
    if j == 0:
        return i - j
    if S[i] == T[j]:
        return edit(S, i-1, T, j-1)
    if S[i] != T[j]:
        return 1 + min(edit(S, i-1, T, j-1), edit(S, i-1, T, j), edit(S, i, T, j-1))
        
# t - number of test cases
# i, j - length of the two strings S and T
# S needs to be converted to T
# S, T - the two strings as input
t = int(input())
while (t > 0):
    t -= 1
    i = int(input())
    j = int(input())
    S = input()
    T = input()
    # p is the function call to function edit
    p = edit(S, i-1, T, j-1)
    print(p)
    # p_dash is the function call to function optimize_edits
    p_dash = optimize_edit(S, i, T, j)
    print (p_dash)
    
