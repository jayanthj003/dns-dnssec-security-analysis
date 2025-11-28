#!/bin/bash

# === CONFIG ===
DOMAIN="smith2022.edu"
ZSK_COUNT=${1:-50}  # Default ZSK count = 50

echo "Generating 1 KSK for $DOMAIN..."
dnssec-keygen -a RSASHA256 -b 2048 -f KSK $DOMAIN

echo "Generating $ZSK_COUNT ZSKs for $DOMAIN..."
for i in $(seq 1 $ZSK_COUNT); do
    echo "Generating ZSK $i..."
    dnssec-keygen -a RSASHA256 -b 1024 $DOMAIN
done

echo "✅ All keys generated for $DOMAIN."

