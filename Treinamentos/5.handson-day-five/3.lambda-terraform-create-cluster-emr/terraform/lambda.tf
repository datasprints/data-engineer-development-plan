resource "aws_lambda_function" "lambda_function" {
  filename      = data.archive_file.file.output_path
  function_name = local.function_name
  role          = aws_iam_role.iam_for_lambda.arn
  handler       = "main.lambda_handler"
  memory_size   = 128
  timeout       = 30

  source_code_hash = data.archive_file.file.output_base64sha256

  runtime = "python3.8"

  tags = {
    lambda = "emr"
  }

}

data "archive_file" "file" {
  type        = "zip"
  source_dir  = "lambda_code/"
  output_path = "build/${local.function_name}.zip"
}

resource "aws_cloudwatch_log_group" "log_group" {
  name = "/aws/lambda/${local.function_name}"
  retention_in_days = 5
}