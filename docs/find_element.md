# 元素定位与交互 #

matip支持原生应用中的元素和混合模式中的HTML元素<br />
Android原生应用可以使用Uiautomatorview,通过点击预览窗口上的空间来获取元素的属性<br />
Android混合应用可以使用Inspector来协助定位元素



## 例子 ##

### 找到屏幕上所有Button ###

	driver.find_elements(class_name="android.widget.Button")

### 找到名字为“EN Button”的按钮 ###

	driver.find_element(text="EN Button")

### 通过HTML标签查找元素 ###
	
	driver.selendroid.find_elements_by_tag_name("a")