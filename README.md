# weechat-unquery

A weechat plugin that provides a `/unquery` command to close private chats only.

Comes useful as `/close` (alias of `/window close`) does not care whether you're closing a private chat, a public channel or a private channel.

## Usage

``` sh
/unquery
```

## Installation

Just like any normal weechat plugin, copy it to `~/.weechat/python` and symlink it in `~/.weechat/python/autoload`.
