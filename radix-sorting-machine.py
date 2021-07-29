from queque import Queue
import math

def radix(input):
    main = Queue()
    bins = [Queue() for i in range(10)]
    top = max(input)
    list = []
    count = 0
    num_digits = int(math.log10(top))+1

    for x in input:
        main.enqueue(x)

    while count < num_digits:
        num = main.dequeue()
        if count == 0:
            var = num % 10
            bins[var].enqueue(num)
        else:
            x = 10 ** count
            var = num // x
            var = var % 10
            bins[var].enqueue(num)
        if main.is_empty():
            for i in range (10):
                while not bins[i].is_empty():
                    x = bins[i].dequeue()
                    main.enqueue(x)
            count += 1

    size = main.size()
    for i in range(main.size()):
        x = main.dequeue()
        list.append(x)

    print(list)

radix([10,21,17,34,1000,44,11, 700,654,123])
