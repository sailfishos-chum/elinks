Name:           elinks
Version:        0.19.1
Release:        1
Summary:        ELinks is a program for browsing the web in text mode
Url:            http://elinks.or.cz/
Source0:        %{name}-%{version}.tar.bz2
License:        GPLv2
BuildRequires:  meson
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
%meson \
-D256-colors=true \
%{nil}
%meson_build

%install
%meson_install

%files
%{_bindir}/elinks
%exclude %{_datadir}/locale/

%files docs
%{_datadir}/man/man1/*
%{_datadir}/man/man5/*

