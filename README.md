# Generate A Folder Of String

I’m a big fan of writing such as wordpress blog. Somehow, I’ve come across troubles sharing the structure of my project. I was doing the screen capture to archive this purpose which is really inconvenient. Therefore, I created this plug in which can help you easily generate a ‘text version’ of project structure：

我比较喜欢写博文，很多时候需要生成一张项目结构图，可是这很麻烦，所以我渴望能有一个简单、易用、快速生成结构图的方式。比如这样：

```javascript
........app
............order
................list.html
................listCtrl.js
............user
................list.html
................listCtrl.js
............app.init.js
........bower.json
........gulpfile.js
........package.json
```

# How to use 使用方法

## Menu 菜单

File->Generate Folder Of String,input in a target project path. Leave it blank if the target is in the same folder with this plug in.

File->Generate Folder Of String，输入要生成的路径；空表示当前所打开的文件夹。

## Shortcuts 快捷键

Make sure there is already an opened file first, and press ‘ctrl+alt+g’ then ‘ctrl + t’ .

前提必须确保打开一份已经存在的文件，按 `ctrl+alt+g, ctrl+t`。

# Peremeters 参数

脚本只有两个参数：

* `prefix_character`：prefix, default to be ‘….’ 前缀字符，默认 `....`。
* `start_level`：start level which is the number of  prefix_character . 开始级别，即 `prefix_character` 生成开始数量。
