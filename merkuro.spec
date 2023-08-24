%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: merkuro
Version: 23.08.0
Release: 1
%if 0%{?git:1}
Source0:        https://invent.kde.org/pim/%{name}/-/archive/master/%{name}-master.tar.bz2
%else
Source0:        https://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%endif
Summary: Calendar application to sync with external services (Nextcloud, GMail, ...)
URL: https://invent.kde.org/pim/merkuro
License: GPL
Group: User Interface/Desktops
BuildRequires: cmake ninja

%description
A calendar application using Akonadi to sync with external services
(Nextcloud, GMail, ...)

%prep
%autosetup -p1
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang %{name} --all-name

%files -f %{name}.lang
%{_bindir}/merkuro-calendar
%{_bindir}/merkuro-contact
%{_bindir}/merkuro-mail
%{_datadir}/applications/org.kde.merkuro.calendar.desktop
%{_datadir}/applications/org.kde.merkuro.contact.desktop
%{_datadir}/applications/org.kde.merkuro.mail.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/metainfo/*
%{_datadir}/plasma/plasmoids/org.kde.merkuro.contact
%{_datadir}/qlogging-categories5/akonadi.quick.categories
%{_datadir}/qlogging-categories5/merkuro.categories
%{_datadir}/qlogging-categories5/merkuro.contact.categories
%{_libdir}/qt5/qml/org/kde/akonadi/*
%{_libdir}/qt5/qml/org/kde/merkuro
