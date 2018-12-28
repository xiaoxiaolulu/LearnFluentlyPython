"""
字符串、字节序列 =》 __repr__  __str__ __format__ __bytes__
数值转化 =》__abs__ __bool__ __complex__ __int__ __float__ __hash__ __index__
集合模拟 =》__len__ __getitem__ __ setitem__ __delitem__ __contains__
迭代枚举 =》__iter__ __reversed__ __next__
可调用模拟 =》__call__
上下文管理 =》__enter__ __exit__
实例创建和销毁 =》__new__ __init__ __del__
属性管理 =》 __getattr__ __getattribute__ __setattr__ __delattr__ _dir__
属性描述符 =》 __get__ __set__ __delete__
跟类相关的服务 =》__prepare__ __instancecheck__ __subclasscheck__

一元运算符 =》 __neg_ -
             __pos__ +
             __abs__ abs()

比较运算符 =》 __lt__ <
             __le__ <=
             __eq__ ==
             __ne__ !=
             __gt__ >
             __ge__ >=
算数运算符 =》 __add__ +
             __sub_ -
             __mul__ *
             __truediv__ /
             __floordiv__ //
             __mod__ %
             __divmod__ divmod()
             __pow__ **/pow()
             __round__ round()
反向算术运算符 =》 __radd__
                 __rsub__
                 __rmul__
                 _rtruediv__
                 __rfloordiv__
                 __rmod__
                 __rdivmod__

增量赋值算术运算符 =》
                _iadd__
                __isub__
                __imul__
                __itruediv__
                __ifloordiv__
                __imod__
                __ipow__
位运算符 =》
            __invert__
            __lshift__
            __rshift__
            __and__
            __or__
            __xor__
反向位运算符 =》
            __rlshift__
            __rrshift__
            __rand__
            __rxor__
            __ror__
增量赋值位运算符 =》
            __ilshift__
            __irshitf__
            __land__
            __ixor__
            __ior__
"""

# 通过实现特殊方法 自定义数据类型可以表现得跟内置类型一样
# 从而写出更具表现力的代码(根据python风格的代码
