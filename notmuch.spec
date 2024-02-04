#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v3
# autospec commit: 750e50d
#
# Source0 file verified with key 0x0345391B55AA1521 (bremner@unb.ca)
#
Name     : notmuch
Version  : 0.38.2
Release  : 56
URL      : https://notmuchmail.org/releases/notmuch-0.38.2.tar.xz
Source0  : https://notmuchmail.org/releases/notmuch-0.38.2.tar.xz
Source1  : https://notmuchmail.org/releases/notmuch-0.38.2.tar.xz.asc
Summary  : Thread-based email index, search and tagging
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+ LGPL-2.1
Requires: notmuch-bin = %{version}-%{release}
Requires: notmuch-data = %{version}-%{release}
Requires: notmuch-lib = %{version}-%{release}
Requires: notmuch-license = %{version}-%{release}
Requires: notmuch-man = %{version}-%{release}
Requires: talloc-lib
BuildRequires : buildreq-configure
BuildRequires : gmime
BuildRequires : gmime-dev
BuildRequires : gnupg
BuildRequires : pkgconfig(gpgme)
BuildRequires : pypi-sphinx
BuildRequires : ruby
BuildRequires : talloc
BuildRequires : talloc-dev
BuildRequires : valgrind
BuildRequires : xapian-core-dev
BuildRequires : zlib
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
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


%package man
Summary: man components for the notmuch package.
Group: Default

%description man
man components for the notmuch package.


%prep
%setup -q -n notmuch-0.38.2
cd %{_builddir}/notmuch-0.38.2
%patch -P 1 -p1
pushd ..
cp -a notmuch-0.38.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1707088505
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static
make  %{?_smp_mflags}
popd
%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1707088505
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/notmuch
cp %{_builddir}/notmuch-%{version}/COPYING %{buildroot}/usr/share/package-licenses/notmuch/36e7b160de7f366db25bd7d9f31efd49e8cbe510 || :
cp %{_builddir}/notmuch-%{version}/COPYING-GPL-3 %{buildroot}/usr/share/package-licenses/notmuch/c5c371a4b28c34d8951a989d53cd28d6035b9662 || :
cp %{_builddir}/notmuch-%{version}/bindings/python/docs/COPYING %{buildroot}/usr/share/package-licenses/notmuch/0dd432edfab90223f22e49c02e2124f87d6f0a56 || :
cp %{_builddir}/notmuch-%{version}/contrib/go/LICENSE %{buildroot}/usr/share/package-licenses/notmuch/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
cp %{_builddir}/notmuch-%{version}/debian/copyright %{buildroot}/usr/share/package-licenses/notmuch/cbd7a33d29f170fcd1a8e1d391891574e449c01f || :
pushd ../buildavx2/
%make_install_v3
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/notmuch
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
/V3/usr/lib64/libnotmuch.so.5.6.0
/usr/lib64/libnotmuch.so.5
/usr/lib64/libnotmuch.so.5.6.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/notmuch/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/notmuch/0dd432edfab90223f22e49c02e2124f87d6f0a56
/usr/share/package-licenses/notmuch/36e7b160de7f366db25bd7d9f31efd49e8cbe510
/usr/share/package-licenses/notmuch/c5c371a4b28c34d8951a989d53cd28d6035b9662
/usr/share/package-licenses/notmuch/cbd7a33d29f170fcd1a8e1d391891574e449c01f

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/nmbug.1.gz
/usr/share/man/man1/notmuch-address.1.gz
/usr/share/man/man1/notmuch-compact.1.gz
/usr/share/man/man1/notmuch-config.1.gz
/usr/share/man/man1/notmuch-count.1.gz
/usr/share/man/man1/notmuch-dump.1.gz
/usr/share/man/man1/notmuch-emacs-mua.1.gz
/usr/share/man/man1/notmuch-git.1.gz
/usr/share/man/man1/notmuch-insert.1.gz
/usr/share/man/man1/notmuch-new.1.gz
/usr/share/man/man1/notmuch-reindex.1.gz
/usr/share/man/man1/notmuch-reply.1.gz
/usr/share/man/man1/notmuch-restore.1.gz
/usr/share/man/man1/notmuch-search.1.gz
/usr/share/man/man1/notmuch-setup.1.gz
/usr/share/man/man1/notmuch-show.1.gz
/usr/share/man/man1/notmuch-tag.1.gz
/usr/share/man/man1/notmuch.1.gz
/usr/share/man/man5/notmuch-hooks.5.gz
/usr/share/man/man7/notmuch-properties.7.gz
/usr/share/man/man7/notmuch-search-terms.7.gz
/usr/share/man/man7/notmuch-sexp-queries.7.gz
