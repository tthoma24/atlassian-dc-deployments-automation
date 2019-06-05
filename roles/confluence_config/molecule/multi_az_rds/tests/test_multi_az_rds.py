import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_confluence_config_file(host):
    f = host.file('/var/atlassian/application-data/confluence/confluence.cfg.xml')
    assert f.exists
    assert f.contains('<property name="hibernate.connection.url">jdbc:postgresql://postgres-db.ap-southeast-2.rds.amazonaws.com:5432/confluence?targetServerType=master</property>')
