import ctypes

lib = ctypes.cdll.LoadLibrary("./library.so")

def test_go_add():
    assert lib.add(1, 2) == 3

if __name__ == "__main__":
    test_go_add()
    print("All tests passed!")
