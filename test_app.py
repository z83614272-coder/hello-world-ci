from app import hello

def test_default_hello():
    assert hello() == "Hello, World!"

def test_custom_hello():
    assert hello("ChatGPT") == "Hello, ChatGPT!"
