class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_pessoa(self, name, phone, CNPJ, Type, fav):
        self.model.add_pessoa(name, phone, CNPJ, Type, fav)

    def remove(self, item):
        self.model.delete_pessoa(item)

    def get_items(self):
        return self.model.lista_vil()

    def get_item_by_id(self, item_id):
        return self.model.get_item_by_id(item_id)

    def update_item(self, item_id, new_data):
        return self.model.alt_pessoa(item_id, new_data)

    def lista_vil(self):
        items = self.get_items()
        self.view.exibir_itens(items)

    def clear(self):
        self.view.clean()
        self.view.show_message("Campos limpos!")

    def add_pessoa(self, name, phone, CNPJ, Type, fav):
        self.model.add_pessoa(name, phone, CNPJ, Type, fav)
        self.view.clear()
        self.view.lista_vil()

    def delete_pessoa(self, item_id):
        self.model.delete_pessoa(item_id)
        self.view.show_message("Pessoa removida com sucesso!")
        self.view.lista_vil()

    def alt_pessoa(self, item_id, new_data):
        self.model.alt_pessoa(item_id, new_data)
        self.view.show_message("Dados da pessoa atualizados com sucesso!")
        self.view.lista_vil()

    def update_item(self, item_id, new_data):
        self.model.alt_pessoa(item_id, new_data)