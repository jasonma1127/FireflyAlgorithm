# FireflyAlgorithm

## CODE EXAPMLE:

```python
def test(X, D):
    x1 = X[0]
    x2 = X[1]
    return x1**2 - x1*x2 + x2**2 + 2*x1 + 4*x2 + 3

def RastriginFunc(X, D):
    funsum = 0
    for i in range(D):
        x = X[i]
        funsum += x**2-10*np.cos(2*np.pi*x)
    funsum += 10*D
    return funsum

def StyblinskiTangFunc(X, D):
    funsum = 0
    for i in range(D):
        x = X[i]
        funsum += (x**4) - 16*(x**2) + 5*x
    funsum *= 0.5
    return funsum


#FireflyAlgorithm(D, Lb, Ub, n, alpha, beta0, gamma, theta, iter_max, func)
FA = FireflyAlgorithm(2, -5, 5, 5, 1.0, 1.0, 0.01, 0.97, 1000, test)
ans = FA.doRun()
print("Minimal",ans)
```
