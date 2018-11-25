provider "aws" {
  access_key = "${var.aws_access_key}"
  secret_key = "${var.aws_secret_key}"
  region     = "${var.aws_region}"
}

resource "aws_default_vpc" "default" {
  tags {
    Name = "Default VPC"
  }
}

resource "aws_instance" "catapult" {
  tags {
    Name  = "catapult"
    Owner = "${var.key_name}"
  }

  ami                    = "ami-0f65671a86f061fcd"
  key_name               = "${var.key_name}"
  instance_type          = "t2.micro"
  associate_public_ip_address = "true"

  connection {
    type        = "ssh"
    user        = "ubuntu"
    host        = "${self.public_ip}"
    private_key = "${file("${var.private_key_path}")}"
  }

  provisioner "file" {
  source      = "${path.cwd}/restartServerApp.sh"
  destination = "/home/ubuntu/restartServerApp.sh"
  }

  provisioner "remote-exec" {
    inline = ["sudo apt install python -y"]
  }

  provisioner "local-exec" {
      command = "ansible-playbook -u ubuntu -i '${self.public_ip},' --private-key ${var.private_key_path} provision.yml"
  }

  provisioner "remote-exec" {
    inline = ["chmod +x /home/ubuntu/restartServerApp.sh",
              "sudo /home/ubuntu/restartServerApp.sh",
              ]
  }

}

resource "aws_default_security_group" "default" {
  vpc_id = "${aws_default_vpc.default.id}"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
