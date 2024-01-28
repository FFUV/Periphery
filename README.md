# Pi Generator

This project is a web application that generates the value of Pi using a Monte Carlo method and presents it in an aesthetically pleasing way.


## Technologies Used

- Front-end: HTML, CSS, JavaScript
- Back-end: Python, Flask

## Features

- Calculates the value of Pi using a Monte Carlo method.
- Generates Pi with a visual representation in a web page.
- Aesthetically pleasing design.

## Setup and Usage

1. Install Python (version 3.7 or higher) if not already installed.
2. Install Flask by running `pip install flask` in the command line.
3. Clone this repository or download the source code.
4. Navigate to the project directory.
5. Run the command `python server.py` to start the server.
6. Open your web browser and go to `http://localhost:5000`.
7. Click on the "Generate Pi" button to compute and display the value of Pi.

## How It Works

The value of Pi is calculated using a Monte Carlo method. The algorithm works as follows:

1. Generate a large number of random points within a unit square.
2. Count the number of points that fall inside a quarter of a unit circle centered at (0.5, 0.5).
3. Estimate the value of Pi using the formula: `pi_estimate = 4 * (points_inside_circle / total_points)`.

The front-end of the web application is built using HTML, CSS, and JavaScript. When the user clicks on the "Generate Pi" button, a request is made to the server. The server generates the random points, performs the calculation, and returns the computed value of Pi to the front-end. The value of Pi is then displayed on the webpage.

## License

This project is licensed under the [MIT License](LICENSE).
