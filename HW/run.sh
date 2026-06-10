#!/bin/bash
COMMAND=$1
if [ "$COMMAND" = "build_generator" ]; then docker build -t csv-generator ./generator
elif [ "$COMMAND" = "run_generator" ]; then docker run --rm -v "$(pwd)/data:/data" csv-generator
elif [ "$COMMAND" = "create_local_data" ]; then python generator/generate.py local_data
elif [ "$COMMAND" = "build_reporter" ]; then docker build -t csv-reporter ./reporter
elif [ "$COMMAND" = "run_reporter" ]; then docker run --rm -v "$(pwd)/data:/data" csv-reporter
elif [ "$COMMAND" = "structure" ]; then find .
elif [ "$COMMAND" = "clear_data" ]; then rm -f data/*.csv rm -f data/*.html
elif [ "$COMMAND" = "inside_generator" ]; then docker run --rm -v "$(pwd)/data:/data" csv-generator ls /data
elif [ "$COMMAND" = "inside_reporter" ]; then docker run --rm -v "$(pwd)/data:/data" csv-reporter ls /data
else
    echo "Unknown command"
fi