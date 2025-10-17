variable "aws_region" {
  description = "AWS region (demo)"
  default     = "us-east-1"
}

variable "ami_id" {
  description = "AMI ID for EC2 instance (demo)"
  default     = "ami-0c94855ba95c71c99"
}

variable "instance_type" {
  description = "EC2 instance type"
  default     = "t2.micro"
}

variable "key_name" {
  description = "SSH key name"
  default     = "demo-key"
}

variable "public_key_path" {
  description = "Path to public SSH key"
  default     = "~/.ssh/id_rsa.pub"
}
