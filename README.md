# Link Grabber From Website 👋
[![License: mit](https://img.shields.io/badge/License-mit-yellow.svg)](LICENCE.MD)
[![Twitter: asdasd](https://img.shields.io/twitter/follow/CodeAx4.svg?style=social)](https://youtube.com/codeax10)

<b> To create a README for this code, I would suggest providing an overview of what the code does, how to use it, and any dependencies it requires. <b>
<br>
<br>

## Usage
```sh
python link_grabber.py <url> [--depth <n>]
```
<br>
Arguments:

* `<url>`                  : This URL of the website to extract links from.
* `--depth <n>` (Optional) : The maximum depth to follow links. Default is 1.

## Example usge:
```sh
python link_grabber.py https://example.com --depth 2
```

# Dependencies
This script requires the following Python modules:
* requests
* pyfiglet
<br>

<b> You can install these modules using pip: </b>

```sh
pip install requests pyfiglet
```

## 😎 Improvements
> The modified code improves the original by using argparse for command-line arguments, requests instead of urllib, error handling, parallelization, depth limit, and a function for parsing. <br>

## 🚀 Future Work
- Add support for specifying output file or directory
- Implement progress bar for displaying progress during link extraction
- Add option for excluding certain types of links (e.g., images, videos)
- Improve error handling and reporting

> If you have any suggestions for further improvements or feature requests, please feel free to create an [issue](https://github.com/CodeAx1avek/Link-extractor-from-url/pulls) or submit a pull request.
<br>
<br>

## 🤝 Contributing

Contributions, issues and feature requests are welcome!

- How to contribute [Click Here](CONTRIBUTING.md)
- Feel free to check [issues page](https://github.com/CodeAx1avek/Link-extractor-from-url/pulls).
<br>
<br>

## ❤️ Show your support
Give a ⭐️ if this project helped you!
<br>
<br>

# ⚖️ License

Copyright © 2023 [CodeAx1](https://github.com/CodeAx1avek).

This project is [MIT]() licensed.
