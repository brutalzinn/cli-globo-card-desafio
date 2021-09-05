class Card:
    def __init__(self, texto, tag = None):
        self.texto = texto
        self.tags = tag
    def get_card(self):
        if self.tags is not None:
            tagsFix = self.tags.replace(' ', '').split(';')
            tagsList = []
            for t in tagsFix:
                if len(t) > 0:
                    tagsList.append(t)
            return {"texto":self.texto,"tags":tagsList}
        else:
            return {"texto":self.texto}
