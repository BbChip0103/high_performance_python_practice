def julia_set(coordinates, maxiter, c):
    for z in coordinates:
        for iteration in range(maxiter):
            if abs(z) < 2.0:
                z = z*z + c
                print(z)
            else:
                break
