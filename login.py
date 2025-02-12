import streamlit as st
import secrets as secrets

# Função para validar o login
def validar_login(username, password):
    # Recupera as credenciais do secrets.toml
    usuario_correto = st.secrets["login"]["username"]
    senha_correta = st.secrets["login"]["password"]
    
    # Verifica se as credenciais estão corretas
    if username == usuario_correto and password == senha_correta:
        return True
    else:
        return False

# Tela de login
def tela_de_login():
    st.title("Login")
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    
    if st.button("Login"):
        if validar_login(username, password):
            st.success("Login realizado com sucesso!")
            # Aqui você pode redirecionar para outra página ou executar outras ações
            st.session_state['logado'] = True
        else:
            st.error("Usuário ou senha incorretos")

# Verifica se o usuário está logado
if 'logado' not in st.session_state:
    st.session_state['logado'] = False

if not st.session_state['logado']:
    tela_de_login()
else:
    st.write("Bem-vindo à aplicação!")
    # Aqui você pode colocar o conteúdo da sua aplicação