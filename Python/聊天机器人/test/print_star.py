def title(show = ''):
    def printStar(func):
        def f():
            print(show, '*******')
            return func()
        return f
    return printStar

@title('hello')
def hello():
    return 1 + 1

def main():
    print(hello())

if __name__ == "__main__":
    main()