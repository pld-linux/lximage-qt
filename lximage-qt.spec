%define		qtver		4.8.5

Summary:	lximage-qt
Name:		lximage-qt
Version:	0.2.0
Release:	0.1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Libraries
Source0:	http://lxqt.org/downloads/lximage-qt/0.2.0/%{name}-%{version}.tar.xz
# Source0-md5:	e45ab2d0308cb80046d41a7ab0f97110
URL:		http://www.lxqt.org/
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtXml-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.3
BuildRequires:	glib2-devel
BuildRequires:	libexif-devel
BuildRequires:	libfm-devel
BuildRequires:	pcmanfm-qt-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lximage-qt

%prep
%setup -q -c %{name}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lximage-qt
%{_desktopdir}/lximage-qt-screenshot.desktop
%{_desktopdir}/lximage-qt.desktop
%{_iconsdir}/hicolor/48x48/apps/lximage-qt.png
%dir %{_datadir}/lximage-qt
%dir %{_datadir}/lximage-qt/translations
%lang(zn_TW) %{_datadir}/lximage-qt/translations/lximage-qt_zh_TW.qm
