
# Byte code level information

import dis

class A:
    def __init__(self):
        print("A's COnstructor")


class B(A):
    pass



dis.dis(B.__init__)
dis.dis(A.__init__)
