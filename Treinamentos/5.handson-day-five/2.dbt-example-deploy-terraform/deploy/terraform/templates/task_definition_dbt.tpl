[
  {
    "name": "${container_name}",
    "image": "${image}:${image_version}",
    "essential": ${essential},
    "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
            "awslogs-group": "${log_group}",
            "awslogs-region": "${log_region}",
            "awslogs-stream-prefix": "${log_stream_prefix}"
        }
    }
  }
]