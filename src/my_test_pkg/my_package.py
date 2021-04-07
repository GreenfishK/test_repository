import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


def my_method():
    print("The packaging, building and installation worked out "
          "fine and this package is accessible within the conda 'uni' environment")

    a = np.random.normal(0, 100, 10)
    b = np.random.normal(0, 100, 10)
    inp = zip(a, b)

    df = pd.DataFrame(inp, columns=['a', 'b'])

    df.plot()
    plt.show()


