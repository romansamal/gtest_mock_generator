from c_header_parser.c_header_parser import FunctionParam
from c_header_parser.c_header_parser import Function

header_include_test_str = """#pragma once
#include <gmock/gmock.h>
#include <gtest/gtest.h>

extern "C"
{
"""


def generate_header_begin(module_name : str):
    mock_file_name = f"{module_name}_mock.hpp"
    f = open(f'{mock_file_name}', 'w')

    f.write(header_include_test_str)
    f.write(f'\t#include "{module_name}.h"\n')
    f.write('}\n\n')

    f.close()


def generate_header_class_interface(module_name : str, func_list: list):
    mock_file_name = f"{module_name}_mock.hpp"
    f = open(f'{mock_file_name}', 'a')

    f.write(f'class {module_name}\n')
    f.write(f'{{\npublic:\n\tvirtual ~{module_name}() = 0;\n\n')

    for func in func_list:
        f.write(f'\tvirtual {func.return_type} {func.name}(')

        if len(func.params) > 0:
            f.write('\n')
            for param in func.params:
                if param == func.params[-1]:
                    f.write(f'\t\t{param.type} {param.name}) = 0;\n\n')
                else:
                    f.write(f'\t\t{param.type} {param.name},\n')
        else:
            f.write(f') = 0;\n\n')

    f.write('};')

    f.close()


def generate_header_class_mock_class(module_name : str, func_list: list):
    mock_file_name = f"{module_name}_mock.hpp"
    mock_class_name = f'{module_name}_mock'
    f = open(f'{mock_file_name}', 'a')
    f.write('\n\n')
    f.write(f'class {mock_class_name} : public {module_name}\n')
    f.write(f'{{\npublic:\n\t~{mock_class_name}() override;\n\n')

    for func in func_list:
        f.write(f'\tMOCK_METHOD{len(func.params)}({func.name},\n\t\t\t\t{func.return_type}(')
        if len(func.params) > 0:
            f.write('\n')
            for param in func.params:
                if param == func.params[-1]:
                    f.write(f'\t\t\t\t{param.type} {param.name}));\n\n')
                else:
                    f.write(f'\t\t\t\t{param.type} {param.name},\n')
        else:
            f.write(f'));\n\n')

    f.write('};\n')

    f.close()


def generate_cpp_class_mock(module_name: str, func_list: list):
    mock_file_name = f"{module_name}_mock.cpp"
    mock_class_name = f'{module_name}_mock'
    f = open(f'{mock_file_name}', 'w')
    f.write(f'#include "{mock_class_name}.hpp"\n\n')
    f.write(f'namespace mock_objects\n{{\n\textern std::unique_ptr<{mock_class_name}> {module_name}Mock;\n}};\n\n')

    f.write(f'{module_name}::~{module_name}()\n{{}}\n\n')
    f.write(f'{mock_class_name}::~{mock_class_name}()\n{{}}\n\n')

    for func in func_list:
        f.write(f'{func.return_type} {func.name}(')

        if len(func.params) > 0:
            f.write(f'\n')
            for param in func.params:
                if param != func.params[-1]:
                    f.write(f'\t{param.type} {param.name},\n')
                else:
                    f.write(f'\t{param.type} {param.name})\n')
        else:
            f.write(f')\n')

        f.write(f'{{\n\treturn mock_objects::{module_name}Mock->{func.name}(')

        if len(func.params) > 0:
            for param in func.params:
                if param != func.params[-1]:
                    f.write(f'{param.name}, ')
                else:
                    f.write(f'{param.name});\n')
        else:
            f.write(f');\n')


        f.write(f'}}\n\n')

    f.close()


def create_mock_header(module_name : str, func_list: list):
    generate_header_begin(module_name)
    generate_header_class_interface(module_name, func_list)
    generate_header_class_mock_class(module_name, func_list)


def generate_mock(module_name : str, func_list: list):
    create_mock_header(module_name, func_list)
    generate_cpp_class_mock(module_name, func_list)
