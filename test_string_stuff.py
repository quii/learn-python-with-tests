def test_string_things():
    assert "poo".upper() == "POO"
    assert "BUM".lower() == "bum"

    age = 38
    assert "you are " + str(age) + " years old" == "you are 38 years old"
