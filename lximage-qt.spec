#
# Conditional build:
#
%define         qtver           6.6.0

Summary:	The image viewer and screenshot tool for LXQt
Summary(pl.UTF-8):	Przeglądarka obrazów i narzędzie do tworzenia zrzutów ekranu dla LXQt
Name:		lximage-qt
Version:	2.3.0
Release:	1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Libraries
Source0:	https://github.com/lxqt/lximage-qt/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	96ada4e4bbc8e72d315202a615a3c4ec
URL:		http://www.lxqt.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6DBus-devel >= %{qtver}
BuildRequires:	Qt6Network-devel >= %{qtver}
BuildRequires:	Qt6PrintSupport-devel >= %{qtver}
BuildRequires:	Qt6Svg-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.18.0
BuildRequires:	cups-devel
BuildRequires:	libexif-devel
BuildRequires:	libfm-qt-devel >= 2.3.0
BuildRequires:	lxqt-build-tools >= 2.3.0
BuildRequires:	qt6-linguist >= %{qtver}
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xz-devel
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Qt port of LXImage, a simple and fast image viewer.

%description -l pl.UTF-8
Port Qt aplikacji LXImage, prostej i szybkiej przeglądarki obrazów.

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%prep
%setup -q

%build
%cmake -B build

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lximage-qt
%{_desktopdir}/lximage-qt.desktop
%{_iconsdir}/hicolor/48x48/apps/lximage-qt.svg
%{_datadir}/metainfo/lximage-qt.metainfo.xml
%dir %{_datadir}/lximage-qt
# required for the lang files
%dir %{_datadir}/lximage-qt/translations
