import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_collectd_installed(host):
    package = host.package('collectd')
    assert package.is_installed

def test_collectd_file(host):
    f = host.file('/etc/collectd/collectd.conf')
    assert f.exists
    assert f.contains('InstrumentationKey "XXX"')
    assert f.mode == 0o0644

def test_jaxb_installed(host):
    f = host.file('/usr/share/collectd/java/jaxb-api-2.3.1.jar')
    assert f.exists

# @pytest.mark.parametrize('filename', [
#   '/opt/atlassian/crowd/current/crowd-webapp/WEB-INF/lib/applicationinsights-core-2.3.1.jar',
#   '/opt/atlassian/crowd/current/crowd-webapp/WEB-INF/lib/applicationinsights-web-2.3.1.jar',
#   '/opt/atlassian/crowd/current/crowd-webapp/WEB-INF/lib/applicationinsights-collectd-2.3.1.jar'
# ])
# def test_app_insight_jars_downloaded(host, filename):
#     f = host.file(filename)
#     assert f.exists

def test_app_insights_collectd_file(host):
    f = host.file('/usr/share/collectd/java/applicationinsights-collectd-2.3.1.jar')
    assert f.exists

# def test_applicationinsights_xml_installed(host):
#     f = host.file('/opt/atlassian/crowd/current/crowd-webapp/WEB-INF/classes/ApplicationInsights.xml')
#     assert f.exists
