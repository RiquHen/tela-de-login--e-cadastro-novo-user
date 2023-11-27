#### Login ####   Python/Flet

único usuário e senha cadastrado(primeiro acesso)

usuario: admin  - senha:admin

- Apresenta uma tela de login(usuario e senha),com os botões de realizar o login ou sair da aplicação

- Banco de dados - pasta banco_dados o arquivo  db_cad.bd, salva o novo usuario e sua senha

Caso o usuario inserido nao esteja salvo no banco de dados(banco_dados/db.cad.db),
o programa abrirá um popup com aviso de 'Usuario não cadastrado'. Caso o usuário esteja cadastrado mas a senha inserida esteja incorreta, tambem abrirá um popup com a informação 'Senha Incorreta'. No caso do usuario e senha conferir com o salvo no db.cad.db, o login será efetuado, e apresetará um popup informando isso.

Após realizar o login, apresenta uma tela com dois botões,
(cadastrar novo usuario)- que abrirá um formulario de novo usuario e nova senha,
para que seja inserido no banco de dados, gerando um novo usuario com acesso a segunda tela.
(logOut) -  volta a tela inicial
