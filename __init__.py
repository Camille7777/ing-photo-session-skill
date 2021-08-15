from mycroft import MycroftSkill, intent_file_handler


class IngPhotoSession(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('session.photo.ing.intent')
    def handle_session_photo_ing(self, message):
        self.speak_dialog('session.photo.ing')


def create_skill():
    return IngPhotoSession()

