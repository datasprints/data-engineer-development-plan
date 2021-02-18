resource "aws_s3_bucket" "bucket_teste" {
  bucket = "rocketdata-tf-first-bucket"
  acl    = "private"

  versioning {
    enabled = true
  }

  tags = {
    Name        = "Mybucket"
    Environment = "DataRocket"

    Name        = "S3"
    Environment = "DataRocket"
  }
}

resource "aws_s3_bucket_public_access_block" "block_access_public" {
  bucket = aws_s3_bucket.bucket_teste.id

  block_public_acls   = true
  block_public_policy = true
  ignore_public_acls = true
  restrict_public_buckets = true
}