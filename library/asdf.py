#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule


def main():
    fields = {"packages": {"required": True, "type": "list"}}

    module = AnsibleModule(argument_spec=fields)
    module.exit_json(changed=False, meta=module.params)


if __name__ == "__main__":
    main()
