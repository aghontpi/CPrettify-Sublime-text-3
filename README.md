# Plugin for Sublime text-3

>A C-prettify plugin for sublime text, just install it and use it.. No additional configurations or installs required.

![Demo](https://public-folder-0000.firebaseapp.com/img/demo.gif)

## Getting Started

### Install from Package Control [CPrettify](https://packagecontrol.io/packages/CPrettify)

Using Package Control [Sublime Package Manager](http://wbond.net/sublime_packages/package_control)

To install use these commands.

* `Ctrl+Shift+P`
* type `install`, select `Package Control: Install Package`
* type `CPrettify`, select `CPrettify`


---or do it manually?---

Just copy the 'Cprettify' folder to  "C:\Users\'[username_here]'\AppData\Roaming\Sublime Text 3\Packages\" -for Windows 

## Usage

* Use  `Ctrl+Shift+P`
* Type `cprettify`, Available options will be shown to use.
---or---
* Use menu options
---or---
* Set keyboard shortcuts via provided settings
* See demo

## Prerequisites

Install package control for sublime.

How to install Package control?. See [Install package control](https://packagecontrol.io/installation)

## Advanced Usage

#### NOTE
##### _Use user setting to override, if changes are made to default, updates will reset it._

* Override provided key bindings from settings if it interfears
* You can also specify which config file to use from provided configs
---or---
you can provide your own config from 'create config file' under settings
and paste your config there and set 
```js
{
	"user_config_file":"False" to "user_config_file":"True"
}
```
* Incase you messed up your config file use "restore default setting" to restore original settings.


## Built With

* Python 
* Sublime-api - documented via comments
* Json - Menus and Settings

## Authors

* **Gopinath (aka) Bluepie** [Gopinath001](https://github.com/Gopinath001) 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
