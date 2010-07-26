#!/bin/sh
# Build an orig.tar.gz file from a git snapshot
# See also http://www.h5l.org/sources.html

version=$( dpkg-parsechangelog -l`dirname $0`/changelog | sed -n 's/^Version: \(.*:\|\)//p' | sed 's/-[0-9.]\+$//' )

git clone --depth 1 -l git://svn.h5l.org/heimdal.git "heimdal-$version"
pushd "heimdal-$version" && ./autogen.sh && ./configure && make dist && popd
rm -rf "heimdal-$version/.git"
tar cj "heimdal-$version" > "heimdal_$version.orig.tar.bz2"
rm -rf "heimdal-$version"
