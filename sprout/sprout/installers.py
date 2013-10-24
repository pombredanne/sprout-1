import os
from fabric.api import *

def dict_to_list(installer_list):
    """ For now the only type of installer we support is 'izpack' """
    return [IzPackInstaller(
                i['hostname'], 
                i['install_script'],
                i['artifact_files'],
                i['env_files'])
           for i in installer_list]


class Installer(object):
    pass # TODO


class IzPackInstaller(Installer):

    def __init__(self, hostname, install_script, artifact_files, env_files):
        self.hostname = hostname
        self.install_script = install_script
        self.artifact_files = artifact_files 
        self.env_files = env_files

    def do_install(self, cfg):
        """ Make the installation happen."""
        # connect to self.hostname
        env.user = cfg.get_remote_user()
        env.host_string = self.hostname
        deploy_temp_dir = cfg.get_deploy_temp_dir()

        run("mkdir -p " + deploy_temp_dir)

        # push install script
        put(os.path.join(cfg.get_environment_dir(), self.install_script), deploy_temp_dir)

        # push artifacts
        for artifact_file in self.artifact_files:
            put(os.path.join(cfg.get_local_temp_dir(), artifact_file), deploy_temp_dir)
            
        # push env_files
        for env_file in self.env_files:
            put(os.path.join(cfg.get_environment_dir(), env_file), deploy_temp_dir)

        # run script
        # TODO
        

    def __str__(self):
        return "<IzPackInstaller hostname:%s installer:%s artifacts:'%s' env_files:'%s'" % (
            self.hostname,
            self.install_script,
            self.artifact_files,
            self.env_files
        )
            
