#### 找js源文件所在位置
- 方法1: 在NetWork请求的Initiator(调用栈)中，即可找到发出该请求所在的原js代码
- 方法2: 在Chrome的Sources中top找涉及加密的功能函数所在的js源文件

#### 找到加密位置代码
打断点，然后点暂停js执行，再刷新页面或者点相应触发时间来重载页面，仔细观察内部加密原理

- Step over（逐语句）

逐行执行，以了解每一行如何操作当前的变量。当你的代码调用另一个函数的时候，调试器不会跳到那个函数的代码中去，其焦点还是当前的函数，而 Step into 则相反。

- Step into（逐过程）

和逐语句类似，但是点击逐过程会在函数调用时,令调试器将执行转到所调用的函数声明中去。

- Toggle breakpoints

切换断点启用、禁用状态，同时保证各自的启用状态不会受到影响。

## packed混淆
[https://www.cnblogs.com/c-x-a/p/9273148.html](https://www.cnblogs.com/c-x-a/p/9273148.html)
[https://www.cnblogs.com/c-x-a/p/9273785.html](https://www.cnblogs.com/c-x-a/p/9273785.html)