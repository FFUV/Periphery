import random
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/pi')
def compute_pi():
    num_points = 1000000  # Number of points to generate for pi estimation
    points_inside_circle = 0

    for _ in range(num_points):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        
        distance = (x - 0.5) ** 2 + (y - 0.5) ** 2
        
        if distance <= 0.25:
            points_inside_circle += 1
    
    pi_estimate = 4 * (points_inside_circle / num_points)
    
    return jsonify(pi=pi_estimate)

if __name__ == '__main__':
    app.run()
