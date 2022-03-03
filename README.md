<div id="top"></div>

[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <!-- <a href="https://github.com/MrPigss/DecoRouter">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

  <h2 align="center">DecoRouter</h3>

  <p align="center">
    A FastAPI style router for Starlette.
    <br />
    <a href="https://github.com/MrPigss/DecoRouter"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/MrPigss/DecoRouter">View Demo</a>
    ·
    <a href="https://github.com/MrPigss/DecoRouter/issues">Report Bug</a>
    ·
    <a href="https://github.com/MrPigss/DecoRouter/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#the-good">The good</a></li>
        <li><a href="#the-less-good">The less good</a></li>
        <li><a href="#the-best-of-both">The best of both</a></li>
      </ul>
    </li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![decoRouter Screen Shot][decoRouter-screenshot]](./images/DecoRouter.png)

FastApi is a great tool for developping API's in a quick and easy way. In their own words:
>FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

It is build using starlette wich is in their own words:
>a lightweight ASGI framework/toolkit, which is ideal for building high performance asyncio services.


### The good

One of the things that I love about FastAPI is how easy it is to setup different routes. Just use a decorator above the function that corresponds to that route and done.
[![FastAPI Screen Shot][FastAPI-screenshot]](./images/FastAPI.png)
It's easy to see wich route corresponds to wich function and vice versa.

<p align="right">(<a href="#top">back to top</a>)</p>

### The less good

In starlette you first declare different functions and then at the end of the file you map the path, allowed HTTP methods and endpoint function together.
[![starlette Screen Shot][starlette-screenshot]](./images/Starlette.png)

This makes it easy to make mistakes as there is not way to immediatly know wich endoint corresponds to a certain function, unless you go look in the routes at the end of the file. They might not even be declared in that file at all.

<p align="right">(<a href="#top">back to top</a>)</p>

### The best of both

DecoRouter auto generates your routes for you based on decorators, just like FastAPI. The downside is that you have to import an extra module, but the added bonus of easier to read and maintain code is certainly worth it.
[![decoRouter Screen Shot][decoRouter-screenshot]](./images/DecoRouter.png)

<p align="right">(<a href="#top">back to top</a>)</p>


## Installation
You can simply install the module using pip.
* `> pip install decorouter`
<p align="right">(<a href="#top">back to top</a>)</p>


## Usage

To use decoRouter you will need to know how starlette works.
decoRouter will not create an app for you, it will only generate the routes.

_For more info regarding starlette, please refer to the [Documentation](https://www.starlette.io/)_

### Example
below is a basic example.  
There is one endpoint '`/`' wich only accepts `GET` requests, and returns `{'hello': 'world'}`.
* example.py:

```python
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from decoRouter import Router

router = Router()

@router.get('/')
async def homepage(request):
    return JSONResponse({'hello': 'world'})


app = Starlette(routes=router)
```
Then run the application...

```sh
$ uvicorn example:app
```

---

### Multiple HTTP methods
It's also possible to accept multiple HTTP methods for one endpoint.  
Below you can see one endpoint '`/`' wich accepts both `POST` and `PUT` requests.

```python
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from decoRouter import Router

router = Router()

@router.PUT()
@router.POST('/')
async def homepage(request):
    return JSONResponse({'hello': 'world'})


app = Starlette(routes=router)
```

As you can see only the last decorator has a path. It is not necessary to define it multiple times as only the last one will be used.

For example:
```python
@router.PUT()
@router.POST('/')
@router.POST('/home')
async def home(request):
    pass
```
Above, the second decorator will do nothing.  
This will result in the endpoint '`/home`' accepting both `PUT` and `POST` requests.
The endpoint '`/`' will return a 404.

This means that there is ONE endpoint per function.
You can't add multiple endpoints to the same function or vice versa.

---

### Multiple endpoints
Unique endpoints are created based on the function name.  
The function names will have no influence over the path of the endpoint.
If a function with a duplicate name is created it will NOT override the original one.
This this means.  
_Duplicate function names will be ignored, only the first one will be used._

```python
@router.get('/')
async def home(request):
    pass

@router.get('/home')
async def home(request):
    pass
```

The above will result in only one endpoint: '`/`'.  
The second occurence of home will be ignored


---

### Extra
starlette does not check for correct HTTP methods, so neither does decoRouter.
Methods are case insensitive. `router.get()` is the same as `router.GET()` or even `router.GeT()`. 
And since there are no checks, things like  `router.ilasdfggb()` are perfectly fine and will not result in an error. Keep this in mind while debugging.
<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Thomas - [@TEeckhout](https://twitter.com/@TEeckhout) - [LinkedIn](https://www.linkedin.com/in/thomas-eeckhout-761500181) - thomas.eeckhout@outlook.be  
Project Link: [https://github.com/MrPigss/DecoRouter](https://github.com/MrPigss/DecoRouter)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
Thank you
* [Starlette](https://www.starlette.io/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Img Shields](https://shields.io)

<p align="right">(<a href="#top">back to top</a>)</p>

## PS.
Apparently starlette still supports using decorators but these are not documented anywhere since they are deprecated since 0.13.0, see [changelog][changelog].

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/MrPigss/DecoRouter.svg?style=flat
[contributors-url]: https://github.com/MrPigss/DecoRouter/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/MrPigss/DecoRouter.svg?style=flat
[forks-url]: https://github.com/MrPigss/DecoRouter/network/members

[stars-shield]: https://img.shields.io/github/stars/MrPigss/DecoRouter.svg?style=flat
[stars-url]: https://github.com/MrPigss/DecoRouter/stargazers

[issues-shield]: https://img.shields.io/github/issues/MrPigss/DecoRouter.svg?style=flat
[issues-url]: https://github.com/MrPigss/DecoRouter/issues

[linkedin-url]: https://www.linkedin.com/in/thomas-eeckhout-761500181/
[linkedIn-shield]: https://img.shields.io/badge/LinkedIn-blue?logo=linkedin&style=flat

[decoRouter-screenshot]: images/DecoRouter.png
[starlette-screenshot]: images/Starlette.png
[FastAPI-screenshot]: images/FastAPI.png

[changelog]: https://www.starlette.io/release-notes/#:~:text=memory%20upload%20files.-,0.13.0,style%20in%20favour%20of%20declarative%20routing%20tables%20and%20middleware%20definitions.,-0.12.12