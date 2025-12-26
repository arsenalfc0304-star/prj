def test_log(capsys):
    captured = capsys.readouterr()
    assert captured.out == "Hello, world!\n"