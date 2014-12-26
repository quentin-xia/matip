## what is matip? ##
Matip is an open source,test automation tool for native and hybrid apps,
tested on emulators and real devices.

### Supported Python Versions ###
        
 * Python 2.6, 2.7
 * Python 3.2, 3.3

### Installing ###
        
If you have `pip <http://www.pip-installer.org>` on your system, you can simply install or upgrade the Python bindings
        
	pip install -U matip
        
Alternately, you can download the source distribution from `PyPI <http://pypi.python.org/pypi/matip>`,unarchive it, and run
        
	python setup.py install
        
Note: both of the methods described above install `matip` as a system-wide package  That will require administrative/root access to ther machine.  You may consider using a `virtualenv <http://www.virtualenv.org/>`_ to create isolated Python environments instead.
        
### Example ###


*open a native apps*

    from matip import driver

    capabilities = {}
    capabilities["app"] = "c:/selendroid-test-app.apk"
    capabilities["device"] = "0123456789ABCDEF"
    capabilities["model"] = "native"

    driver = driver.MobileDriver(capabilities)

    do some thing...
    
    driver.quit()

<br />
<br />
<br />

## 什么是matip? ##
matip是开源的移动端自动化测试框架，可以测试原生和混合模式的应用

### 优点 ###

- 能根据文本，描述等属性定位需要操作的UI元素
- 支持多种手势操作，如：点击、案件、拖拽等
- 可进行跨应用的测试
- 支持原生和混合模式应用
- 环境搭建极其简单，无需root，无需安装Android SDk

### 缺点 ###

- 只支持API Level 17+（Android 4.2+）
- 暂不支持中文输入

### 环境 ###

- Python 2.6, 2.7
- Python 3.2, 3.3

### 安装 ###
如果系统中已安装 `pip <http://www.pip-installer.org>` ,你可以直接安装或更新matip

	pip install -U matip

或者，你可以从 `PYPI <http://pypi.python.org/pypi/matip>` 下载源文件，解压并执行setup.py

	python setup.py install

注：上述两种方法安装matip需要将python加入环境变量

### 例子 ###
*安装并打开一个原生应用*

    from matip import driver

    capabilities = {}
    capabilities["app"] = "c:/selendroid-test-app.apk"
    capabilities["device"] = "0123456789ABCDEF"
    capabilities["model"] = "native"

    driver = driver.MobileDriver(capabilities)

    do some thing...
    
    driver.quit()

<br />

**有任何疑问或吐槽请联系：** 

- QQ: 873334303
- Email: 873334303@qq.com