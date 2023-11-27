from flet import *
import sqlite3
conn = sqlite3.connect('banco_dados/db_cad.db',check_same_thread=False)

def main(page:Page):
    page.window_width=400
    page.window_height =350
    page.title= 'Tela de Login'
    page.vertical_alignment= CrossAxisAlignment.CENTER
    page.theme_mode='light'
    page.window_center()
    pass

    #Fecha popup de confirmação de operações realizadas
    def close_popUp(e):
        popUp.open=False
        popUp.update()
    # popup de confirmação - operações realizadas
    popUp = AlertDialog(
        modal=True,
        actions=[OutlinedButton('OK', on_click=close_popUp)])
    #Funcao que limpa os campos(usuário e senha)
    def limpa_campos():
        user.value=''
        senha.value = ''
    #verifica se usuário está cadastrado e se a senha coincide com a informada
    def sucesso_login():
        page.dialog = popUp
        popUp.title= Text('Bem Vindo')
        popUp.content=Text(f'Olá {user.value}.\nLogin Realizado com Sucesso!',size=18)
        popUp.open = True
        limpa_campos()
        page.update()
        logado.visible =True
        logado.update()
        inicial.visible = False
        inicial.update()
    # verifica se o usuário(login) está cadastrado
    def erro_user():
        page.dialog = popUp
        popUp.title= Text('ERRO!!')
        popUp.content=Text('Usuário não cadastrado!',size=18)
        popUp.open = True
        limpa_campos()
        page.update()
    # funçao abre popup de erro de senha
    def erro_senha():
        page.dialog = popUp
        popUp.title= Text('ERRO!!')
        popUp.content=Text('Senha Inválida!',size=18)
        popUp.open = True
        limpa_campos()
        page.update()
    # fecha a janela e encerra a aplicação
    def close_page(e):
        page.window_close()
    #Busca para ver se o usuário se encontra cadastrado no banco de dados
    def busca(nome, senha):
        c = conn.cursor()
        c.execute(f'SELECT * FROM users WHERE user = "{nome}"')
        saida = c.fetchall()
        if len(saida) != 0:
            if saida[0][2] == senha:
                sucesso_login()
            else:
                erro_senha()
        else:
            erro_user()
    
    # Usuário e senha usados na tela de login 
    user = TextField(label='Usuário',icon=icons.SUPERVISED_USER_CIRCLE, width=300,height=35)
    senha = TextField(label='Senha',password=True, height=35, width=300, icon=icons.LOCK)
    
    def logar(e):
        busca(user.value,senha.value)
        #open_popUp()             
    
    #usuário e senha usados no cadastro de novo usuário
    novo_usuario = TextField(label='Novo Usuário')
    nova_senha = TextField(label='Nova Senha', password=True)
    def novo_cadastro(e):
        cadastro.visible=True
        cadastro.update()
    # cadastra novo usuario que poderá efetuar login
    def cadastro(e):
        usuario = novo_usuario.value
        senha = nova_senha.value
        c = conn.cursor()
        comando = f'INSERT INTO users (user, senha) VALUES ("{usuario}", "{senha}")'
        c.execute(comando)
        conn.commit()
        conn.close
        novo_usuario.value = nova_senha.value = ''
        page.update()
        popUp.title=Text('Sucesso')
        popUp.content=Text('Cadastro Realizado com sucesso!!!', size=18)
        popUp.open=True
        popUp.update()
        print('OK')
    # Volta a página inicial da aplicação(login)
    def page_inicial(e):
        logado.visible=False
        cadastro.visible = False
        inicial.visible=True
        page.update()
    #Fecha a pagina de cadastro e vai para o menu
    def voltar(e):
        cadastro.visible = False
        page.update()
    #container da tela apresentada apos o login
    logado = Container(Row([OutlinedButton('Cadastrar Novo Usuário', on_click=novo_cadastro),
            OutlinedButton('LogOut', on_click=page_inicial) 
           ])
       )  
    logado.visible =False # inicia nao visivel
    # container tela de cadastro de novo usuario
    cadastro = Container(Column([
        novo_usuario, nova_senha,
        Row([ElevatedButton('Cadastrar', on_click=cadastro), ElevatedButton('Voltar', on_click=voltar)
             ])
        ])
    )
    cadastro.visible=False# inicia nao visivel
    # container tela da tela de inicio do programa
    inicial = container =(
        Column([Text('Login de Usuário', size=20, width=800, weight='bold', text_align='center'),
            user, senha,
            Row([ElevatedButton('SAIR', on_click=close_page,icon= icons.CLOSE_OUTLINED),
                 ElevatedButton('LogIn',icon='login', on_click=logar)],spacing=20, alignment= MainAxisAlignment.CENTER)],
                MainAxisAlignment.CENTER, spacing=20)

    )

    #Adicionando os containers a pagina
    page.add(Text('', height=15),inicial,logado, cadastro
        
    )   
    page.update()
    

app(target=main)