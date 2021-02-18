{
  "StartAt": "dbt_run",
  "States": {
    "dbt_run": {
      "Type": "Task",
      "Resource": "arn:aws:states:::ecs:runTask.sync",
      "Parameters": {
        "Cluster": "${ecs_cluster}",
        "TaskDefinition": "${ecs_task_name}",
        "LaunchType": "FARGATE",
        "NetworkConfiguration": {
          "AwsvpcConfiguration": {
            "Subnets": ["${subnet_1}"],
            "AssignPublicIp": "ENABLED",
            "SecurityGroups": ["${security_group_1}"]
          }
        },
        "Overrides": {
          "ContainerOverrides": [
            {
              "Name": "dbt",
              "Command.$": "$.commands"
            }
          ]
        }
      },
      "Retry": [
        {
          "ErrorEquals": ["States.ALL"],
          "IntervalSeconds": ${retry_seconds},
          "BackoffRate": ${retry_backoff},
          "MaxAttempts": ${retry_attempts}
        }
      ],
      "Catch": [
        {
          "ErrorEquals": ["States.ALL"],
          "Next": "FailureNotifier",
          "ResultPath": null
        }
      ],
      "End": true,
      "ResultPath": "$.dbt_run"
    },
    "FailureNotifier": {
      "Type": "Pass",
      "Next": "Failure",
      "ResultPath": "$.notifier"
    },
    "Failure": {
      "Type": "Fail"
    }
  }
}
