# FireflyAlgorithm

## CODE EXAPMLE:

```python
def func(x1, x2):
    return x1**2 - x1*x2 + x2**2 + 2*x1 + 4*x2 + 3

#FireflyAlgorithm(D, Lb, Ub, n, alpha, beta0, gamma, theta, iter_max, func)
FA = FireflyAlgorithm(2, -5, 5, 5, 1.0, 1.0, 0.01, 0.97, 50, func)
ans = FA.doRun()
print("Minimal",ans)
```
