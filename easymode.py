
from __future__ import annotations

from ansible.cli import CLI

import os
import stat

from ansible import constants as C
from ansible import context
from ansible.cli.arguments import option_helpers as opt_help
#from ansible.errors import AnsibleError
#from ansible.executor.playbook_executor import PlaybookExecutor
#from ansible.module_utils.common.text.converters import to_bytes
#from ansible.playbook.block import Block
#from ansible.plugins.loader import add_all_plugin_dirs
#from ansible.utils.collection_loader import AnsibleCollectionConfig
#from ansible.utils.collection_loader._collection_finder import _get_collection_name_from_path, _get_collection_playbook_path
from ansible.utils.display import Display


display = Display()

class easyModeCLI(CLI):
	name = "ansible-easymode"

	def init_parser(self):

        # create parser for CLI options
        super(PlaybookCLI, self).init_parser(
            usage="%prog [options] [easyModeTask] [specificVariable]",
            desc="Creates Ansible playbooks based on prompt recieved")

        opt_help.add_connect_options(self.parser)
        opt_help.add_meta_options(self.parser)
        opt_help.add_runas_options(self.parser)
        opt_help.add_subset_options(self.parser)
        opt_help.add_check_options(self.parser)
        opt_help.add_inventory_options(self.parser)
        opt_help.add_runtask_options(self.parser)
        opt_help.add_vault_options(self.parser)
        opt_help.add_fork_options(self.parser)
        opt_help.add_module_options(self.parser)


    def run(self):

        super(easyModeCLI, self).run()
        if easyModeTask == "ssh":
            playbook_content = generate_ssh_playbook()
            with open('%easyModeTask_playbook.yml', 'w') as file:
                file.write(playbook_content)
            print("%easyModeTask playbook generated successfully.")
        else:
            print("Unsupported protocol.")

        


def generate_ssh_playbook():
    playbook = """
---
- name: Configure ssh
  gather_facts: no
  
  tasks:
    - name: Configure 
      ios_config:
        lines:
          - set service ssh port %specificVariable
"""
    return playbook


def main(args=None):
easyModeCLI.cli_executor(args)


if __name__ == '__main__':
    main()
