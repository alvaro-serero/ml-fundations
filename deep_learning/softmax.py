"""Softmax Activation Function"""
import math


def softmax(scores: list[float]) -> list[float]:
    m = max(scores)
    exps = [math.exp(v - m) for v in scores]
    total = sum(exps)

    return [e / total for e in exps]


print([round(x, 4) for x in softmax([1, 2, 3])])
print([round(x, 4) for x in softmax([1, 1, 1])])
print([round(x, 4) for x in softmax([-1, 0, 5])])
print([round(x, 4) for x in softmax([1000, 2000, 3000])])
