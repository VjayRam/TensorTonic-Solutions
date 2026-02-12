def linear_interpolation(values):
    """
    Fill missing (None) values using linear interpolation.
    """
    # Write code here
    result = list(values)
    n = len(result)

    i = 0 
    while i < n:
        if result[i] is None:
            left_idx = i - 1
            right_idx = i 

            while right_idx < n and result[right_idx] is None:
                right_idx += 1

            v_left = result[left_idx]
            v_right = result[right_idx]

            num_steps = right_idx - left_idx

            delta_v = v_right - v_left

            for j in range(left_idx + 1, right_idx):
                steps_from_l = j - left_idx
                result[j] = v_left + (steps_from_l / num_steps) * delta_v
            
            i = right_idx
        
        else:
            i += 1
    
    return result