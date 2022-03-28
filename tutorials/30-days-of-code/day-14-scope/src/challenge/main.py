class Difference:

    def __init__(self, numbers):
        self.__elements = numbers
        self.deltas = set()
        self.maximumDifference = 0

    def computeDifference(self):

        offset = 1

        for num1 in self.__elements[:-1]:
            for num2 in self.__elements[offset:]:
                diff = abs(num1 - num2)
                self.deltas.add(diff)
            offset += 1

        self.maximumDifference = sorted(list(self.deltas))[-1]


# End of Difference class

_ = input()
a = [int(e) for e in input().split(" ")]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
