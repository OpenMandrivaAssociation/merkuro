#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: plasma6-merkuro
Version: 24.02.0
Release: %{?git:0.%{git}.}2
%if 0%{?git:1}
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/merkuro/-/archive/%{gitbranch}/merkuro-%{gitbranchd}.tar.bz2#/merkuro-%{git}.tar.bz2
%else
Source0:        https://invent.kde.org/pim/merkuro/-/archive/master/merkuro-master.tar.bz2
%endif
%else
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/merkuro/-/archive/%{gitbranch}/merkuro-%{gitbranchd}.tar.bz2#/merkuro-%{git}.tar.bz2
%else
Source0:        https://download.kde.org/%{stable}/release-service/%{version}/src/merkuro-%{version}.tar.xz
%endif
%endif
Summary: Calendar application to sync with external services (Nextcloud, GMail, ...)
URL: https://invent.kde.org/pim/merkuro
License: GPL
Group: User Interface/Desktops
BuildRequires: cmake ninja
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6QmlModels)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(KF6CalendarCore)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6Contacts)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6ItemModels)
BuildRequires: cmake(KF6Kirigami2)
BuildRequires: cmake(Plasma) >= 6.0.0
BuildRequires: cmake(PlasmaQuick)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6QQC2DesktopStyle)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6KirigamiAddons)
BuildRequires: cmake(Freetype)
BuildRequires: cmake(Fontconfig)
BuildRequires: cmake(KPim6MailCommon)
BuildRequires: cmake(KPim6CalendarUtils)
BuildRequires: cmake(KPim6IdentityManagementCore)
BuildRequires: cmake(KPim6AkonadiCalendar)
BuildRequires: cmake(KPim6MailTransport)
BuildRequires: cmake(Gpgmepp)
BuildRequires: cmake(KF6TextTemplate)
BuildRequires: cmake(KPim6MimeTreeParserCore)

%description
A calendar application using Akonadi to sync with external services
(Nextcloud, GMail, ...)

%prep
%autosetup -p1 -n merkuro-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang merkuro --all-name

%files -f merkuro.lang
%{_bindir}/merkuro-calendar
%{_bindir}/merkuro-contact
%{_bindir}/merkuro-mail
%{_datadir}/applications/org.kde.merkuro.calendar.desktop
%{_datadir}/applications/org.kde.merkuro.contact.desktop
%{_datadir}/applications/org.kde.merkuro.mail.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/metainfo/*
%{_datadir}/plasma/plasmoids/org.kde.merkuro.contact
%{_datadir}/qlogging-categories6/akonadi.quick.categories
%{_datadir}/qlogging-categories6/merkuro.categories
%{_datadir}/qlogging-categories6/merkuro.contact.categories
%{_qtdir}/qml/org/kde/akonadi/*
%{_qtdir}/qml/org/kde/merkuro
