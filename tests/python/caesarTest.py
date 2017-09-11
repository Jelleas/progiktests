import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

@t.test(0)
def key0(test):
    def testMethod():
        import sys
        sys.argv = ["caesar.py", "0"]
        inputArgs = ["def"]
        output = lib.outputOf(_fileName, inputArgs)
        line = lib.getLine(output, 0)
        return asserts.contains(line, "def")

    test.test = testMethod
    test.description = lambda : "encrypt def naar def met key = 0"

@t.test(10)
def key3(test):
    def testMethod():
        import sys
        sys.argv = ["caesar.py", "3"]
        inputArgs = ["abc"]
        output = lib.outputOf(_fileName, inputArgs)
        line = lib.getLine(output, 0)
        return asserts.contains(line, "def")

    test.test = testMethod
    test.description = lambda : "encrypt abc naar def met key = 3"
