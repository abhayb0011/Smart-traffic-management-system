# Smart Traffic Management System

A technology solution that integrates real-time vehicle detection with dynamic signal control to optimize traffic flow at intersections.

## Features

* **Real-Time Vehicle Detection**: Uses YOLO and OpenCV to identify and count vehicles in each lane.
* **Adaptive Signal Timing**: Dynamically adjusts green-light durations based on lane-specific vehicle density.
* **Custom Dataset**: Annotated vehicle dataset prepared with LabelImg for accurate model training.
* **Simulation**: Interactive Pygame simulation showcases system performance and dynamic signal control.

## Technologies

* **YOLO** for object detection
* **OpenCV** for image processing
* **LabelImg** for dataset annotation
* **Pygame** for simulation

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/abhayb0011/Smart-Traffic-Management-System.git
   cd Smart-Traffic-Management-System
   ```

2. Create and activate a Python virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Download or train the YOLO model weights and place them in the `models/` directory.

## Usage

### 1. Run the Pygame Simulation

```bash
python simulation.py
```

The simulation will launch a window showing an urban intersection with vehicles spawning randomly. Adaptive traffic lights will adjust based on detected vehicle count.

### 2. Run the Traffic Management API

```bash
python app.py
```

* The API hosts routes for prediction, history tracking, and signal control logic.
* Integrate with front-end or additional clients as needed.

## Dataset

* The dataset is annotated using LabelImg. Images are stored in `data/images/` and annotations in `data/labels/`.
* To add more data, annotate new frames and place them in the respective directories.
