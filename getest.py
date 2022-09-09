


def counter():
    return [1, 2, 3]


def counter_generator():
    for number in [1, 2, 3]:
        yield number

print(counter())
generator = counter_generator()

print(generator.__iter__().__next__())
print(generator.__iter__().__next__())