# Generate A Folder Of String

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

# 使用方法

## 菜单

File->Generate Folder Of String，输入要生成的路径；空表示当前所打开的文件夹。

## 快捷键

前提必须确保打开一份已经存在的文件，按 `ctrl+alt+g, ctrl+t`。

# 参数

脚本只有两个参数：

* `prefix_character`：前缀字符，默认 `....`。
* `start_level`：开始级别，即 `prefix_character` 生成开始数量。
