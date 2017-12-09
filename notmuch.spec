#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : notmuch
Version  : 0.25.3
Release  : 4
URL      : https://notmuchmail.org/releases/notmuch-0.25.3.tar.gz
Source0  : https://notmuchmail.org/releases/notmuch-0.25.3.tar.gz
Summary  : Thread-based email index, search and tagging
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 GPL-3.0+ LGPL-2.1
Requires: notmuch-bin
Requires: notmuch-lib
Requires: notmuch-data
BuildRequires : gmime
BuildRequires : gmime-dev
BuildRequires : go
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : ruby
BuildRequires : setuptools
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
Requires: notmuch-data

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
Requires: notmuch-lib
Requires: notmuch-bin
Requires: notmuch-data
Provides: notmuch-devel

%description dev
dev components for the notmuch package.


%package lib
Summary: lib components for the notmuch package.
Group: Libraries
Requires: notmuch-data

%description lib
lib components for the notmuch package.


%prep
%setup -q -n notmuch-0.25.3
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1512828056
%configure --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1512828056
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/notmuch
/usr/bin/notmuch-emacs-mua

%files data
%defattr(-,root,root,-)
/usr/share/emacs/site-lisp/coolj.el
/usr/share/emacs/site-lisp/notmuch-address.el
/usr/share/emacs/site-lisp/notmuch-company.el
/usr/share/emacs/site-lisp/notmuch-compat.el
/usr/share/emacs/site-lisp/notmuch-crypto.el
/usr/share/emacs/site-lisp/notmuch-draft.el
/usr/share/emacs/site-lisp/notmuch-hello.el
/usr/share/emacs/site-lisp/notmuch-jump.el
/usr/share/emacs/site-lisp/notmuch-lib.el
/usr/share/emacs/site-lisp/notmuch-logo.png
/usr/share/emacs/site-lisp/notmuch-maildir-fcc.el
/usr/share/emacs/site-lisp/notmuch-message.el
/usr/share/emacs/site-lisp/notmuch-mua.el
/usr/share/emacs/site-lisp/notmuch-parser.el
/usr/share/emacs/site-lisp/notmuch-print.el
/usr/share/emacs/site-lisp/notmuch-query.el
/usr/share/emacs/site-lisp/notmuch-show.el
/usr/share/emacs/site-lisp/notmuch-tag.el
/usr/share/emacs/site-lisp/notmuch-tree.el
/usr/share/emacs/site-lisp/notmuch-version.el
/usr/share/emacs/site-lisp/notmuch-wash.el
/usr/share/emacs/site-lisp/notmuch.el
/usr/share/zsh/functions/Completion/Unix/_notmuch

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libnotmuch.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libnotmuch.so.5
/usr/lib64/libnotmuch.so.5.0.0
