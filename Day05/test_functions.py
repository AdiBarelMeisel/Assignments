#Test that the fuctions run well.
import CountDay05

def test_chars_counter():
    assert CountDay05.chars_number("1!aaTT5!wrts") == 12
    assert CountDay05.chars_number(" ") == 1
    assert CountDay05.chars_number("") == 0

def test_lines_counter():
    assert CountDay05.lines_number("") == 0
    assert CountDay05.lines_number("dfdsf\ndfsd") == 2

def test_words_counter():
    assert CountDay05.words_number("sfsdfsdfsd") == 1
    assert CountDay05.words_number("sfsdf sdfsd") == 2
    assert CountDay05.words_number("") == 0

if __name__ == "__main__":
    test_chars_counter()
    test_lines_counter()
    test_words_counter()
    print("tests succesfully passed")



    
