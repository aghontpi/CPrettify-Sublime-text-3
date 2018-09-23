# Plugin for Sublime text-3

A C-prettify plugin for sublime text, just install it and use it.. No additional configurations or installs required.

![Demo](http://imdead.esy.es/img/functions.gif)

## Getting Started

Install from Package Control [CPrettify](http://www.sublimetext.com/3)

### Using Package Control [Sublime Package Manager](http://wbond.net/sublime_packages/package_control)

To install use these commands.

* `Ctrl+Shift+P`
* type `install`, select `Package Control: Install Package`
* type `CPrettify`, select `CPrettify`


---or do it manually?---

Just copy the 'Cprettify' folder to  "C:\Users\'[username_here]'\AppData\Roaming\Sublime Text 3\Packages\" -for Windows 

## Usage

* Use  `Ctrl+Shift+P`
* Type `cprettify`, Available options will be shown to use. See demo

### Prerequisites

Install package control for sublime.

How to install Package control? 

[Install package control](https://packagecontrol.io/installation)

## Advanced Usage

#### NOTE! use user setting to override, if changes are made to default, updates will reset it.

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
* Install package control

## Authors

* **Gopinath (aka) Bluepie** 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
