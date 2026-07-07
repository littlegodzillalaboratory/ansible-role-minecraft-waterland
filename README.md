![Avatar](avatar.jpg)

[![Build Status](https://github.com/littlegodzillalaboratory/ansible-role-minecraft-waterland/workflows/CI/badge.svg)](https://github.com/littlegodzillalaboratory/ansible-role-minecraft-waterland/actions?query=workflow%3ACI)
[![Security Status](https://snyk.io/test/github/littlegodzillalaboratory/ansible-role-minecraft-waterland/badge.svg)](https://snyk.io/test/github/littlegodzillalaboratory/ansible-role-minecraft-waterland)

# Ansible Role Minecraft Waterland

Ansible Role Minecraft Waterland is a Ansible role for provisioning Minecraft Waterland customisations .

## Usage

Use the role in your playbook:

    - hosts: all

      vars:
        ans_reverse: true
        ans_transformation: 'upper'

      roles:
        - littlegodzillalaboratory.minecraft_waterland

## Colophon

<!-- BEGIN:DEVELOPERS_GUIDE -->
[Developer's Guide](https://littlegodzillalaboratory.github.io/developers-guide-ansible.html)
<!-- END:DEVELOPERS_GUIDE -->

<!-- BEGIN:BUILD_REPORTS -->
Build reports:

* [Lint report](https://littlegodzillalaboratory.github.io/ansible-role-minecraft-waterland/lint/ansible-lint.txt)
* [Test report](https://littlegodzillalaboratory.github.io/ansible-role-minecraft-waterland/test/molecule.txt)

<!-- END:BUILD_REPORTS -->
