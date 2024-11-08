#include <npe.h>
#include <iostream>


npe_function(foo)
npe_arg(X, sparse_double)
npe_begin_code()
{
    return pybind11::none();
}
npe_end_code()
