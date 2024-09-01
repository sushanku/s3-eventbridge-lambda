resource "aws_s3_bucket" "s3_trigger_eventbridge" {
  bucket = "s3-eventbridge-sushan3"
  tags = {
    Name        = "Eventbridge S3 Bucket"
  }
}

resource "aws_s3_bucket" "s3_trigger_eventbridge_revised" {
  bucket = "s3-eventbridge-sushan-revised-3"
  tags = {
    Name        = "Eventbridge S3 Bucket"
  }
  }

resource "aws_s3_bucket_notification" "bucket_notification" {
  bucket      = aws_s3_bucket.s3_trigger_eventbridge.id
  eventbridge = true
}
