from django.http import Http404


def check_topic_owner(request, topic):
    """ Evita que um usuário edite assuntos de outros usuários """
    if topic.owner != request.user:
        raise Http404