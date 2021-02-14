# Machine Learning Projects

[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

> Keywords: `machine learning`, `data science`, `kmeans`,`classication`, `streamlit`, `clustering`

## Table of Contents

- [Project List](#projects)
  - [KMeans image predominant colors detection](#kmeans-image-predominant-colors-detection)
- [Contact](#contact)
- [License](#license)

## Projects

### Kmeans image predominant colors detection

[View Code](https://github.com/marcosmapl/ml-projects/blob/main/kmeans-color-detection.py)

This project is a small APP using Python and [Streamlit](https://www.streamlit.io/) to detect a certain number of predominant colors in an image using the KMeans algorithm. The project allows the user to choose: an image (from some sample images saved in `img`project folder) and a desired number of colors.

Once the selection is made, the APP maps the chosen image into an array of pixels. This array still undergoes a scaling process so that the KMeans algorithm can be applied to it. Through the KMeans algorithm, the central pixels of the image are identified, in RGB format. 

For each pixel, the RGB code is converted to hexadecimal format and is passed as a parameter in an HTTP request to the API. This API provides information about the color referring to the passed hexadecimal code. In response to the request, an JSON object is returned. Finally, the APP lists all identified colors and their information!

> Requeriments | Install command
> --- | ---
> __Streamlit__ | `pip install streamlit`
> __Matplotlib__ | `pip install matplotlib`
> __PIL__ | `pip install pil` (cannot coexists with Pillow)
> __Numpy__ | `pip install numpy`
> __Pandas__ | `pip install pandas`
> __Requests__ | `pip install requests`

To run the project execute the following command via terminal/prompt:
> streamlit run kmeans-color-detection.py

## Contact

Marcos Lima [![LinkedIn][linkedin-shield]][linkedin-url]

marcos.lima@icomp.ufam.edu.br

[See my project on GitHub](https://github.com/marcosmapl/ml-projects/)

## License

- Copyright 2020 © [marcosmapl](https://github.com/marcosmapl).

<!-- Markdown link & img dfn's -->
[wiki]: https://github.com/marcosmapl/ml-projects/wiki
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/marcosmapl
[forks-shield]: https://img.shields.io/github/forks/marcosmapl/ml-projects.svg?style=flat-square
[forks-url]: https://github.com/marcosmapl/ml-projects/network/members
[stars-shield]: https://img.shields.io/github/stars/marcosmapl/ml-projects.svg?style=flat-square
[stars-url]: https://github.com/marcosmapl/ml-projects/stargazers
[issues-shield]: https://img.shields.io/github/issues/marcosmapl/ml-projects.svg?style=flat-square
[issues-url]: https://github.com/marcosmapl/ml-projects/issues
