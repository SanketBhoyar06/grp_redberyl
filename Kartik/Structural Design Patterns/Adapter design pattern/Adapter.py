class A:
    def __init__(self) -> None:
        pass

    def methodA(self, method):
        self.methodA = method

class B:
    def __init__(self) -> None:
        pass

    def methodB(self, method):
        self.methodB = method

class C:
    def __init__(self) -> None:
        pass

    def instanceC(self, B):
        self.instanceC = B
        