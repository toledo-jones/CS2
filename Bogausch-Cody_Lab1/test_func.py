def test_function():
    print("hello world")


def execute_function(function):
    print(function)
    # This line will error:
    function()  # NoneType is not callable

execute_function(test_function())