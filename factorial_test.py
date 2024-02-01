from factorial import factorial

def test_factorial():
    assert factorial(8) == 40320
    assert factorial(18) == 6402373705728000
    assert factorial(45) == 119622220865480194561963161495657715064383733760000000000
    assert factorial (-17) == "Factorials don't work for negative numbers"
    assert factorial(0) == 1
















# print(factorial(8) == 40320)
# print(factorial(18) == 6402373705728000)
# print(factorial(45) == 119622220865480194561963161495657715064383733760000000000)
# Test how high of a number your program can calculate. Can you push it further?
