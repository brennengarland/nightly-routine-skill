from mycroft import MycroftSkill, intent_file_handler


class NightlyRoutine(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('routine.nightly.intent')
    def handle_routine_nightly(self, message):
        self.speak_dialog('routine.nightly')


def create_skill():
    return NightlyRoutine()

