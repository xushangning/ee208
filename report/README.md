# 写报告注意事项

## 要求

1. 中文
2. **不要**引用代码。例如[学长的报告](https://github.com/yyong119/BookSearchEngine/blob/master/Book_search_reporter.pdf)中没有引用代码。主要写自己做的东西、使用的技术、面对的困难和解决方法。
3. 可以模仿一下学长报告的风格。

## 模板使用方法

1. 在初始状态下本文件夹中只有 `main.tex` 文件。每个人要开始写报告的话，先在本文件夹下面新建一个 `.tex` 文件，这个文件将存放你写的那部分报告，文件名用英文。不妨假设这个 `.tex` 文件叫 `crawler.tex`；
2. `crawler.tex`（和其他所有除了 `main.tex` 以外的所有 Tex 文件） 的格式**必须**按照下面的来

```latex
\documentclass[main.tex]{subfiles}

\begin{document}

% 报告内容

\end{document}
```

3. 一个 Tex 文件中写一个到多个 section，section 的标题和内容都可以是中文。由于 LaTeX 已经配置好了，不需要再自行 `\usepackage`；
4. 由于 `crawler.tex` 是不完整的 Tex 文件，此时直接编译 `crawler.tex` **一定**会报错。为了看到编译 `crawler.tex` 得到的报告，我们先要在 `main.tex` 中引用 `crawler.tex`，类似在 C++ 中引用头文件。`\subfile{}` 这个命令类似 C++ 中的 `#include`，可以引用其他 Tex 文件。现在我们要在 `main.tex` 引用 `crawler.tex` 的文件，在 `main.tex` 中找到如下几行：

```latex
\begin{document}

\begin{CJK}{UTF8}{gbsn}

\maketitle

\subfile{aaa}   % <-- 看这里

\end{CJK}

\end{document}
```

5. 要引用 `crawler.tex`， 就要在 `main.tex` 中添加 `\subfile{crawler}`。注意不要写 `crawler.tex` 的文件后缀名。由于 `\subfile{}` 出现的顺序决定了被引用文件在最终报告中出现的顺序，而且我想要让 `crawler.tex` 出现在 `aaa` 前面，所以会在 `main.tex` 中写

```latex
\subfile{crawler}   % 在 aaa 上面
\subfile{aaa}       % <-- 看这里
```

6. 这个时候才可以编译 `crawler.tex`，编译结果为**完整**的报告，而不只是 `crawler.tex` 中的内容。
7. 所有 `\subfile{}` 命令必须出现在 `main.tex` 中的 `\maketitle` 和 `\end{CJK}` 这两行中间。
8. 由于我们并没有叫 `aaa.tex` 的文件，`\subfile{aaa}` 只是用于演示，所以在 `main.tex` 中并不会有这么一行。
8. 不要把编译好的报告（PDF 文件）提交到 GitHub 上。
