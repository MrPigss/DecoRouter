from starlette.routing import Route


class Router:
    """decorator factory that generates paths for starlette with the use of decorators.

    Yields:
        Route: starlette Route objects
    """

    def __init__(self) -> None:
        self._routes = {}

    def method(self, name):
        def decorator(path: str = None):
            def inner(func):
                fname = func.__name__
                if fname in self._routes:
                    self._routes[fname].methods.add(name.upper())
                else:
                    self._routes[fname] = Route(path, func, methods=[name])

                return func

            return inner

        return decorator

    def __getattr__(self, item: str):
        if item.upper() == "GET":
            self.method("HEAD")
        return self.method(item)

    def __iter__(self):
        for route in (r := self._routes):
            yield r[route]
