from src.models import user
from src.models.store import Store
from src.models.user import User


class ServiceUser:
    def _init_(self):
        self.store = Store()

    def validando_se_existe_usuario(self, name):
        lista = self.store.bd

        if len(lista) >= 1:
            for i in range(len(lista)):
                if lista[i].name == name:
                    return True

    def add_user(self, name, job):
        if name is not None and job is not None:
            if isinstance(name, str) and isinstance(job, str):
                if self.procura_usuario(name) is None:
                    user = User(name, job)
                    self.store.bd.append(user)
                    return "Usuario adicionado"
                else:
                    return "Usuário invalido"
            else:
                return "Parametro inválidos"
        else:
            return "Parametro inválidos"


    def procura_usuario(self, name):
        for _ in self.store.bd:
            if user.name == name:
                return None

    def remove_user(self, name):
        if self.validando_se_existe_usuario(name):
            lista = self.store.bd

            for i in range(len(lista)):
                if lista[i].name == name:
                    lista.pop(i)
                    return f"Usuário {name} removido"

        return f"Não foi possível remover o usuário {name}, já que ele não foi encontrado!"