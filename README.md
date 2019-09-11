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
    ./Configuration 项目配置如 Yaml, json, config file等
    ./CookBook jupyter notebooks  案例集锦，面试相关问题(按照 leetcode题型做了基本分类还包含 CoderByte，Kaggle 等)
        ./Algiorithms 案例集锦，面试相关算法题
        ./Scripts bash脚本（awk,sed,grep）
        ./SQL SQL优化
        ./MultProcess 线程进程问题
    ./DataAnalysis 数据处理和分析，大数据
    ./DB Mysql,sqlitter,redis, postgresql, mongodb
    ./DesignPatterns 编程设计模式
    ./Draw 编程绘图
    ./Distributed 分布式相关
    ./FrameworkServices Python Web框架
    ./Game 游戏
    ./GUI 图形开发
    ./LanguageSong 语言或语音处理
    ./office 文档处理方法，包含VBA宏脚本
    ./NetworkProtocal 网络协议TCP/UDP/HTTP/WEBSOCKETS对比
    ./PicturesVideo 图形和视频处理
    ./Process 进程线程，协程
    ./Spider 爬虫对比
    ./Sphinx Sphinx转换后的html文档
    ./System 系统操作
    ./VersionDevOps WEB部署CI/CD
    ./Jupyter_notebook_config.py notebook配置
    ./VisualStudioCpp (windows MinGW环境) 汇总以C/C++的算法数据结构，包含算法导论在线实例等
    ./Jupyter_notebook_systemd.service 在Centosn nottebook 

文件库管理和发布
----------------------------------------------------        
* Jupyter notebook： 同步到github; 

```
post_save_hook同步github方式：
* post_save_hook(model=model, os_path=os_path, contents_manager=cm)
# 在Jupyter notebook 编辑保存后触发

* github webhook 在其他分支有提交或合并时，需要自定义实现扩展API支持 
[File save hooks](https://jupyter-notebook.readthedocs.io/en/stable/extending/savehooks.html?highlight=hook)
```

* sphinx 转换为静态HTML，链接到个人主页 github.io:

```
# On Linux or MacOS, you should open your terminal and run the following command.

$ pip install -U sphinx

# On Windows, you should open Command Prompt (⊞Win-r and type cmd) and run the same command.

C:\> pip install -U sphinx

# Build static page

sphinx-build -b html sourcedir builddir
# or sphinx-build -b latexpdf sourcedir builddir

```

*在Github.io 配置页面，不要使用 Jekyll theme。*

* 相关主题会整理发布到CSDN Blog：https://blog.csdn.net/banrieen

* Github.io 还在完善中。