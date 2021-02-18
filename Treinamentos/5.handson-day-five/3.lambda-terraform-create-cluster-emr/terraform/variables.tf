locals {
  function_name = upper("${var.function_name}-${var.env}")
}

variable "account_id" {
  type        = string
  default     = "503147517431"
  description = "Account ID of aws provider to inject in IAM Roles."
}

variable "function_name" {
  type        = string
  default     = "emr-execute-job"
  description = "Lambda function name"
}

variable "env" {
  type        = string
  default     = "dev"
  description = "Environment to add in resource name. Eg: dev."
}

variable "region" {
  type        = string
  default     = "us-east-2"
  description = "Region name to inject in IAM Roles."
}
