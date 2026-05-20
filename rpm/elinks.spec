Name:           elinks
Version:        0.19.1
Release:        1
Summary:        ELinks is a program for browsing the web in text mode
Url:            http://elinks.or.cz/
Source0:        %{name}-%{version}.tar.bz2
License:        GPLv2
BuildRequires:  autoconf
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(nspr)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(mozjs185)

%description
ELinks is a program for browsing the web in text mode.

%package docs
Summary: Elinks documentation package

%description docs
Documentation for Elinks - a program for browsing the web in text mode.

%prep
%autosetup -n %{name}-%{version}/upstream

%build
./autogen.sh
%configure --enable-256-colors
%make_build

%install
%make_install

%files
%defattr(-,root,root)
%{_bindir}/elinks
%exclude %{_datadir}/locale/

%files docs
%defattr(-,root,root)
%{_datadir}/man/man1/*
%{_datadir}/man/man5/*

