def validate_records(records, schema):
    results = []
    
    for i, record in enumerate(records):
        errors = []
        is_valid = True
        
        for col_def in schema:
            col = col_def['column']
            expected_type = col_def['type']
            
            # 1. Missing Check
            if col not in record:
                errors.append(f"{col}: missing")
                is_valid = False
                continue
            
            val = record[col]
            
            # 2. Null Check
            if val is None:
                if not col_def.get('nullable', False):
                    errors.append(f"{col}: null")
                    is_valid = False
                continue # Skip type/range if None
            
            # 3. Type Check
            actual_type = type(val)
            type_match = False
            if expected_type == "float":
                type_match = actual_type in [float, int]
            elif expected_type == "int":
                type_match = actual_type is int
            elif expected_type == "str":
                type_match = actual_type is str
                
            if not type_match:
                errors.append(f"{col}: expected {expected_type}, got {actual_type.__name__}")
                is_valid = False
                continue
                
            # 4. Range Check
            if expected_type in ["int", "float"]:
                if 'min' in col_def and val < col_def['min']:
                    errors.append(f"{col}: out of range")
                    is_valid = False
                elif 'max' in col_def and val > col_def['max']:
                    errors.append(f"{col}: out of range")
                    is_valid = False
                    
        results.append((i, is_valid, errors))
        
    return results