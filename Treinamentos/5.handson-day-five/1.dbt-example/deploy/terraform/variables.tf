variable "aws_region" {
  type        = string
  default     = "us-east-2"
  description = "Default Region Services"
}

variable "project" {
  type        = string
  default     = "dbt-serverless"
  description = "Project name all components"
}

variable "security_group" {
  type        = string
  default     = "sg-b3c1accd"
  description = "Security group to project"
}

variable "subnet1" {
  type        = string
  default     = "subnet-163a445a"
  description = "Subnet a to projeto"
}