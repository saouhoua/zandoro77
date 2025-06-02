#!/bin/bash

# Function to run a script multiple times
run_script_multiple_times() {
    script_name=$1
    cycles=$2

    for ((i = 1; i <= cycles; i++)); do
        echo "Running $script_name - Cycle $i/$cycles"
        bash "$script_name" || { echo "Error running $script_name"; exit 1; }
    done
}

# Run run0.sh for 10 times, then start.py
echo "Starting initial run of run0.sh for 10 cycles..."
run_script_multiple_times "run0.sh" 10
echo "Running start.py after run0.sh..."
python3 "start.py" || { echo "Error running start.py"; exit 1; }

# Run run1.sh for 10 cycles and start.py, repeated 5 times
for ((j = 1; j <= 5; j++)); do
    echo "Starting cycle $j/5 of run1.sh + start.py..."
    run_script_multiple_times "run1.sh" 10
    echo "Running start.py after run1.sh..."
    python3 "start.py" || { echo "Error running start.py"; exit 1; }
done

echo "Script completed successfully!"
