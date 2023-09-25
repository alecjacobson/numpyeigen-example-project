#include <npe.h>
#include <iostream>


const char* example_function_doc = R"igl_Qu8mg5v7(
Simple example function that returns its input
)igl_Qu8mg5v7";
npe_function(example_function)
npe_doc(example_function_doc)
npe_arg(A_cpp, dense_float, dense_double)
npe_arg(B_cpp, npe_matches(A_cpp))
npe_begin_code()
std::cout<<"B_cpp:\n"<<B_cpp<<std::endl;
npe_end_code()
