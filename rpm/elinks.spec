Name:           elinks

%define __meson_auto_features disabled

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

%if 0%{?_chum}
Type: console-application
PackagedBy: llewelld
%endif

%prep
%autosetup -n %{name}-%{version}/upstream

%build
%meson \
-D256-colors=true \
-D88-colors=true \
-Dapidoc=false \
-Dbacktrace=false \
-Dbittorrent=false \
-Dbrotli=false \
-Ddoc=false \
-Dgpm=false \
-Dhtmldoc=false \
-Dlibev=true \
-Dnls=false \
-Dpdfdoc=false \
-Dterminfo=true \
-Dtre=false \
%{nil}

#TODO:
#libavif', type: 'boolean', value: false, description: 'support for AVIF images')
#libwebp', type: 'boolean', value: false, description: 'support for WEBP images')

%meson_build

%install
%meson_install

rm -rf %{buildroot}%{_mandir}/*

%files
%{_bindir}/elinks
%exclude %{_datadir}/locale/
