Summary:	lximage-qt
Name:		lximage-qt
Version:	0.4.0
Release:	1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Libraries
Source0:	http://downloads.lxqt.org/lximage-qt/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	0bd2c6474d8d9c73b606e81647e777f0
URL:		http://www.lxqt.org/
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Xml-devel
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
%setup -q

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

%find_lang %{name} --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lximage-qt
%{_desktopdir}/lximage-qt-screenshot.desktop
%{_desktopdir}/lximage-qt.desktop
%{_iconsdir}/hicolor/48x48/apps/lximage-qt.png
%dir %{_datadir}/lximage-qt
%dir %{_datadir}/lximage-qt/translations
