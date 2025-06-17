#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def run_module():
    module_args = dict(
        name=dict(type='str', required=True)
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    user_name = module.params['name']
    message = f"Hello, {user_name}"

    result = dict(
        changed=False,
        message=message
    )

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
