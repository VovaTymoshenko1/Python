Python 3.9.8 (tags/v3.9.8:bb3fdcf, Nov  5 2021, 20:48:33) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
def proterm(i, value, x):
    pro = 1;
    for j in range(i):
        pro = pro * (value - x[j]);
    return pro;

def dividedDiffTable(x, y, n):
    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) /
                       (x[j] - x[i + j]));
    return y;

def applyFormula(value, x, y, n):
    sum = y[0][0];

    for i in range(1, n):
        sum = sum + (proterm(i, value, x) * y[0][i]);

    return sum;

n = 5;
y = [[0 for i in range(10)]
     for j in range(10)];
x = [3.5, 3.55, 3.6, 3.65, 3.7];

y[0][0] = 33.1154
y[1][0] = 34.8133
y[2][0] = 36.5982
y[3][0] = 38.4747
y[4][0] = 40.4473

y = dividedDiffTable(x, y, n);

value = 3.643;

print("\nValue at", value, "is",
      round(applyFormula(value, x, y, n), 2))
