from entities.html_request import HtmlRequest
from utils.navigator import Navigator


class Activator(object):

    @staticmethod
    def command_activator(html_request: HtmlRequest):
        return Navigator.user_interaction(html_request.commend)
