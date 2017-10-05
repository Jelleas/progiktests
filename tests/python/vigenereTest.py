import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

@t.test(0)
def keya(test):
    def testMethod():
        import sys
        sys.argv = ["vigenere.py", "a"]
        output = lib.outputOf(
            _fileName,
            stdinArgs = ["a"],
            overwriteAttributes = [("__name__", "__main__")]
        )
        line = lib.getLine(output, 0)
        return asserts.contains(line, "a")

    test.test = testMethod
    test.description = lambda : "encrypts a as a using a as keyword"

@t.test(10)
def keybaz(test):
    def testMethod():
        import sys
        sys.argv = ["vigenere.py", "baz"]
        output = lib.outputOf(
            _fileName,
            stdinArgs = ["barfoo"],
            overwriteAttributes = [("__name__", "__main__")]
        )
        line = lib.getLine(output, 0)
        return asserts.contains(line, "caqgon")

    test.test = testMethod
    test.description = lambda : "encrypts barfoo as caqgon using baz as keyword"

@t.test(20)
def keyBaZ(test):
    def testMethod():
        import sys
        sys.argv = ["vigenere.py", "BaZ"]
        output = lib.outputOf(
            _fileName,
            stdinArgs = ["BaRFoo"],
            overwriteAttributes = [("__name__", "__main__")]
        )
        line = lib.getLine(output, 0)
        return asserts.contains(line, "CaQGon")

    test.test = testMethod
    test.description = lambda : "encrypts BaRFoo as CaQGon using BaZ as keyword"

@t.test(30)
def keyBAZ(test):
    def testMethod():
        import sys
        sys.argv = ["vigenere.py", "BAZ"]
        output = lib.outputOf(
            _fileName,
            stdinArgs = ["BARFOO"],
            overwriteAttributes = [("__name__", "__main__")]
        )
        line = lib.getLine(output, 0)
        return asserts.contains(line, "CAQGON")

    test.test = testMethod
    test.description = lambda : "encrypts BARFOO as CAQGON using BAZ as keyword"

@t.test(40)
def weirdCharacters(test):
    def testMethod():
        import sys
        sys.argv = ["vigenere.py", "baz"]
        output = lib.outputOf(
            _fileName,
            stdinArgs = ["world!$?"],
            overwriteAttributes = [("__name__", "__main__")]
        )
        line = lib.getLine(output, 0)
        return asserts.contains(line, "xoqmd!$?")

    test.test = testMethod
    test.description = lambda : "encrypts world!$? as xoqmd!$? using baz as keyword"

@t.test(50)
def invalidInput(test):
    def testMethod():
        import sys
        sys.argv = ["vigenere.py"]
        output = lib.outputOf(
            _fileName,
            stdinArgs = ["foo"],
            overwriteAttributes = [("__name__", "__main__")],
            ignoreExceptions = [SystemExit]
        )
        line = lib.getLine(output, 0)
        return asserts.contains(line, "usage: python vigenere.py keyword")

    test.test = testMethod
    test.description = lambda : "handles lack of argv[1]"

@t.test(60)
def tooMuchInput(test):
    def testMethod():
        import sys
        sys.argv = ["vigenere.py", "foo", "bar"]
        output = lib.outputOf(
            _fileName,
            stdinArgs = ["foo"],
            overwriteAttributes = [("__name__", "__main__")],
            ignoreExceptions = [SystemExit]
        )
        line = lib.getLine(output, 0)
        return asserts.contains(line, "usage: python vigenere.py keyword")

    test.test = testMethod
    test.description = lambda : "handles len(argv) > 2"
