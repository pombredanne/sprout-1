

def dict_to_list(installer_list):
    """ For now the only type of installer we support is 'izpack' """
    return [IzPackInstaller(i['hostname'], i['installer_artifacts'], i['user_input_file']
        ) for i in installer_list]


class Installer(object):
    pass # TODO


class IzPackInstaller(Installer):

    def __init__(self, hostname, installer_artifacts, user_input_file):
        self.hostname = hostname
        self.installer_artifacts = installer_artifacts
        self.user_input_file = user_input_file


