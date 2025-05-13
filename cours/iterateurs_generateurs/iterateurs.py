# # iterable __iter__()
# fruits = ["pomme", "banane", "kiwis"]

# print(type(fruits.__iter__()))
# print(type(fruits.__iter__().__next__()))

# for (i, fruit) in enumerate(fruits):
#     print(f"Fruit n°{i} :", fruit)

# # iter

# # it = iter(fruits)
# # print(next(it))
# # print(next(it))
# # print(next(it))

# # print(next(it))

# # it = iter(fruits)
# # for _ in range(4):
# #     print(next(it))

# it = iter(fruits)
# while True:
#     try:
#         next(it)
#     except StopIteration:
#         break

# Iterateur
class Compteur:
    def __init__(self, max: int) -> None:
        self.max = max
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if (self.current < self.max):
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration


c = Compteur(5)

# for i in Compteur(5):
#     print(i)

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

"FAC-002"
"FAC-003"
"FAC-004"
"FAC-005"