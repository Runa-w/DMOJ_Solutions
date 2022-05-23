N = int(input())

intro1 = 'A long time ago in a galaxy ' + ('far, ' * (N - 1)) + 'far away...'

intro2 = 'A long time ago in a galaxy ' + ('far ' * N) + 'away...'

if N > 1:
    print(intro1)
else:
    print(intro2)
