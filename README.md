<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Best-README-Template</h3>

  <p align="center">
    An awesome README template to jumpstart your projects!
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
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
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
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

---

One of the things that I love about FastAPI is how easy it is to setup different routes. Just use a decorator above the function that corresponds to that route and done.
[![FastAPI Screen Shot][FastAPI-screenshot]](./images/FastAPI.png)
It's easy to see wich route corresponds to wich function and vice versa.

<p align="right">(<a href="#top">back to top</a>)</p>

### The less good

---

In starlette you first declare different functions and then at the end of the file you map the path, allowed HTTP methods and endpoint function together.
[![scarlette Screen Shot][starlette-screenshot]](./images/scarlette.png)

This makes it easy to make mistakes as there is not way to immediatly know wich endoint corresponds to a certain function, unless you go look in the routes at the end of the file. They might not even be declared in that file at all.

<p align="right">(<a href="#top">back to top</a>)</p>

### The best of both

---

DecoRouter auto generates your routes for you based on decorators, just like FastAPI. The downside is that you have to import an extra module, but the added bonus of easier to read and maintain code is certainly worth it.
[![decoRouter Screen Shot][decoRouter-screenshot]](./images/DecoRouter.png)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

To get started follow these simple example steps.

### Installation

You can install the module using pip.
* `> pip install decorouter`
<p align="right">(<a href="#top">back to top</a>)</p>


## Usage

To use decoRouter you will need to know how starlette works.
decoRouter will not create an app for you, it will only generate the routes.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Thomas - [@TEeckhout](https://twitter.com/@TEeckhout) - thomas.eeckhout@outlook.be

Project Link: [https://github.com/MrPigss/DecoRouter](https://github.com/MrPigss/DecoRouter)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
Thank you
* [Starlette](https://www.starlette.io/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Img Shields](https://shields.io)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues

[linkedin-url]: https://www.linkedin.com/in/thomas-eeckhout-761500181/
[linkedIn-shield]: https://img.shields.io/badge/LinkedIn-blue?logo=linkedin&style=flat

[decoRouter-screenshot]: images/DecoRouter.png
[starlette-screenshot]: images/starlette.png
[FastAPI-screenshot]: images/FastAPI.png
