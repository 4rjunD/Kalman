# Kalman
# Kalman Filter Pose Fusion

This project demonstrates how to use a **Kalman Filter** to fuse pose estimates from two cameras and optionally incorporate historical data for improved estimation.

## Overview

The goal of this program is to combine pose data from two cameras, using a Kalman filter to produce a more accurate fused pose estimate. The program also allows the incorporation of historical data for further refinement of the pose estimate.

The system uses **6-dimensional pose data** (e.g., position and velocity in 3D space) as input from two cameras and an optional historical dataset, then fuses them using a Kalman filter to provide a single, refined pose estimate.

## Features

- **Kalman Filter Initialization**: The filter is initialized with state and measurement dimensions set to 6, representing a 6D pose.
- **Pose Fusion**: Pose estimates from two cameras are averaged, with optional historical data weighted in the final estimate.
- **Kalman Filter Update**: The filter's predict-update cycle is used to refine the estimate based on measurements.

## Requirements

- Python 3.x
- `numpy` library
- `filterpy` library (for Kalman filter)

You can install the required dependencies using:

```bash
pip install numpy filterpy
