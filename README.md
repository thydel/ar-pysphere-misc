# Provide some pysphere modules
Auto generated README from modules documentation

## vsphere add disk
### documentation
```yaml
---

module: vsphere_add_disk

short_description: Add a disk on a guest on VMWare vSphere

description:

  - This module add a disk to a specific guest on VMWare vSphere.
  - This module requires the pysphere python module.
  - This module was a quick and dirty mix of:
    - U(https://github.com/ansible-provisioning/ansible-provisioning/blob/master/library/vsphere_facts)
    - U(https://groups.google.com/forum/#!topic/pysphere/Ehu12Umaruk)
    - U(https://groups.google.com/forum/#!topic/pysphere/Ulutb1oNDOI)

author: Thierry Delamare

notes:

  - This module ought to be run from a system that can access vSphere directly.
    Either by using local_action, or using delegate_to.

options:
  host:
    description:
      - The vSphere server from the cluster the virtual server is located on.
    required: true
    aliases: [ vcenter ]
  login:
    description:
      - The login name to authenticate on the vSphere cluster.
    required: true
    aliases: [ user ]
  password:
    description:
      - The password to authenticate on the vSphere cluster.
    required: true
    aliases: [ pass ]
  guest:
    description:
      - The virtual server to add a disk on
    required: true
    aliases: [ vm, name ]
  disk:
    description:
      - The unit number of the disk to be added (zero based)
    required: true
    aliases: [ unit ]
```

### examples
```yaml
- local_action:
    host={{ host }} login={{ login }} password={{ password }}
    guest={{ inventory_hostname }}.epiconcept.fr disk=1 size=40
```
## vsphere add nic
### documentation
```yaml
---

module: vsphere_add_nic

short_description: Add a NIC on a guest on VMWare vSphere

description:

  - This module add an network interface to a specific guest on VMWare vSphere.
  - This module requires the pysphere python module.
  - This module was a quick and dirty mix of:
    - `vsphere_facts <https://github.com/ansible-provisioning/ansible-provisioning/blob/master/library/vsphere_facts>`__
    - `PySphere - Missing Pieces <http://snapfiber.com/pysphere-missing-pieces.html>`__

options:

  host:
    description:
      - The vSphere server from the cluster the virtual server is located on.
    required: true
  login:
    description:
      - The login name to authenticate on the vSphere cluster.
    required: true
  password:
    description:
      - The password to authenticate on the vSphere cluster.
    required: true
  guest:
    description:
      - The virtual server to add a NIC on
    required: true
  net:
    description:
      - The name of the network the NIC will be attached
    required: true

notes:

  - This module ought to be run from a system that can access vSphere directly.
    Either by using local_action, or using delegate_to.
```

### examples
```yaml
---

- local_action:
    vsphere_clone host={{ host }} login={{ login }} password={{ password }}
    guest={{ inventory_hostname }}.epiconcept.fr net=ADM
    register: admin
```
## vsphere extraconfig
### documentation
```yaml
---

module: vsphere_extraconfig

short_description:

  - Change VMX settings on a guest on VMWare vSphere.  This module has
    a dependency on pysphere >= 1.7.

description:
  - This Change VMX settings on a guest on VMWare vSphere
  - This module requires the pysphere python module.

version_added: "1.4"
author: Thierry Delamare

notes:

  - This module ought to be run from a system that can access vSphere
    directly.  Either by using local_action, or using delegate_to.

  - I assemble this before M(vsphere_guest) was available.

  - Turned out that as by 1.9.1 C(vm_extra_config) do not work with
    C(reconfigured).

  - Alias similar to M(vsphere_guest) added.

options:
  host:
    description:
      - The vSphere server from the cluster the virtual server is located on.
    required: true
    aliases: [ vcenter, vcenter_hostname ]
  login:
    description:
      - The login name to authenticate on the vSphere cluster.
    required: true
    aliases: [ user, username ]
  password:
    description:
      - The password to authenticate on the vSphere cluster.
    required: true
    aliases: [ pass ]
  guest:
    description:
      - The virtual server to change the options on
    required: true
    aliases: [ vm, name ]
  xtracnfset:
    description:
      - a dict of options to set
    aliases: [ vm_extra_config ]
```

### examples
```yaml
---

- vsphere_extraconfig:
    vcenter_hostname: vcenter.mydomain.local
    username: myuser
    password: mypass
    guest: newvm001
    xtracnfset:
      disk.locking : "false"
      disk.EnableUUID: "true"
```
## vsphere status
### documentation
```yaml
---

module: vsphere_status

short_description: Gather status for a guest on VMWare vSphere

description:
  - This module gathers status for a specific guest on VMWare vSphere.
  - This module requires the pysphere python module.

options:
  vcenter_hostname:
    description:
      - The hostname of the vcenter server the module will connect to, to create the guest.
    required: true
    default: null
    aliases: []
  guest:
    description:
      - The virtual server name you wish to manage.
    required: true
  username:
    description:
      - Username to connect to vcenter as.
    required: true
    default: null
  password:
    description:
      - Password of the user to connect to vcenter as.
    required: true
    default: null

version_added: "1.9"
author: Thierry Delamare

notes:

  - This module ought to be run from a system that can access vSphere directly.
    Either by using local_action, or using delegate_to.

  - Mimic M(vsphere_guest) which lack the feature.

  - Cloned from https://github.com/ansible-provisioning
```

### examples
```yaml
---

- vsphere_status:
    vcenter_hostname: vcenter.mydomain.local
    username: myuser
    password: mypass
    guest: newvm001
```

