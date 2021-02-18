resource "aws_cloudwatch_event_rule" "cron_events_lambda" {
  name                = "cron-${local.function_name}"
  description         = "All days at 6 PM"
  schedule_expression = "cron(30 18 * * ? *)"
}

resource "aws_cloudwatch_event_target" "check_foo_every_one_minute" {
  rule      = aws_cloudwatch_event_rule.cron_events_lambda.name
  target_id = "lambda_function"
  arn       = aws_lambda_function.lambda_function.arn
}

resource "aws_lambda_permission" "allow_cloudwatch_to_call_check_foo" {
  statement_id  = "AllowExecutionFromCloudWatch"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.lambda_function.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.cron_events_lambda.arn
}