#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dropwatch
Version  : 1.5.1
Release  : 4
URL      : https://github.com/nhorman/dropwatch/archive/v1.5.1.tar.gz
Source0  : https://github.com/nhorman/dropwatch/archive/v1.5.1.tar.gz
Summary  : Kernel dropped packet monitor
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: dropwatch-bin = %{version}-%{release}
Requires: dropwatch-license = %{version}-%{release}
Requires: dropwatch-man = %{version}-%{release}
Requires: binutils
BuildRequires : binutils
BuildRequires : binutils-dev
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(libnl-3.0)
BuildRequires : pkgconfig(readline)
BuildRequires : readline-dev
Patch1: 0001-Fix-bfd-build-failure.patch

%description
dropwatch is an utility to interface to the kernel to monitor for dropped
network packets.

%package bin
Summary: bin components for the dropwatch package.
Group: Binaries
Requires: dropwatch-license = %{version}-%{release}

%description bin
bin components for the dropwatch package.


%package license
Summary: license components for the dropwatch package.
Group: Default

%description license
license components for the dropwatch package.


%package man
Summary: man components for the dropwatch package.
Group: Default

%description man
man components for the dropwatch package.


%prep
%setup -q -n dropwatch-1.5.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1567273912
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1567273912
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/dropwatch
cp COPYING %{buildroot}/usr/share/package-licenses/dropwatch/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dropwatch

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dropwatch/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/dropwatch.1
