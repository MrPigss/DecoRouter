from starlette.routing import Route

class Router:
    """decorator factory that generates paths for starlette with the use of decorators.

    Yields:
        Route: starlette Route objects
    """
    _routes = {}

    @staticmethod
    def method(name):
        def decorator(path: str = None):
            def inner(func):
                fname = func.__name__
                if fname in Router._routes:
                    Router._routes[fname].methods.add(name.upper())
                else:
                    Router._routes[fname] = Route(path, func, methods = [name])

                return func

            return inner
        return decorator

    def __getattribute__(self, item: str):
        return Router.method(item)

    @staticmethod
    def __iter__():
        for route in (r:=Router._routes):
            yield r[route]

