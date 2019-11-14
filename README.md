慕课学习 和 编程训练
===================================

1. 算法训练题，当前以 Python/C++ 为主。
2. Mook，参考书籍的源码分别建立了工程目录。
3. 按组件功能分类的对比分析,范例在根目录下。

目录描述：
------------------------------------
    ./AI AI算法和框架
    ./Algorithms 数据结构和算法教程代码目录，对比整理。
    ./CallAnother 不同编程语言接口调用，如python <=> C
    ./Configuration 配置管理如 Yaml, json, configration files等
    ./CookBook jupyter notebooks  案例集锦，面试相关问题(按照 leetcode题型做了基本分类还包含 CoderByte，Kaggle 等)
        ./Algiorithms 案例集锦，面试相关算法题
        ./Scripts bash脚本（awk,sed,grep）
        ./SQL SQL优化
        ./MultProcess 线程进程问题
    ./DataAnalysis 数据处理和分析
    ./DB  Mysql,sqlitter,redis, postgresql, mongodb数据库
    ./DesignPatterns  设计模式
    ./Draw  绘图
    ./Distributed 分布式相关
    ./FrameworkServices  Web框架
    ./Game 游戏
    ./GUI 图形开发
    ./LanguageSong 语言或语音处理
    ./MicrosoftOffice 文档处理方法，包含VBA宏脚本
    ./NetworkProtocal 网络协议TCP/UDP/HTTP/WEBSOCKETS对比
    ./PicturesVideo 图形和视频处理
    ./MultiProcess 进程线程，协程
    ./Spider 爬虫对比
    ./Sphinx Sphinx转换后的html文档
    ./System 系统操作
    ./VersionDevOps WEB部署CI/CD
    ./Jupyter_notebook_config.py notebook配置
    ./VisualStudioCpp (windows MinGW环境) 汇总以C/C++的算法数据结构，包含算法导论在线实例等
    ./XcodeCpp (Mac OS Gnu环境) 汇总以C/C++的算法数据结构，包含算法导论在线实例等
    ./Jupyter_notebook_systemd.service 操作系统下使用 systemctl 管理服务  

文件库管理和发布
----------------------------------------------------        
* Jupyter notebook： 同步到github; 

```
# 修改根目录下的 jupyter_notebook_systemd.service 中的 post_save_hook 要同步的 branch，一般是非 master 的。
post_save_hook 同步 github 方式：

* post_save_hook(model=model, os_path=os_path, contents_manager=cm)

# 在 Jupyter notebook 编辑保存后触发

* github webhook 在其他分支有提交或合并时，需要自定义实现扩展 API 支持 
[File save hooks](https://jupyter-notebook.readthedocs.io/en/stable/extending/savehooks.html?highlight=hook)

```

* 设置 systemd service

```
# 将根目录下的 jupyter_notebook_systemd.service 拷贝到 /etc/systemd/system （以 centos 7 为例）路径下

cp -f ./jupyter_notebook_systemd.service /etc/systemd/system/jupyter.service

# systemctl reload config , 这一步系统会自动提示。
# 通过 systemctl start/stop/restart jupyter 

systemctl start jupyter 

```
  *不同系统下 bash 所在路径可能不同，以及登录用户可能不同，需要记得更新！*

* sphinx 转换为静态HTML，链接到个人主页 github.io:
  这个原本是便于展示，尤其是一些 pdf，文本。现在主要是将 ipynb 转换为 web 文档。

```
# On Linux or MacOS, you should open your terminal and run the following command.

$ pip install -U sphinx

# On Windows, you should open Command Prompt (⊞Win-r and type cmd) and run the same command.

C:\> pip install -U sphinx

# Build static page

sphinx-build -b html sourcedir builddir

# or sphinx-build -b latexpdf sourcedir builddir

# 也可以在 post_save_hook 中配置 nbconvert 但是它依赖 pandoc,有时候不好安装；再次还要组织目录和服务器。
# 有时候直接使用页面工具 File 选项中的 Save as 或 Download as 也是比较轻松的。
```
* 最后注意，jupyter.service 启动时读取的是根目录下的 jupyter_notebook_config.py, 如果部署环境或路径改变，需要修改其中的 c.NotebookApp.notebook_dir ,当然在配置我并没有启用它。此时，可能非常想再写一个 bash 脚本，或者找一个 CI/CD 工具来做，这已经比较简单了，粒度适中，不要反而搞得太复杂了。Nbextensions 很多不能用，或许也是其中的原因吧。

*在Github.io 配置页面，不要使用 Jekyll theme。*

* 相关主题会整理发布到CSDN Blog：https://blog.csdn.net/banrieen
* Github.io 还在完善中。