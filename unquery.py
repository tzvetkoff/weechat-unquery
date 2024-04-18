# Provide a /unquery command to close private chats only
#
# Usage:
#   /unquery

import weechat


def cmd_unquery(_cb_data, buf, _args):
    name = weechat.buffer_get_string(buf, 'name')
    names = name.split('.')

    if name == 'weechat' or len(names) == 2 or names[-1].startswith('#') or names[-1].startswith('&'):
        weechat.prnt('', 'unquery: command "unquery" must be executed on private chat buffer')
        return weechat.WEECHAT_RC_ERROR

    weechat.command(buf, '/close')
    return weechat.WEECHAT_RC_OK


def main():
    if not weechat.register(
        'unquery',                                                  # Plugin name
        'Latchezar Tzvetkoff',                                      # Author
        '1.0.0',                                                    # Version
        'MIT',                                                      # License
        'Provide a /unquery command to close private chats only',   # Description
        '',                                                         # Shutdown callback
        '',                                                         # Character set
    ):
        return weechat.WEECHAT_RC_ERROR

    weechat.hook_command(
        'unquery',              # Command
        'Close private chat',   # Command description
        '',                     # Arguments
        '',                     # Arguments description
        '',                     # Completion template
        'cmd_unquery',          # Callback
        '',                     # Callback data
    )


if __name__ == '__main__':
    main()
