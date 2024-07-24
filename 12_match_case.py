#第一个case ['gcc']表示列表仅有'gcc'一个字符串，没有指定文件名，报错；
#第二个case ['gcc', file1, *files]表示列表第一个字符串是'gcc'，第二个字符串绑定到变量file1，后面的任意个字符串绑定到*files（符号*的作用将在函数的参数中讲解），它实际上表示至少指定一个文件；
#第三个case ['clean']表示列表仅有'clean'一个字符串；
#最后一个case _表示其他所有情况。
#可见，match语句的匹配规则非常灵活，可以写出非常简洁的代码。
args = ['gcc', 'hello.c', 'world.c']
# args = ['clean']
# args = ['gcc']

match args:
    # 如果仅出现gcc，报错:
    case ['gcc']:
        print('gcc: missing source file(s).')
    # 出现gcc，且至少指定了一个文件:
    case ['gcc', file1, *files]:
        print('gcc compile: ' + file1 + ', ' + ', '.join(files))
    # 仅出现clean:
    case ['clean']:
        print('clean')
    case _:
        print('invalid command.')