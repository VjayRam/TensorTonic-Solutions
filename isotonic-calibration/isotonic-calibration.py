import numpy as np

def calibrate_isotonic(cal_labels, cal_probs, new_probs):
    """
    Apply isotonic regression calibration using PAVA.
    """
    # 1. Sort calibration data
    indices = np.argsort(cal_probs)
    sorted_probs = np.array(cal_probs)[indices]
    sorted_labels = np.array(cal_labels)[indices].astype(float)
    
    # 2. Fit Isotonic Regression (PAVA)
    # Each element: [sum_of_labels, count_of_elements]
    stack = []
    for label in sorted_labels:
        new_block = [label, 1]
        while stack and (stack[-1][0] / stack[-1][1]) >= (new_block[0] / new_block[1]):
            prev_sum, prev_count = stack.pop()
            new_block[0] += prev_sum
            new_block[1] += prev_count
        stack.append(new_block)
        
    # Expand blocks back into a full calibrated array
    calibrated_values = []
    for val_sum, count in stack:
        calibrated_values.extend([val_sum / count] * count)
    calibrated_values = np.array(calibrated_values)

    # 3. Transform new_probs using Linear Interpolation
    # np.interp handles clamping automatically for values outside the range
    result = np.interp(new_probs, sorted_probs, calibrated_values)
    
    return result.tolist()