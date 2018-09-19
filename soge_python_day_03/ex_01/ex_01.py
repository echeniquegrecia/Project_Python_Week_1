#!/usr/bin/python3

def repeat_me(n):
    def decorator(func_to_execute):
        def func_modified():
            for i in range(0,n):
                func_to_execute()
        return func_modified
    return decorator    

@repeat_me(2)
def test(): 
    print("hello")