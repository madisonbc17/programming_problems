import time

final_count = 1000
final_sum = 0
add = False

while final_count > 0:
    final_count = final_count - 1
    print(final_count)
    
    if final_count % 5 == 0:
        add = True

    elif final_count % 3 == 0:
        add = True

    else:
        add = False
    if add == True:
        final_sum += final_count

    
    add = False

print(final_sum)