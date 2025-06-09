#!/bin/bash
set -e
VERSION=$(git describe --tags --abbrev=0 2>/dev/null || echo "0.1.0")
rm -rf dist
mkdir dist
TAR=dist/belonging-$VERSION.tar.gz
tar -czf "$TAR" belonging data README.md LICENSE
echo "Created $TAR"
