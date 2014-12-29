## Matip 关键字 ##

### app ###

.apk文件所在的本地绝对路径或者远程路径，matip会将安装路径对应的应用安装在真机或模拟器上<br />
如：<br />
c:/my.apk <br />
或 <br />
http://myapp.com/my.apk

### device ###
要使用的真机或模拟器设备ID，可通过adb命令查看：<br />

	adb devices

### model ###
应用类型(native、hybrid)

<br />
### 例子 ###
原生应用：

	from matip import driver

	capabilities = {}
	capabilities["app"] = "c:/selendroid-test-app.apk"
	capabilities["device"] = "0123456789ABCDEF"
	capabilities["model"] = "native"
	
	driver = driver.MobileDriver(capabilities)

混合应用：
	
	from matip import driver
	
	capabilities = {}
	capabilities["app"] = "c:/selendroid-test-app.apk"
	capabilities["device"] = "0123456789ABCDEF"
	capabilities["model"] = "hybrid"
	
	driver = driver.MobileDriver(capabilities)