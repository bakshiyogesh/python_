# Unlike instance methods, static methods aren’t bound to an object. 
# In other words, static methods cannot access and modify an object state.
# In addition, Python doesn’t implicitly pass the cls parameter (or the self parameter) to static methods. 
# Therefore, static methods cannot access and modify the class’s state.
# To define a static method you use the @staticmethod decorator


class KashiNath:
    _rahul='saved'
    # @staticmethod
    def static_method_name(params):
        print("named here")

kashinath=KashiNath()
kashinath.static_method_name()
#to call static method use syntax className.static_method_name
