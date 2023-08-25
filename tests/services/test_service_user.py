from src.services.service_user import ServiceUser


class TestServiceUser:

    def test_add_user_com_sucesso(self):
        #Setup
        service = ServiceUser()
        resultado_esperado = "Usuário Adalberto adicionado"

        #Chamada
        resultado = service.add_user("Adalberto", "Programador")

        #Avaliação
        assert resultado == resultado_esperado


    def test_add_user_ja_cadastrado(self):
        #Setup
        service = ServiceUser()
        resultado_esperado = "Não é possivel adicionar usuário já cadastrado!"
        service.add_user("Adalberto", "Programador")

        #Chamada
        resultado = service.add_user("Adalberto", "Programador")

        #Avaliação
        assert resultado == resultado_esperado


    def test_add_user_com_parametros_invalidos(self):
        #Setup
        service = ServiceUser()
        resultado_esperado = "Parametros Invalidos"
        service.add_user(1, 2)

        #Chamada
        resultado = service.add_user(1, 2)

        #Avaliação
        assert resultado == resultado_esperado

    def test_add_user_campos_em_branco(self, none=None):
        #Setup
        service = ServiceUser()
        resultado_esperado = "Requer preenchimento dos campos"
        service.add_user(none, none)

        #Chamada
        resultado = service.add_user(none, none)

        #Avaliação
        assert resultado == resultado_esperado


    def test_remover_usuario_cadastrado(self):
        #Setup
        service = ServiceUser()
        resultado_esperado = "Usuário Adalberto removido"
        service.add_user("Adalberto", "Programador")

        #Chamada
        resultado = service.remove_user("Adalberto")

        #Avaliação
        assert resultado == resultado_esperado


    def test_remover_useuario_nao_cadastrado(self):
        #setup
        service = ServiceUser()
        resultado_esperado = "Não foi possível remover o usuário Bento, já que ele não foi encontrado!"
        service.remove_user("Adalberto")

        #Chamada
        resultado = service.remove_user("Bento")

        #Avaliação
        assert resultado == resultado_esperado


    def test_buscar_nome_cadastrado(self):
        #Setup
        service = ServiceUser()
        resutado_esperado = "Usuário Adalberto recuperado!"
        service.add_user("Adalberto", "Programador")

        #Chamda

        resultado = service.get_user("Adalberto")

        #Avaliação
        assert resultado == resutado_esperado

    def test_buscar_nome_nao_cadastrado(self):
        #Setup
        service = ServiceUser()
        resutado_esperado = "Usuário Adalberto, não localizado!"
        service.add_user("Bento", "Contador")

        #Chamda

        resultado = service.get_user("Adalberto")

        #Avaliação
        assert resultado == resutado_esperado