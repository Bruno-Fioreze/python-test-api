
## Passos para executar a aplicação.
Caso esteja utilizando windows troque o python3 por python.

- Entre na pasta do projeto.
- Execute o comando python3 -m venv venv.
- Execute o comando pip install -r requirements.txt.
- No caso do linux, ative a venv com source venv/bin/activate.
- No caso do windows, ative a venv com venv/Scripts/Activate.
- Execute o comando python3 manage.py runserver 127.0.0.1:5000.

## Exemplos:
- Entrada
	> http://127.0.0.1:8000/000.000.000-99/
- Saída	
	> {"status": "FREE"}
	
## Comandos para executar os testes.
	> python3 manage.py test validator.tests.TestUtilsValidator
	> python3 manage.py test validator.tests.TestValidatorAPI
	> python3 manage.py test validator.tests.TestValidatorAPI.test_call_end_point_return_200_if_cpf_exist_in_archive
	
## Um pouco sobre a aplicação.
A aplicação foi feita utilizando Python, Django, Django-Rest, Pandas e unittest (TDD).
Ela é bem simples e todo o código desenvolvido se encontra no app validator.