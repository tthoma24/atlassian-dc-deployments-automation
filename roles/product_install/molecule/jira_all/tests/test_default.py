import os
from six.moves import urllib
import pytest
import testinfra.utils.ansible_runner
import json
from pprint import pprint

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

@pytest.fixture
def ansiblevars(host):
    ansiblevars = json.loads(host.file('/tmp/ansible.vars').content_string)
    return ansiblevars

def test_version_is_correct(host, ansiblevars):
    verfile = host.file(ansiblevars['atl_product_version_file']['cmd'][1])
    assert verfile.exists
    assert verfile.content.decode("UTF-8").strip() == ansiblevars['atl_product_version']

def test_is_downloaded(host, ansiblevars):
    installer = host.file(ansiblevars['atl_product_download'])
    assert installer.exists
    assert installer.user == 'root'

def test_completed_lockfile(host, ansiblevars):
    ansiblevars = json.loads(host.file('/tmp/ansible.vars').content_string)
    lockfile = host.file(ansiblevars['atl_product_download']+'_completed')
    assert lockfile.exists
    assert lockfile.user == 'root'

def test_is_unpacked(host, ansiblevars):
    installer = host.file(ansiblevars['atl_installation_base']+'/'+ansiblevars['atl_product_edition']+'/'+ansiblevars['atl_product_version']+'/atlassian-jira/')
    assert installer.exists
    assert installer.is_directory
    assert installer.user == 'jira'
    assert installer.mode == 0o0755

def test_obr_is_downloaded(host):
    installer = host.file('/media/atl/downloads/jira-servicedesk-application-3.16.1.obr')
    assert installer.exists
    assert installer.user == 'root'

def test_obr_completed_lockfile(host):
    lockfile = host.file('/media/atl/downloads/jira-servicedesk-application-3.16.1.obr_completed')
    assert lockfile.exists
    assert lockfile.user == 'root'

def test_obr_is_unpacked(host):
    jsdjar = host.file('/media/atl/jira/shared/plugins/installed-plugins/jira-servicedesk-application-3.16.1.jar')
    assert jsdjar.exists
    assert jsdjar.user == 'jira'
    assert jsdjar.mode == 0o0750