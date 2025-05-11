## 调试
对窗体程序调试而言： 不要使用 MessageBox，因为不高效


1. 使用 Debug.WriteLine 或 Trace.WriteLine 输出调试信息，因为调试信息会输出在 Visual Studio 的 Output 窗口


1. 按 F9 设置断点
2. 使用 System.Diagnostics.Debugger.Break()
   1. 适用场景：动态逻辑中无法预测断点位置时（如循环或条件分支）。
3. 条件断点（Conditional Breakpoints）

## 