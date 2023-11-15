import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import os
#symbolic var
x, y = sp.symbols('x y')



functions = [
    (5*x**3 - 2*x**2 + 3*x - 17,"5x3.dat"),
    (sp.sin(x) + sp.cos(x),"sinxcosx.dat"),
    (2*sp.ln(x+1),"2ln.dat"),
    (x + 2*y,"x2y.dat"),
    (sp.sin(x/2) + 2*sp.cos(x),"sinx2.dat"),
    (x**2 + 3*x*y - 7*y + 1,"23xy.dat"),
]
def generator_single(t, dom, path):
    domain = np.arange(dom[0], dom[1], 0.1)
    func, name = t
    x = str(dom[0]) + str(dom[1])
    filename = name.replace("-", "_")
    with open(os.path.join(path, x + filename), "w") as f:
        f.write("1 100 -5 5 101\n")
        for i in domain:
            result = func(i)
            f.write(f"{i} {result}\n")


def gen_multi(t, dom, path):
    domain = np.arange(dom[0], dom[1], 0.1)
    func, name = t
    z = str(dom[0]) + str(dom[1])
    filename = name.replace("-", "_")
    with open(os.path.join(path, z + filename), "w") as f:
        f.write("1 100 -5 5 101\n")
        for i in domain:
            for j in domain:
                result = func(i, j)
                f.write(f"{i} {j} {result}\n")

if __name__ == "__main__":
    OUT_PATH = "input"
    # Konwersja funkcji symbolicznych na funkcje numeryczne
    numerical_functions = [(sp.lambdify(x, func), name) for func, name in functions[:3]]
    numerical_functions += [(sp.lambdify((x,y), func), name) for func, name in functions[3:]]
    for old_output in os.listdir(OUT_PATH):
        os.remove(OUT_PATH +"\\"+ old_output)
    for domain in [[-10, 10], [0, 100], [-1, 1], [-1000, 1000]]:
        generator_single(numerical_functions[0], domain, OUT_PATH)

    for domain in [[-3.14, 3.14], [0, 7], [0, 100], [-100, 100]]:
        generator_single(numerical_functions[1], domain, OUT_PATH)

    for domain in [[0, 4], [0, 9], [0, 99], [0, 999]]:
        generator_single(numerical_functions[2], domain, OUT_PATH)
    

    for domain in [[0, 1], [-10, 10], [0, 100], [-1000, 1000]]:
        gen_multi(numerical_functions[3], domain, OUT_PATH)

    for domain in [[-3.14, 3.14], [0, 7], [0, 100], [-100, 100]]:
        gen_multi(numerical_functions[4], domain,  OUT_PATH)

    for domain in [[-10, 10], [0, 100], [-1, 1], [-1000, 1000]]:
        gen_multi(numerical_functions[5], domain,  OUT_PATH)