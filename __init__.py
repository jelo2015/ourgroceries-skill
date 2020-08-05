from mycroft import MycroftSkill, intent_file_handler


class Ourgroceries(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('ourgroceries.intent')
    def handle_ourgroceries(self, message):
        self.speak_dialog('ourgroceries')


def create_skill():
    return Ourgroceries()

