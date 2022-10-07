import re


class FunctionParam:

    def __init__(self, param_type, param_name):
        self.type = param_type
        self.name = param_name


class Function:

    def __init__(self, name, return_type, params):
        self.name = name
        self.return_type = return_type
        self.params = params


def parse(file_name: str):
    file = open(file_name)
    result = []

    found_func = False
    function = ""
    wrong_char_pattern = re.compile(r"[\{\=\-\!\/\#]|static")

    for line in file:
        res = wrong_char_pattern.search(line)
        line = line.replace('\n', '').replace('\t', '')

        if res is not None:
            continue

        if "(" in line and ")" in line:
            function += line
            result.append(function)
            function = ""
            found_func = False

        elif "("  in line:
            function += line
            found_func = True

        elif  ")" in line and found_func == True:
            found_func = False
            function += line
            function = " ".join(function.split())
            result.append(function)
            function = ""

        elif found_func == True:
            function += line

    return result


def get_function_list(function_list: list):
    result = []

    for func_str in function_list:
        func_without_br = func_str.split("(")[0].split(' ')
        return_type = func_without_br[0]
        function_name = func_without_br[1]
        function_params_list = []
        raw_params = func_str.split("(")[1].split(",")

        for param in raw_params:
            param = " ".join(param.replace(")", '').replace(";", '').split())

            if len(param) > 0 and param != 'void':
                param = param.split(' ')
                function_param = FunctionParam(param[0], param[1])
                function_params_list.append(function_param)

        func = Function(function_name, return_type, function_params_list)

        result.append(func)

    return result
