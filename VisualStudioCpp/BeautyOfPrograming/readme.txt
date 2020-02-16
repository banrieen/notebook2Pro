========================================================================
    C++/WinRT BeautyOfPrograming Project Overview
========================================================================

This project demonstrates how to get started consuming Windows Runtime 
classes directly from standard C++, using platform projection headers
generated from Windows SDK metadata files.

Steps to generate and consume SDK platform projection:
1. Build project initally to generate platform projection headers into
    your Generated Files folder.
2. Include a projection namespace header in your pch.h, such as 
    <winrt/Windows.Foundation.h>.
3. Consume winrt namespace and any Windows Runtime namespaces, such as 
    winrt::Windows::Foundation, from source code.
4. Initialize apartment via init_apartment() and consume winrt classes.

Steps to generate and consume a projection from third party metadata:
1. Add a WinMD reference by right-clicking the References project node
    and selecting "Add Reference...".  In the Add References dialog, 
    browse to the component WinMD you want to consume and add it.
2. Build the project once to generate projection headers for the 
    referenced WinMD file under the "Generated Files" subfolder.
3. As above, include projection headers in pch or source code 
    to consume projected Windows Runtime classes.

========================================================================
Learn more about C++/WinRT here:
http://aka.ms/cppwinrt/
========================================================================

    主要内容：
    
    按照内容层次汇总编篡《编篡珠玑 Programing Pearls SecindEditon》，《编篡之美 Beauty Of Prpgraming》，《算法基础与在线实践—北京大学“程序设计与算法”慕课》和《算法精讲—C语言描述》C/C++基础算法数据结构的实例。
    以 算法精讲，算法基础与在线实践 为主干，综合应用或插入编篡珠玑和编篡之美的理念案例。
    辅助 Algorithms/ 目录下的章节，著成 “算法与程序设计”的应用篇；Xcode中的内容辅助以著成“算法与程序设计”的思索篇。