import os
from fabric.api import *

def create_objects(cfg, service_hosts):
    """ Turn a list of service host info into objects that can do
        starting, stopping of services, or other things that 
        we think up.
    """
    return [ServiceHost(
                s['hostname'], 
                s['services'],
                cfg.get_remote_user())
           for s in service_hosts]


class ServiceHost(object):

    def __init__(self, hostname, services, remote_user):
        self.hostname = hostname
        self.services = services
        self.remote_user = remote_user
        self.connected = False

    def _connect(self):
        if not self.connected:
            # connect to self.hostname
            env.user = self.remote_user
            env.host_string = self.hostname
            self.connected = True

    def _run_service(self, service_name, state):
        sudo('/sbin/service %s %s' % (service_name, state))

    def _run_all_services(self, state):
        for service_name in self.services:
            self._run_service(service_name, state)

    def start(self):
        self._connect()
        _run_all_services('start')

    def stop(self):
        self._connect()
        self._run_all_services('stop')


    def restart(self):
        """ Restart the services on this host."""
        self._connect()
        self._run_all_services('restart')
