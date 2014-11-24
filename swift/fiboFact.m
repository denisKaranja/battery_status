func fibonacci(numbers: Int)->Int
{
    if numbers == 1 || numbers == 0
    {
        return 1
    }
    else
    {
        return fibonacci(numbers - 1) + fibonacci(numbers - 2)
    }
}

func factorial(number: Int)->Int
{
    if number == 0 || number == 1
    {
        return 1
    }
    else
    {
        return number * factorial(number - 1)
    }
}

println("Fibonacci 10 is ",fibonacci(10))

println("Factorail 5 is ",factorial(5))