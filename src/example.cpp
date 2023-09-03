#include <npe.h>
#include <iostream>


const char* example_function_doc = R"igl_Qu8mg5v7(
Simple example function that returns its input
)igl_Qu8mg5v7";
npe_function(example_function)
npe_arg(in1, dense_int32, dense_int64)
npe_arg(in2, npe_matches(in1))
npe_doc(example_function_doc)
npe_begin_code()
{
    std::cout << "sizeof(in1[0])*8: " << sizeof(in1[0])*8 << std::endl;
    std::cout << "sizeof(in2[0])*8: " << sizeof(in2[0])*8 << std::endl;
    return std::make_tuple(npe::move(in1), npe::move(in2));
}
npe_end_code()
