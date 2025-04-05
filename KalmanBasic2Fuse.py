import numpy as np
from filterpy.kalman import KalmanFilter

def initialize_kalman():
    kf = KalmanFilter(dim_x=6, dim_z=6)  # 6 state variables (pose), 6 measurements
    
    kf.F = np.eye(6)
    
    kf.H = np.eye(6)
    
    kf.P *= 1e3  
    kf.R *= 1e1 
    kf.Q *= 1e-2  
    
    return kf

def fuse_pose_estimates(kf, pose_cam1, pose_cam2, historical_data=None):
    measurement = (np.array(pose_cam1) + np.array(pose_cam2)) / 2
    
    # If historical data is available and valid, use it for improved estimation
    if historical_data:
        historical_array = np.array(historical_data)
        if historical_array.shape[0] > 0 and historical_array.shape[1] == 6:
            historical_avg = np.mean(historical_array, axis=0)
            measurement = 0.7 * measurement + 0.3 * historical_avg
    
    # Kalman filter predict-update cycle
    kf.predict()
    kf.update(measurement)
    
    return kf.x  # Fused pose estimate

kf = initialize_kalman()
pose_cam1 = [0.5, 1.2, 0.8, 0.1, 0.05, 0.02]
pose_cam2 = [0.6, 1.1, 0.85, 0.12, 0.04, 0.01]
historical_data = [
    [0.4, 1.0, 0.75, 0.09, 0.03, 0.015],
    [0.45, 1.05, 0.78, 0.1, 0.035, 0.018]
]

fused_pose = fuse_pose_estimates(kf, pose_cam1, pose_cam2, historical_data)
print("Fused Pose Estimate:", fused_pose)
