import c_header_parser as chp
import cpp_gtest_mock_generator as cpp_mock_gen


MODULE_NAME = "test_file.h"


def main():
    file_name = MODULE_NAME

    result = chp.parse(file_name)

    for f in result:
        print(f)

    res = chp.get_function_list(result)

    cpp_mock_gen.generate_mock(file_name.split('.')[0], res)


if __name__ == '__main__':
    main()
