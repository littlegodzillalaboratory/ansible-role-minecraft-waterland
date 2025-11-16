<img align="right" src="https://raw.github.com/littlegodzillalaboratory/ansible-role-minecraft-waterland/main/avatar.jpg" alt="Avatar"/>

[![Build Status](https://github.com/littlegodzillalaboratory/ansible-role-minecraft-waterland/workflows/CI/badge.svg)](https://github.com/littlegodzillalaboratory/ansible-role-minecraft-waterland/actions?query=workflow%3ACI)
[![Security Status](https://snyk.io/test/github/cliffano/ansible-role-minecraft-waterland/badge.svg)](https://snyk.io/test/github/cliffano/ansible-role-minecraft-waterland)
<br/>

Ansible Role Minecraft Waterland
--------------------------------

Ansible Role Minecraft Waterland is a Ansible role for provisioning Minecraft Waterland customisations .

Usage
-----

Use the role in your playbook:

    - hosts: all

      vars:
        ans_reverse: true
        ans_transformation: 'upper'

      roles:
        - cliffano.minecraft_waterland