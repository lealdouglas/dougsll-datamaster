import pytest

from definition_project.main import main


def test_main(capsys):
    # Chama a função main
    main()
    # Captura a saída padrão
    captured = capsys.readouterr()
    # Verifica se a saída é 'hello world\n'
    assert captured.out == 'hello world\n'
