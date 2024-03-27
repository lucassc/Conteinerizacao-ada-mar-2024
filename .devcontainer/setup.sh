#!/usr/bin/env bash

echo "Configurando seu codespace..."

#
echo "Configurando docker completion for bash"
echo "" >> ~/.bashrc
echo "source <(docker completion bash)" >> ~/.bashrc

source <(docker completion bash)