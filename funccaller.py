class CallKeeper:
    def __init__(self):
        self.funcs = {}

    def addfunc(self,name):
        def wrapper(func):
            self.funcs[name] = func
            return func
        return wrapper

    def callfunc(self,name):
        return self.funcs[name]()


app = CallKeeper()

@app.addfunc('foo')
def hello():
    print('Hello world')


app.callfunc('foo')
