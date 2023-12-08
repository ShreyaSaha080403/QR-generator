# QR Code Generator

QR Code Generator is a simple web application built with Flask that allows users to generate QR codes for provided URLs.

SEE IT FOR YOURSELF --> LINK: http://127.0.0.1:5000

## Features

- Generate QR codes for URLs.
- View the generated QR code image.
- Return to the home page to generate another QR code.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/<your-username>/qr-code-generator.git
    cd qr-code-generator
    ```

2. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open your web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).
3. Enter a URL, generate a QR code, and view the result.
4. To generate another QR code, click the "Return to Home" button.

## Dependencies

- Flask
- qrcode[pil]

Install the dependencies using the following command:

```bash
pip install -r requirements.txt
