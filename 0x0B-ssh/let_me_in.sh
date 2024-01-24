#!/bin/bash

# Server details
server=3.85.136.169
user="ubuntu"

# SSH public key
ssh_public_key="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCSlrX3Q11kF8rfwQm1yCIjG4std3+dJRz9pUvWA1dyABV8//Y5uhO9cOe60LwDYWRjvouCWeNxZVXulRUURut5zYgTFqpKRDMLFEvB2yPMn6ytapxJW9YMke+LgJHhiKHz1DAxc4dSvZYWkt2noyBM1xZSJbb4HYItm+U+5lnpsbQXcsndTq3qQuNmDF4X7Xb0Bn+qzb/gqEPtkXDdWDzCXwonGlUoo/j5sJNdtK/QhCxc0lveMJtpnYrqdJ5sZx5L6G0O4xrmMjet+YT7BtS0QA/ZX/xi4Jhsz59/vQIw8nvkDQlOIefseAzeHz/UUQiOjbcRzMwSFV4ikVdjtKkT6BtKpjaVleTbzc++rlceGbQZwd0jJRReFiAvCd7WrBRxDW+fr2fXFV27DcQfIsLjLwJ0QzafyRtY7Nz4+2H/U02qY2x4HM7gG+qW7PTD5e/J4EAM2w6PkN8cZEJ/Psj8a7C8lt6ft6mca4E7WLjx4/z1R2n46eRTveE7WueewBNN1uj5TEGSYC/gUYVek7P3EwRhLHq6eq4WDb4IZgV2+MSNMR5wMrRhurhWVvzQB+nJgKgbZ78IuSXcuOWUCxghcz0nkHzGsuxVROfw2xFTCsal8v+oDJpDgR8Y0zwBq257Xi+bhDvrpzwkeCHe+nyFpD8P4ClzIutOJI7i5FI41Q== kidus@kidus-ThinkPad-T14-Gen-1"
# Connect to the server and add the SSH public key to authorized_keys
ssh ubuntu@35.153.98.251 "mkdir -p ~/.ssh && echo \"$ssh_public_key\" >> ~/.ssh/authorized_keys && chmod 700 ~/.ssh && chmod 600 ~/.ssh/authorized_keys"

echo "SSH public key added to the server for user '$user'."
