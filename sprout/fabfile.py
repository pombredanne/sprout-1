from fabric.api import local
import json
import os
import glob
from pprint import pprint
from sprout import * 

__all__ = ['get_artifacts', 'deploy', 'restart_services']


def _clean(tmpdir):
    """ Remove any existing files from a previous run of sprout. """
    _ensure_exists(tmpdir)
    _remove_files(tmpdir)
        

def _ensure_exists(tmpdir):
    try:
        os.makedirs(tmpdir)
    except OSError:
        if not os.path.isdir(tmpdir):
            raise
        
def _remove_files(tmpdir):
    files = glob.glob(os.path.join(tmpdir, '*'))
    for f in files:
        print('removing %s' % f)
        os.remove(f)


def _get_artifacts(cfg):
    """ Go to nexus, get artifacts defined in config file and save those files to the local directory. """
    _clean(cfg.settings['local_temp_dir'])

    for artifact in cfg.artifacts:
        # get that artifact and put it in the local store
        code, o, e = artifact.download(cfg.settings['nexus_hostname'], cfg.settings['local_temp_dir'])
        print('Download Results:' + str(code))
        output = (str(o) + '\n' + str(e)).strip()
        print(output)


def get_artifacts(config_file):
    cfg = config.load_config(config_file)
    _get_artifacts(cfg)

def deploy(config_file):
    """ For each artifact, 
         connect to the servers this artifact goes to
         copy the artifact to the server
         copy the installer script to the server
         execute the installer on the server.
    """
    cfg = config.load_config(config_file)
    _get_artifacts(cfg)

    for inst in cfg.installer_list:
        inst.do_install(cfg)

def restart_services(config_file):
    """ Restart the services for the hosts in this configuration """
    cfg = config.load_config(config_file)
    print cfg.service_hosts
    for service_host in cfg.service_hosts:
        print("host: %s" % service_host)
        service_host.restart()
    
