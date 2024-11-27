import go_add

def test_go_add():
    assert go_add.go_add(1, 2) == 3

if __name__ == "__main__":
    test_go_add()
    print("All tests passed!")
