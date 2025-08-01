#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: merkuro
Version: 25.04.3
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/merkuro/-/archive/%{gitbranch}/merkuro-%{gitbranchd}.tar.bz2#/merkuro-%{git}.tar.bz2
%else
Source0:        https://download.kde.org/%{stable}/release-service/%{version}/src/merkuro-%{version}.tar.xz
%endif
Summary: Calendar application to sync with external services (Nextcloud, GMail, ...)
URL: https://invent.kde.org/pim/merkuro
License: GPL
Group: User Interface/Desktops
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Location)
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
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6Holidays)
BuildRequires: cmake(Plasma) >= 6.0.0
BuildRequires: cmake(PlasmaQuick)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6QQC2DesktopStyle)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6KirigamiAddons)
BuildRequires: cmake(KPim6AkonadiSearch)
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

%rename plasma6-merkuro

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
A calendar application using Akonadi to sync with external services
(Nextcloud, GMail, ...)

%files -f %{name}.lang
%{_bindir}/merkuro-calendar
%{_bindir}/merkuro-contact
%{_bindir}/merkuro-mail
%{_datadir}/applications/org.kde.merkuro.calendar.desktop
%{_datadir}/applications/org.kde.merkuro.contact.desktop
%{_datadir}/applications/org.kde.merkuro.mail.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/metainfo/*
%{_datadir}/plasma/plasmoids/org.kde.merkuro.contact.applet
%{_datadir}/qlogging-categories6/akonadi.quick.categories
%{_datadir}/qlogging-categories6/merkuro.categories
%{_datadir}/qlogging-categories6/merkuro.contact.categories
%{_datadir}/knotifications6/merkuro.mail.notifyrc
%{_libdir}/libMerkuroComponents.so*
%{_libdir}/libmerkuro_contact.so*
%{_qtdir}/qml/org/kde/akonadi/*
%{_qtdir}/qml/org/kde/merkuro
%{_datadir}/applications/org.kde.merkuro.desktop
