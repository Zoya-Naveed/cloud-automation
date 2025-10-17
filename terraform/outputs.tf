output "instance_id" {
  value = aws_instance.dev_vm.id
}

output "instance_public_ip" {
  value = aws_instance.dev_vm.public_ip
}
