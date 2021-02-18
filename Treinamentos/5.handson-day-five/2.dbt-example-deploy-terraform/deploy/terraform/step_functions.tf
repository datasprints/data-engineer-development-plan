resource "aws_iam_role" "step_function_role" {
  name = "${var.project}-step-function-role"
  description = "Allow Step Functions to access AWS resources"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "Service": "states.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF
}

resource "aws_iam_policy" "step_function_policy" {
  name        = "${var.project}-step-function-policy"

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "ecs:DescribeTasks",
        "ecs:RunTask",
        "ecs:StopTask"
      ],
      "Effect": "Allow",
      "Resource": "*"
    },
    {
      "Action": [
        "iam:PassRole"
      ],
      "Effect": "Allow",
      "Resource": "*"
    },
    {
      "Action": [
        "events:DescribeRule",
        "events:PutTargets",
        "events:PutRule"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "attach_policy_step_function_role" {
  role       = aws_iam_role.step_function_role.name
  policy_arn = aws_iam_policy.step_function_policy.arn
}

data "template_file" "state_machine" {
  template = file("templates/state_machine.tpl")
  vars = {
    ecs_cluster = aws_ecs_cluster.ecs_cluster.arn
    ecs_task_name = "${var.project}-task"
    subnet_1 = var.subnet1
    security_group_1 = var.security_group
    retry_seconds = 5
    retry_backoff = 1.5
    retry_attempts = 3
  }
}

resource "aws_sfn_state_machine" "sfn_state_machine" {
  name     = "${var.project}-with-deps"
  role_arn = aws_iam_role.step_function_role.arn

  definition = data.template_file.state_machine.rendered
}