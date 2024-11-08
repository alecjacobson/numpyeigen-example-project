import numpy as np
import my_module
import time
import scipy.sparse
# timing
import time

def rand_sparse(n,density):
    n_features = n
    n_samples = n
    rng1 = np.random.RandomState(42)
    rng2 = np.random.RandomState(43)

    nnz = int(n_samples*n_features*density)

    row = rng1.randint(n_samples, size=nnz)
    cols = rng2.randint(n_features, size=nnz)
    data = rng1.rand(nnz)

    S = scipy.sparse.csc_matrix((data, (row, cols)), shape=(n_samples, n_features))
    return S

for p in range(2,8):
    n = 10**p
    S = rand_sparse(n,1.0/(n))
    my_module.foo(S)
    start = time.time()
    for i in range(10):
        my_module.foo(S)
    end = time.time()
    t = (end - start)/10
    print("%10d %f" % (n,t))
