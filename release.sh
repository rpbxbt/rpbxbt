#!/bin/bash
set -e
VERSION=$(git describe --tags --abbrev=0 2>/dev/null || echo "0.1.0")
rm -rf dist
mkdir dist
BELONGING_TAR=dist/belonging-$VERSION.tar.gz
NEXUS_TAR=dist/nexus_ai-$VERSION.tar.gz
tar -czf "$BELONGING_TAR" belonging data README.md LICENSE

tar -czf "$NEXUS_TAR" nexus_ai data README.md LICENSE

echo "Created $BELONGING_TAR and $NEXUS_TAR"
