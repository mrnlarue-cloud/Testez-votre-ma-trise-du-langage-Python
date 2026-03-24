def log_decorator(func):
    def wrapper():
        print("Avant l'exécution")
        func()
        print("Après l'exécution")

    return wrapper


@log_decorator
def function_test():
    print("Cette fonction ne prend pas d'arguments.")


function_test()
