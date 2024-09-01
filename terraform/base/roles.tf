resource "aws_iam_role" "s3_eventbridge_role" {
  name = "s3_eventbridge_role"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF

  managed_policy_arns = [
    "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole",
    # "arn:aws:iam::aws:policy/service-role/AmazonS3ObjectLambdaExecutionRolePolicy"
    "arn:aws:iam::aws:policy/service-role/AWSLambdaRole"
  ]
}

resource "aws_iam_policy" "s3_read_write_policy" {
  name        = "S3ReadWritePolicy"
  description = "A policy to allow read and write access to a specific S3 bucket."

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": ["${aws_s3_bucket.s3_trigger_eventbridge.arn}/*", "${aws_s3_bucket.s3_trigger_eventbridge_revised.arn}/*"]
    }
  ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "s3_eventbridge_policy_attachment" {
  policy_arn = aws_iam_policy.s3_read_write_policy.arn
  role       = aws_iam_role.s3_eventbridge_role.name
}
