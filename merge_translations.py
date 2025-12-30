import json
import os

def merge_json(source_file, target_file):
    if not os.path.exists(target_file):
        with open(target_file, 'w', encoding='utf-8') as f:
            json.dump({}, f)
    
    with open(target_file, 'r', encoding='utf-8') as f:
        target_data = json.load(f)
        
    with open(source_file, 'r', encoding='utf-8') as f:
        source_data = json.load(f)
        
    target_data.update(source_data)
    
    with open(target_file, 'w', encoding='utf-8') as f:
        json.dump(target_data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 2:
        merge_json(sys.argv[1], sys.argv[2])
        print(f"Merged {sys.argv[1]} into {sys.argv[2]}")
