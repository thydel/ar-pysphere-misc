#!/usr/bin/python

# (c) 2014, <t.delamare@epiconcept.fr>
#
# This module is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software.  If not, see <http://www.gnu.org/licenses/>.

DOCUMENTATION = '''
#include documentation.yml
'''

EXAMPLES = '''
#include examples.yml
'''

import sys
try:
    import pysphere
    from pysphere import VIServer
except ImportError:
    print "failed=True msg='pysphere python module unavailable'"
    sys.exit(1)

import ssl

def main():

    module = AnsibleModule(
        argument_spec = dict(
            host = dict(required=True, aliases=['vcenter', 'vcenter_hostname'], type='str'),
            login = dict(required=True, aliases=['user', 'username'], type='str'),
            password = dict(required=True, aliases=['pass'], type='str'),
            guest = dict(required=True, aliases=['name', 'vm'], type='str'),
            validate_certs=dict(required=False, type='bool', default=True),

            xtracnfset = dict(required=True, aliases=['vm_extra_config'], type='dict'),
        ),
        supports_check_mode=True
    )

    host = module.params.get('host')
    login = module.params.get('login')
    password = module.params.get('password')
    guest = module.params.get('guest')
    validate_certs = module.params['validate_certs']

    xtracnfset = module.params.get('xtracnfset')

    server = VIServer()
    if not validate_certs:
        default_context = ssl._create_default_https_context
        ssl._create_default_https_context = ssl._create_unverified_context
    try:
        server.connect(host, login, password)
    except Exception, e:
        module.fail_json(msg='Failed to connect to %s: %s' % (host, e))

    # Check if the VM exists before continuing    
    try:
        vm = server.get_vm_by_name(guest)
    except pysphere.resources.vi_exception.VIException, e:
        module.fail_json(msg=e.message)

    # get current config
    xtracnf = {}
    for c in vm.properties.config.extraConfig:
        xtracnf[c._obj._key] = c._obj._value

    changed = False
    old = {}
    new = {}
    for k in xtracnfset:
        if not k in xtracnf or xtracnf[k] != xtracnfset[k]:
            if not k in xtracnf:
                old[k] = None
            else:
                old[k] = xtracnf[k]
            new[k] = xtracnfset[k]
            settings = { k: xtracnfset[k] }
            if not module.check_mode:
                vm.set_extra_config(settings)
            changed = True

    module.exit_json(changed=changed, xtracnfset=xtracnfset, xtracnf=xtracnf, old=old, new=new)

# this is magic, see lib/ansible/module_common.py
#<<INCLUDE_ANSIBLE_MODULE_COMMON>>
main()
