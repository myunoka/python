def foo():
    try:
        print(1)
        return 'ok'
        print(2)

    except:
        pass
    else:
        print('结束')
    finally:
        print('hhhh')
a = foo()
print(a)