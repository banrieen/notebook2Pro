编程训练 和 慕课学习
===================================

1. 算法训练题当前以 Python/C 为主.
2. Mook 学习分别建立了工程目录
3. 按组件功能分类的试题,范例在根目录下.


Jupyter notebook： 同步到github; 等完善后会发布到 readdoc

post_save_hook同步github方式：
* post_save_hook(model=model, os_path=os_path, contents_manager=cm)
  在Jupyter notebook 编就后保存后触发

* github webhook 在其他分支有提交或合并时，需要自定义实现扩展API支持 
[File save hooks](https://jupyter-notebook.readthedocs.io/en/stable/extending/savehooks.html?highlight=hook)


* sphinx 安装和配置:

```
On Linux or MacOS, you should open your terminal and run the following command.

$ pip install -U sphinx

On Windows, you should open Command Prompt (⊞Win-r and type cmd) and run the same command.

C:\> pip install -U sphinx

```
* Build static page

 sphinx-build -b html sourcedir builddir
 or sphinx-build -b latexpdf sourcedir builddir

 **在Github.io 配置页面，不要使用Jekyll theme。**

CookBook 为常见的练习题目
----------------------------------------------------

* 按照 leetcode题型做了基本分类

* 还包含 CoderByte，Kaggle 等