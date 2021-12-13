#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x0345391B55AA1521 (bremner@unb.ca)
#
Name     : notmuch
Version  : 0.34.2
Release  : 43
URL      : https://notmuchmail.org/releases/notmuch-0.34.2.tar.xz
Source0  : https://notmuchmail.org/releases/notmuch-0.34.2.tar.xz
Source1  : https://notmuchmail.org/releases/notmuch-0.34.2.tar.xz.asc
Summary  : Thread-based email index, search and tagging
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+ LGPL-2.1
Requires: notmuch-bin = %{version}-%{release}
Requires: notmuch-data = %{version}-%{release}
Requires: notmuch-lib = %{version}-%{release}
Requires: notmuch-license = %{version}-%{release}
Requires: talloc-lib
BuildRequires : Sphinx
BuildRequires : buildreq-distutils3
BuildRequires : gmime
BuildRequires : gmime-dev
BuildRequires : gnupg
BuildRequires : pypi(cffi)
BuildRequires : ruby
BuildRequires : talloc
BuildRequires : talloc-dev
BuildRequires : valgrind
BuildRequires : xapian-core-dev
BuildRequires : zlib
BuildRequires : zlib-dev
Patch1: dont-fail-on-unrecognized-option.patch

%description
Fast system for indexing, searching, and tagging email.  Even if you
receive 12000 messages per month or have on the order of millions of
messages that you've been saving for decades, Notmuch will be able to
quickly search all of it.

Notmuch is not much of an email program. It doesn't receive messages
(no POP or IMAP support). It doesn't send messages (no mail composer,
no network code at all). And for what it does do (email search) that
work is provided by an external library, Xapian. So if Notmuch
provides no user interface and Xapian does all the heavy lifting, then
what's left here? Not much.

%package bin
Summary: bin components for the notmuch package.
Group: Binaries
Requires: notmuch-data = %{version}-%{release}
Requires: notmuch-license = %{version}-%{release}

%description bin
bin components for the notmuch package.


%package data
Summary: data components for the notmuch package.
Group: Data

%description data
data components for the notmuch package.


%package dev
Summary: dev components for the notmuch package.
Group: Development
Requires: notmuch-lib = %{version}-%{release}
Requires: notmuch-bin = %{version}-%{release}
Requires: notmuch-data = %{version}-%{release}
Provides: notmuch-devel = %{version}-%{release}
Requires: notmuch = %{version}-%{release}

%description dev
dev components for the notmuch package.


%package lib
Summary: lib components for the notmuch package.
Group: Libraries
Requires: notmuch-data = %{version}-%{release}
Requires: notmuch-license = %{version}-%{release}

%description lib
lib components for the notmuch package.


%package license
Summary: license components for the notmuch package.
Group: Default

%description license
license components for the notmuch package.


%prep
%setup -q -n notmuch-0.34.2
cd %{_builddir}/notmuch-0.34.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1639417613
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static --without-docs
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1639417613
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/notmuch
cp %{_builddir}/notmuch-0.34.2/COPYING %{buildroot}/usr/share/package-licenses/notmuch/36e7b160de7f366db25bd7d9f31efd49e8cbe510
cp %{_builddir}/notmuch-0.34.2/COPYING-GPL-3 %{buildroot}/usr/share/package-licenses/notmuch/c5c371a4b28c34d8951a989d53cd28d6035b9662
cp %{_builddir}/notmuch-0.34.2/bindings/python/docs/COPYING %{buildroot}/usr/share/package-licenses/notmuch/0dd432edfab90223f22e49c02e2124f87d6f0a56
cp %{_builddir}/notmuch-0.34.2/contrib/go/LICENSE %{buildroot}/usr/share/package-licenses/notmuch/01a6b4bf79aca9b556822601186afab86e8c4fbf
cp %{_builddir}/notmuch-0.34.2/debian/copyright %{buildroot}/usr/share/package-licenses/notmuch/cbd7a33d29f170fcd1a8e1d391891574e449c01f
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/notmuch

%files data
%defattr(-,root,root,-)
/usr/share/zsh/site-functions/_email-notmuch
/usr/share/zsh/site-functions/_notmuch

%files dev
%defattr(-,root,root,-)
/usr/include/notmuch.h
/usr/lib64/libnotmuch.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libnotmuch.so.5
/usr/lib64/libnotmuch.so.5.5.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/notmuch/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/notmuch/0dd432edfab90223f22e49c02e2124f87d6f0a56
/usr/share/package-licenses/notmuch/36e7b160de7f366db25bd7d9f31efd49e8cbe510
/usr/share/package-licenses/notmuch/c5c371a4b28c34d8951a989d53cd28d6035b9662
/usr/share/package-licenses/notmuch/cbd7a33d29f170fcd1a8e1d391891574e449c01f
