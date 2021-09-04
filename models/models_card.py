class Card:
    def __init__(self, texto, tag):
        self.texto = texto
        self.tags = tag
    def getCard(self):
        tagsFix = self.tags.replace(' ', '').split(';')
        tagsList = []
        for t in tagsFix:
            if len(t) > 0:
                tagsList.append(t)
        return {"texto":self.texto,"tags":tagsList}
